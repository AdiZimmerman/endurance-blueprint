# 📊 Endurance Blueprint: Fitness & Readiness Dashboard

> [!NOTE]
> *Currently showing baseline demo data. Add your `INTERVALS_API_KEY` to `.env` to stream live Garmin & Intervals data.*

**Athlete Profile:** Adi Zimmerman (Baseline) | **FTP:** 260 W | **LTHR:** 172 bpm | **Max HR:** 188 bpm

*Last Updated: 2026-09-21 11:19:44 UTC via [Intervals.icu Open API](https://www.intervals.icu/features/open-api/)*

---

## 🎯 Target Race Countdowns

| Event | Target Date | Countdown | Goal Standard | Focus Disciplines |
| :--- | :--- | :--- | :--- | :--- |
| **Sub-1:30 Half Marathon** | 2026-11-29 | **69 days** | **Sub-1:30:00** (6:51/mi) | Threshold Run + Road Cycling Base |
| **IRONMAN 70.3 Oceanside** | 2027-04-03 | **194 days** | **Sub-5:00:00** (4:51:30) | Harbor Swim + Pendleton Hills + Brick Runs |
| **IRONMAN California** | 2027-10-18 | **392 days** | **Sub-10:00:00** (9:48:30) | River Swim + 112m Delta Aero + Marathon |
| **Sub-3:00 Marathon (CIM / PR)** | 2027-12-05 | **440 days** | **Sub-3:00:00** (6:49/mi) | Marathon Specificity + Post-Ironman Speed |

---

## ⚡ Current Fitness & Fatigue Metrics

| Metric | Current Value | Physiological Purpose & Interpretation |
| :--- | :--- | :--- |
| **Fitness (CTL)** | **78.5** | Chronic Training Load (~42-day rolling exponential weighted average). Represents total cardiovascular aerobic engine. |
| **Fatigue (ATL)** | **84.2** | Acute Training Load (~7-day rolling weighted average). Reflects short-term training fatigue and stress. |
| **Form (TSB)** | **-5.7** | Training Stress Balance ($CTL - ATL$). Governs fresh leg readiness vs training fatigue state. |
| **Ramp Rate** | **+4.1 / wk** | Weekly change in CTL. Safe progression: $+3$ to $+7$ load points per week. |
| **Resting HR** | **44** bpm | Parasympathetic health marker; elevation of 5+ bpm flags incomplete recovery. |
| **HRV (RMSSD)** | **68** ms | Autonomic nervous system balance; higher scores indicate strong adaptability. |
| **Sleep** | **7h 45m** (Score: 86) | Primary recovery window for tissue repair and growth hormone release. |
| **Current Weight** | **72.5** kg | Monitored for power-to-weight ratio and race nutrition hydration balancing. |

### 🧭 Form & Readiness Status
> 🟡 **Productive Training Zone** (Optimal physiological adaptation & sustainable building)

---

## 🏃🚴🏊 Recent Activity Stream (Garmin / Intervals.icu)

| Date | Sport | Activity Title | Distance | Duration | Avg HR | Power / Pace | Load (TSS) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-09-20** | Ride | Saturday Long Road Aerobic Ride | 82.4 km | 3h 05m | 134 bpm | 195 W (Zone 2) | 142 |
| **2026-09-19** | Run | Quality Long Run with Fast Finish | 19.3 km | 1h 26m | 154 bpm | 7:10 / mi avg | 98 |
| **2026-09-17** | Run | Lactate Threshold Intervals 3x2mi | 14.5 km | 1h 02m | 164 bpm | 6:30 / mi reps | 85 |
| **2026-09-16** | Swim | CSS Threshold Intervals 5x200m | 2.5 km | 45m | 138 bpm | 1:34 / 100m | 52 |

---

## 🔄 How to Refresh Live Data

```bash
# Pull live data from Intervals.icu / Garmin:
python3 scripts/intervals_sync.py

# Push a structured workout to Intervals.icu calendar (syncs to Garmin):
python3 scripts/intervals_sync.py --push-workout "Tuesday Threshold Run" "Warmup
- 15m Z2

Main Set 3x
- 2mi 6:30/mi
- 2m Z1

Cooldown
- 10m Z2"
```
