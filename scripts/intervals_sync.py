#!/usr/bin/env python3
"""
Intervals.icu Open API & Garmin Data Integration for Endurance Blueprint.

Implements the official Intervals.icu REST / OpenAPI specification:
- Swagger Docs: https://intervals.icu/api/v1/docs/swagger-ui/index.html
- Feature Overview: https://www.intervals.icu/features/open-api/

Features:
1. Pulls Fitness (CTL), Fatigue (ATL), Form (TSB), Ramp Rate, HRV, Resting HR, and Sleep.
2. Pulls recent completed activities synced from Garmin Connect, Wahoo, Strava, and Zwift.
3. Renders live `fitness-dashboard.md` with race countdowns and recovery interpretation.
4. Supports pushing structured text workouts to Intervals.icu calendar for direct Garmin device sync.
5. Uses Python standard library only (zero external pip dependencies).
"""

import os
import sys
import json
import base64
import argparse
from datetime import datetime, timedelta
import urllib.request
import urllib.error

INTERVALS_API_BASE = "https://intervals.icu/api/v1"

def load_env(env_path=".env"):
    """Load KEY=VALUE pairs from a .env file if present."""
    if not os.path.exists(env_path):
        return
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key, val = key.strip(), val.strip().strip("\"'")
            if key not in os.environ:
                os.environ[key] = val

def make_api_request(endpoint, api_key, method="GET", payload=None):
    """
    Execute authenticated HTTP request using Intervals.icu OpenAPI specification:
    - Authentication: Basic Auth with username 'API_KEY' and athlete's personal API key.
    """
    url = f"{INTERVALS_API_BASE}{endpoint}" if endpoint.startswith("/") else f"{INTERVALS_API_BASE}/{endpoint}"
    auth_str = f"API_KEY:{api_key}"
    auth_header = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "EnduranceBlueprint/1.0"
    }

    data = json.dumps(payload).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            resp_body = resp.read().decode("utf-8")
            return json.loads(resp_body) if resp_body else {}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        print(f"[!] HTTP Error {e.code} for {url}: {error_body}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"[!] Network or parsing error for {url}: {e}", file=sys.stderr)
        raise

def get_countdown(target_date_str):
    """Calculate days remaining until target race date."""
    target = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    diff = (target - today).days
    if diff > 0:
        return f"**{diff} days**"
    elif diff == 0:
        return "**🔥 RACE DAY TODAY!**"
    else:
        return f"Completed ({abs(diff)} days ago)"

def calculate_tsb_status(tsb):
    """Interpret Training Stress Balance (Form) relative to race readiness."""
    if tsb is None:
        return "N/A"
    if tsb > 15:
        return "🟢 **Fresh / Transition** (Low fatigue; ideal for post-race recovery or pre-block test)"
    elif 0 <= tsb <= 15:
        return "🟢 **Optimal Race Readiness** (Supercompensated, race-primed, fresh nervous system)"
    elif -10 <= tsb < 0:
        return "🟡 **Productive Training Zone** (Optimal physiological adaptation & sustainable building)"
    elif -30 <= tsb < -10:
        return "🟠 **High Fatigue / Overload** (Heavy block load; monitor recovery & sleep markers closely)"
    else:
        return "🔴 **High Exhaustion & Injury Risk** (Excessive accumulated fatigue; immediate deload advised)"

def generate_dashboard(data, athlete_profile=None, mock=False):
    """Generate comprehensive Markdown dashboard content."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    ctl = data.get("ctl", 0.0)
    atl = data.get("atl", 0.0)
    tsb = round(ctl - atl, 1) if (ctl is not None and atl is not None) else 0.0
    ramp_rate = data.get("rampRate", 0.0)
    resting_hr = data.get("restingHR", "-")
    weight = data.get("weight", "-")
    hrv = data.get("hrv", "-")
    sleep_hrs = data.get("sleep_hours", "-")
    sleep_score = data.get("sleepScore", "-")
    
    status_text = calculate_tsb_status(tsb)
    mock_notice = "> [!NOTE]\n> *Currently showing baseline demo data. Add your `INTERVALS_API_KEY` to `.env` to stream live Garmin & Intervals data.*\n\n" if mock else ""

    # Athlete metadata if available
    profile_md = ""
    if athlete_profile:
        name = athlete_profile.get("name", "Athlete")
        ftp = athlete_profile.get("icu_ftp", "-")
        lthr = athlete_profile.get("icu_lthr", "-")
        max_hr = athlete_profile.get("icu_max_hr", "-")
        profile_md = f"**Athlete Profile:** {name} | **FTP:** {ftp} W | **LTHR:** {lthr} bpm | **Max HR:** {max_hr} bpm\n\n"

    # Activities table
    activities_md = ""
    activities = data.get("recent_activities", [])
    if activities:
        activities_md = "| Date | Sport | Activity Title | Distance | Duration | Avg HR | Power / Pace | Load (TSS) |\n"
        activities_md += "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
        for act in activities[:10]:
            date = act.get("start_date_local", "")[:10]
            sport = act.get("type", "Workout")
            name = act.get("name", "Training Session")
            dist = act.get("distance_km", 0.0)
            dist_str = f"{dist:.1f} km" if dist > 0 else "-"
            dur_mins = act.get("moving_time_mins", 0)
            hrs = dur_mins // 60
            mins = dur_mins % 60
            time_str = f"{hrs}h {mins:02d}m" if hrs > 0 else f"{mins}m"
            avg_hr = act.get("average_heartrate", "-")
            load = act.get("icu_training_load", "-")
            metric = act.get("primary_metric", "-")
            activities_md += f"| **{date}** | {sport} | {name} | {dist_str} | {time_str} | {avg_hr} bpm | {metric} | {load} |\n"
    else:
        activities_md = "_No recent activities recorded._\n"

    content = f"""# 📊 Endurance Blueprint: Fitness & Readiness Dashboard

{mock_notice}{profile_md}*Last Updated: {now_str} via [Intervals.icu Open API](https://www.intervals.icu/features/open-api/)*

---

## 🎯 Target Race Countdowns

| Event | Target Date | Countdown | Goal Standard | Focus Disciplines |
| :--- | :--- | :--- | :--- | :--- |
| **Sub-1:30 Half Marathon** | 2026-11-29 | {get_countdown("2026-11-29")} | **Sub-1:30:00** (6:51/mi) | Threshold Run + Road Cycling Base |
| **IRONMAN 70.3 Oceanside** | 2027-04-03 | {get_countdown("2027-04-03")} | **Sub-5:00:00** (4:51:30) | Harbor Swim + Pendleton Hills + Brick Runs |
| **IRONMAN California** | 2027-10-18 | {get_countdown("2027-10-18")} | **Sub-10:00:00** (9:48:30) | River Swim + 112m Delta Aero + Marathon |
| **Sub-3:00 Marathon (CIM / PR)** | 2027-12-05 | {get_countdown("2027-12-05")} | **Sub-3:00:00** (6:49/mi) | Marathon Specificity + Post-Ironman Speed |

---

## ⚡ Current Fitness & Fatigue Metrics

| Metric | Current Value | Physiological Purpose & Interpretation |
| :--- | :--- | :--- |
| **Fitness (CTL)** | **{ctl}** | Chronic Training Load (~42-day rolling exponential weighted average). Represents total cardiovascular aerobic engine. |
| **Fatigue (ATL)** | **{atl}** | Acute Training Load (~7-day rolling weighted average). Reflects short-term training fatigue and stress. |
| **Form (TSB)** | **{tsb}** | Training Stress Balance ($CTL - ATL$). Governs fresh leg readiness vs training fatigue state. |
| **Ramp Rate** | **{ramp_rate:+.1f} / wk** | Weekly change in CTL. Safe progression: $+3$ to $+7$ load points per week. |
| **Resting HR** | **{resting_hr}** bpm | Parasympathetic health marker; elevation of 5+ bpm flags incomplete recovery. |
| **HRV (RMSSD)** | **{hrv}** ms | Autonomic nervous system balance; higher scores indicate strong adaptability. |
| **Sleep** | **{sleep_hrs}** (Score: {sleep_score}) | Primary recovery window for tissue repair and growth hormone release. |
| **Current Weight** | **{weight}** kg | Monitored for power-to-weight ratio and race nutrition hydration balancing. |

### 🧭 Form & Readiness Status
> {status_text}

---

## 🏃🚴🏊 Recent Activity Stream (Garmin / Intervals.icu)

{activities_md}
---

## 🔄 How to Refresh Live Data

```bash
# Pull live data from Intervals.icu / Garmin:
python3 scripts/intervals_sync.py

# Push a structured workout to Intervals.icu calendar (syncs to Garmin):
python3 scripts/intervals_sync.py --push-workout "Tuesday Threshold Run" "Warmup\n- 15m Z2\n\nMain Set 3x\n- 2mi 6:30/mi\n- 2m Z1\n\nCooldown\n- 10m Z2"
```
"""
    return content

def get_mock_data():
    """Realistic demo data for testing when credentials are not yet supplied."""
    return {
        "ctl": 78.5,
        "atl": 84.2,
        "rampRate": 4.1,
        "restingHR": 44,
        "hrv": 68,
        "weight": 72.5,
        "sleep_hours": "7h 45m",
        "sleepScore": 86,
        "recent_activities": [
            {
                "start_date_local": "2026-09-20T08:00:00",
                "type": "Ride",
                "name": "Saturday Long Road Aerobic Ride",
                "distance_km": 82.4,
                "moving_time_mins": 185,
                "average_heartrate": 134,
                "primary_metric": "195 W (Zone 2)",
                "icu_training_load": 142
            },
            {
                "start_date_local": "2026-09-19T06:30:00",
                "type": "Run",
                "name": "Quality Long Run with Fast Finish",
                "distance_km": 19.3,
                "moving_time_mins": 86,
                "average_heartrate": 154,
                "primary_metric": "7:10 / mi avg",
                "icu_training_load": 98
            },
            {
                "start_date_local": "2026-09-17T17:15:00",
                "type": "Run",
                "name": "Lactate Threshold Intervals 3x2mi",
                "distance_km": 14.5,
                "moving_time_mins": 62,
                "average_heartrate": 164,
                "primary_metric": "6:30 / mi reps",
                "icu_training_load": 85
            },
            {
                "start_date_local": "2026-09-16T07:00:00",
                "type": "Swim",
                "name": "CSS Threshold Intervals 5x200m",
                "distance_km": 2.5,
                "moving_time_mins": 45,
                "average_heartrate": 138,
                "primary_metric": "1:34 / 100m",
                "icu_training_load": 52
            }
        ]
    }

def fetch_live_intervals_data(athlete_id, api_key):
    """
    Fetch wellness and activity streams using Intervals.icu OpenAPI endpoints:
    - GET /api/v1/athlete/{id}
    - GET /api/v1/athlete/{id}/wellness
    - GET /api/v1/athlete/{id}/activities
    """
    today = datetime.now().date()
    oldest = (today - timedelta(days=14)).isoformat()
    newest = today.isoformat()
    
    print(f"[+] Connecting to Intervals.icu OpenAPI for athlete ID '{athlete_id}'...")

    # 1. Fetch Athlete Profile
    athlete_profile = None
    try:
        athlete_profile = make_api_request(f"/athlete/{athlete_id}", api_key)
    except Exception as e:
        print(f"[*] Note: Could not fetch athlete profile ({e}). Continuing...")

    # 2. Fetch Wellness
    wellness_list = make_api_request(f"/athlete/{athlete_id}/wellness?oldest={oldest}&newest={newest}", api_key)
    latest_wellness = wellness_list[-1] if isinstance(wellness_list, list) and wellness_list else {}

    # 3. Fetch Activities
    activities_list = make_api_request(f"/athlete/{athlete_id}/activities?oldest={oldest}&newest={newest}", api_key)
    
    activities_clean = []
    if isinstance(activities_list, list):
        for act in sorted(activities_list, key=lambda x: x.get("start_date_local", ""), reverse=True):
            avg_watts = act.get("icu_weighted_avg_watts") or act.get("average_watts")
            avg_speed = act.get("average_speed") or act.get("icu_average_speed")
            
            # Format primary performance metric
            sport = act.get("type", "Activity")
            if sport in ["Ride", "VirtualRide"] and avg_watts:
                metric = f"{round(avg_watts)} W"
            elif sport in ["Run", "VirtualRun"] and avg_speed and avg_speed > 0:
                # Pace in min/mi
                sec_per_mi = 1609.344 / avg_speed
                pace_m = int(sec_per_mi // 60)
                pace_s = int(sec_per_mi % 60)
                metric = f"{pace_m}:{pace_s:02d} / mi"
            elif avg_speed and avg_speed > 0:
                metric = f"{round(avg_speed * 3.6, 1)} km/h"
            else:
                metric = "-"

            activities_clean.append({
                "start_date_local": act.get("start_date_local", ""),
                "type": sport,
                "name": act.get("name", "Workout"),
                "distance_km": round(act.get("distance", 0) / 1000.0, 1),
                "moving_time_mins": round(act.get("moving_time", 0) / 60),
                "average_heartrate": round(act.get("average_heartrate", 0)) if act.get("average_heartrate") else "-",
                "primary_metric": metric,
                "icu_training_load": act.get("icu_training_load", "-")
            })

    # Sleep calculation
    sleep_secs = latest_wellness.get("sleepSecs")
    sleep_hours_str = "-"
    if sleep_secs:
        sh = sleep_secs // 3600
        sm = (sleep_secs % 3600) // 60
        sleep_hours_str = f"{sh}h {sm:02d}m"

    metrics = {
        "ctl": latest_wellness.get("ctl", 0.0),
        "atl": latest_wellness.get("atl", 0.0),
        "rampRate": latest_wellness.get("rampRate", 0.0),
        "restingHR": latest_wellness.get("restingHR", "-"),
        "hrv": latest_wellness.get("hrv", "-"),
        "weight": latest_wellness.get("weight", "-"),
        "sleep_hours": sleep_hours_str,
        "sleepScore": latest_wellness.get("sleepScore", "-"),
        "recent_activities": activities_clean
    }
    
    return metrics, athlete_profile

def push_structured_workout(athlete_id, api_key, workout_name, workout_description, target_date=None, sport="Run"):
    """
    Push a structured text workout to Intervals.icu calendar via OpenAPI POST /events.
    Intervals.icu automatically converts the text workout into Garmin structured workout steps!
    """
    date_str = target_date or datetime.now().strftime("%Y-%m-%dT06:00:00")
    payload = {
        "category": "WORKOUT",
        "start_date_local": date_str,
        "type": sport,
        "name": workout_name,
        "description": workout_description
    }
    
    print(f"[+] Pushing workout '{workout_name}' to Intervals.icu for {date_str}...")
    res = make_api_request(f"/athlete/{athlete_id}/events", api_key, method="POST", payload=payload)
    print(f"[✓] Workout created successfully! Event ID: {res.get('id', 'N/A')}")
    print("[*] Intervals.icu will automatically sync this workout to your Garmin device.")
    return res

def main():
    parser = argparse.ArgumentParser(description="Endurance Blueprint: Intervals.icu OpenAPI & Garmin Sync")
    parser.add_argument("--mock", action="store_true", help="Generate dashboard using realistic demo data")
    parser.add_argument("--output", default="fitness-dashboard.md", help="Output path for fitness dashboard")
    parser.add_argument("--push-workout", nargs=2, metavar=("NAME", "DESCRIPTION"), help="Push structured workout (e.g. --push-workout 'Threshold Run' 'Warmup\\n- 15m Z2')")
    parser.add_argument("--date", help="Target date for workout in YYYY-MM-DDTHH:MM:SS format")
    parser.add_argument("--sport", default="Run", choices=["Run", "Ride", "Swim", "Other"], help="Sport type for pushed workout")
    args = parser.parse_args()

    load_env()
    
    # In Intervals.icu OpenAPI, athlete ID "0" refers to the authenticated user of the API key
    athlete_id = os.environ.get("INTERVALS_ATHLETE_ID") or "0"
    api_key = os.environ.get("INTERVALS_API_KEY")
    
    # Handle Workout Push
    if args.push_workout:
        if not api_key or api_key == "your_intervals_api_key_here":
            print("[!] Error: You must specify a valid INTERVALS_API_KEY in .env to push workouts.", file=sys.stderr)
            sys.exit(1)
        w_name, w_desc = args.push_workout
        push_structured_workout(athlete_id, api_key, w_name, w_desc.replace("\\n", "\n"), target_date=args.date, sport=args.sport)
        return

    # Handle Dashboard Sync
    is_mock = args.mock or not (api_key and api_key != "your_intervals_api_key_here")

    if is_mock:
        print("[!] No valid INTERVALS_API_KEY found or --mock requested.")
        print("[*] Generating dashboard with baseline reference data...")
        data = get_mock_data()
        profile = {"name": "Adi Zimmerman (Baseline)", "icu_ftp": 260, "icu_lthr": 172, "icu_max_hr": 188}
    else:
        try:
            data, profile = fetch_live_intervals_data(athlete_id, api_key)
            print("[✓] Live metrics fetched successfully via Intervals.icu OpenAPI!")
        except Exception as e:
            print(f"[!] Falling back to baseline data due to connection error: {e}", file=sys.stderr)
            data = get_mock_data()
            profile = None
            is_mock = True

    dashboard_md = generate_dashboard(data, athlete_profile=profile, mock=is_mock)
    
    with open(args.output, "w") as f:
        f.write(dashboard_md)
    
    print(f"[✓] Successfully generated {args.output}")

if __name__ == "__main__":
    main()
