#!/usr/bin/env python3
"""
Intervals.icu & Garmin Data Sync for Endurance Blueprint.

Pulls Fitness (CTL), Fatigue (ATL), Form (TSB), Wellness, and Activity data
from Intervals.icu (which automatically syncs with Garmin, Wahoo, Strava, and Zwift)
and updates `fitness-dashboard.md` in the repository root.

Uses Python standard library only (zero external dependencies).
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
    """Load simple KEY=VALUE pairs from a .env file if present."""
    if not os.path.exists(env_path):
        return
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key, val = key.strip(), val.strip()
            if key not in os.environ:
                os.environ[key] = val.strip("\"'")

def make_request(url, api_key):
    """Execute authenticated HTTP GET request using standard urllib."""
    auth_header = base64.b64encode(f"API_KEY:{api_key}".encode("utf-8")).decode("utf-8")
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Basic {auth_header}",
            "User-Agent": "EnduranceBlueprint/1.0"
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

def get_countdown(target_date_str):
    """Calculate days remaining until race day."""
    target = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    diff = (target - today).days
    if diff > 0:
        return f"**{diff} days**"
    elif diff == 0:
        return "**RACE DAY TODAY!**"
    else:
        return f"Completed ({abs(diff)} days ago)"

def calculate_tsb_status(tsb):
    """Interpret Training Stress Balance (Form)."""
    if tsb is None:
        return "N/A"
    if tsb > 15:
        return "🟢 **Fresh / Transition** (Low fatigue, tapering or deconditioning)"
    elif 0 <= tsb <= 15:
        return "🟢 **Optimal Race Readiness** (Tapered, race-primed)"
    elif -10 <= tsb < 0:
        return "🟡 **Productive Training Zone** (Optimal adaptation & fitness build)"
    elif -30 <= tsb < -10:
        return "🟠 **High Fatigue / Overload** (Hard training block; monitor recovery)"
    else:
        return "🔴 **High Injury & Exhaustion Risk** (Excessive fatigue; deload advised)"

def generate_dashboard(data, mock=False):
    """Generate Markdown dashboard content."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    ctl = data.get("ctl", 0.0)
    atl = data.get("atl", 0.0)
    tsb = round(ctl - atl, 1) if (ctl is not None and atl is not None) else 0.0
    ramp_rate = data.get("rampRate", 0.0)
    resting_hr = data.get("restingHR", "N/A")
    weight = data.get("weight", "N/A")
    hrv = data.get("hrv", "N/A")
    
    status_text = calculate_tsb_status(tsb)
    mock_notice = "> [!NOTE]\n> *Currently displaying demo / placeholder data. Configure `.env` with your Intervals.icu API Key to stream live Garmin/Intervals data.*\n\n" if mock else ""

    activities_md = ""
    activities = data.get("recent_activities", [])
    if activities:
        activities_md = "| Date | Sport | Title | Distance | Duration | Avg HR | Power / Pace | Load / TSS |\n"
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
        activities_md = "_No recent activities loaded._\n"

    content = f"""# 📊 Endurance Blueprint: Fitness & Readiness Dashboard

{mock_notice}*Last Updated: {now_str}*

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

| Metric | Value | Description & Purpose |
| :--- | :--- | :--- |
| **Fitness (CTL)** | **{ctl}** | Chronic Training Load (~42-day rolling exponential weighted average). Represents total aerobic engine. |
| **Fatigue (ATL)** | **{atl}** | Acute Training Load (~7-day rolling weighted average). Represents recent training fatigue. |
| **Form (TSB)** | **{tsb}** | Training Stress Balance ($CTL - ATL$). Indicates readiness to race or train hard. |
| **Ramp Rate** | **{ramp_rate:+.1f} / wk** | Weekly change in CTL. Ideal range: $+3$ to $+7$ per week to prevent overtraining. |
| **Resting HR** | **{resting_hr}** bpm | Lower baseline indicates strong parasympathetic tone and recovery. |
| **HRV (RMSSD)** | **{hrv}** ms | Heart Rate Variability baseline metric. |
| **Current Weight** | **{weight}** kg | Monitored for power-to-weight and hydration tracking. |

### 🧭 Current Status Interpretation
> {status_text}

---

## 🏃🚴🏊 Recent Activity Log (Garmin / Intervals.icu)

{activities_md}
---

## 🔄 How to Refresh Live Data

To refresh this dashboard with live data from your Garmin / Intervals.icu account:

```bash
# 1. Ensure your .env has INTERVALS_ATHLETE_ID and INTERVALS_API_KEY
# 2. Run the sync script:
python3 scripts/intervals_sync.py
```
"""
    return content

def get_mock_data():
    """Fallback sample data when API keys are not yet configured."""
    return {
        "ctl": 78.5,
        "atl": 84.2,
        "rampRate": 4.1,
        "restingHR": 44,
        "hrv": 68,
        "weight": 72.5,
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

def fetch_live_data(athlete_id, api_key):
    """Fetch real metrics from Intervals.icu."""
    today = datetime.now().date()
    oldest = (today - timedelta(days=14)).isoformat()
    newest = today.isoformat()
    
    wellness_url = f"{INTERVALS_API_BASE}/athlete/{athlete_id}/wellness?oldest={oldest}&newest={newest}"
    activities_url = f"{INTERVALS_API_BASE}/athlete/{athlete_id}/activities?oldest={oldest}&newest={newest}"
    
    print(f"[+] Connecting to Intervals.icu for athlete '{athlete_id}'...")
    wellness_data = make_request(wellness_url, api_key)
    activities_data = make_request(activities_url, api_key)
    
    latest_wellness = wellness_data[-1] if isinstance(wellness_data, list) and wellness_data else {}
    
    activities_clean = []
    if isinstance(activities_data, list):
        for act in sorted(activities_data, key=lambda x: x.get("start_date_local", ""), reverse=True):
            activities_clean.append({
                "start_date_local": act.get("start_date_local", ""),
                "type": act.get("type", "Activity"),
                "name": act.get("name", "Workout"),
                "distance_km": round(act.get("distance", 0) / 1000.0, 1),
                "moving_time_mins": round(act.get("moving_time", 0) / 60),
                "average_heartrate": round(act.get("average_heartrate", 0)) if act.get("average_heartrate") else "-",
                "primary_metric": f"{round(act.get('icu_weighted_avg_watts', 0))} W" if act.get("icu_weighted_avg_watts") else f"{round(act.get('icu_average_speed', 0)*3.6, 1)} km/h",
                "icu_training_load": act.get("icu_training_load", "-")
            })

    return {
        "ctl": latest_wellness.get("ctl", 0.0),
        "atl": latest_wellness.get("atl", 0.0),
        "rampRate": latest_wellness.get("rampRate", 0.0),
        "restingHR": latest_wellness.get("restingHR", "-"),
        "hrv": latest_wellness.get("hrv", "-"),
        "weight": latest_wellness.get("weight", "-"),
        "recent_activities": activities_clean
    }

def main():
    parser = argparse.ArgumentParser(description="Sync Intervals.icu / Garmin training data to Endurance Blueprint")
    parser.add_argument("--mock", action="store_true", help="Force mock data generation without API call")
    parser.add_argument("--output", default="fitness-dashboard.md", help="Output Markdown file path")
    args = parser.parse_args()

    load_env()
    
    athlete_id = os.environ.get("INTERVALS_ATHLETE_ID")
    api_key = os.environ.get("INTERVALS_API_KEY")
    
    is_mock = args.mock or not (athlete_id and api_key and api_key != "your_intervals_api_key_here")

    if is_mock:
        print("[!] No valid INTERVALS_API_KEY found or --mock enabled.")
        print("[*] Generating dashboard with realistic training baseline data...")
        data = get_mock_data()
    else:
        try:
            data = fetch_live_data(athlete_id, api_key)
            print("[✓] Successfully retrieved live metrics from Intervals.icu!")
        except Exception as e:
            print(f"[!] Error connecting to Intervals.icu ({e}). Falling back to baseline data.", file=sys.stderr)
            data = get_mock_data()
            is_mock = True

    markdown_content = generate_dashboard(data, mock=is_mock)
    
    with open(args.output, "w") as f:
        f.write(markdown_content)
    
    print(f"[✓] Dashboard written to {args.output}")

if __name__ == "__main__":
    main()
