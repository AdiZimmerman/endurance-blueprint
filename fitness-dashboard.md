# 📊 Endurance Blueprint: Fitness & Readiness Dashboard

> [!NOTE]
> *Currently displaying demo / placeholder data. Configure `.env` with your Intervals.icu API Key to stream live Garmin/Intervals data.*

*Last Updated: 2026-09-21 11:16:33 UTC*

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

| Metric | Value | Description & Purpose |
| :--- | :--- | :--- |
| **Fitness (CTL)** | **78.5** | Chronic Training Load (~42-day rolling exponential weighted average). Represents total aerobic engine. |
| **Fatigue (ATL)** | **84.2** | Acute Training Load (~7-day rolling weighted average). Represents recent training fatigue. |
| **Form (TSB)** | **-5.7** | Training Stress Balance ($CTL - ATL$). Indicates readiness to race or train hard. |
| **Ramp Rate** | **+4.1 / wk** | Weekly change in CTL. Ideal range: $+3$ to $+7$ per week to prevent overtraining. |
| **Resting HR** | **44** bpm | Lower baseline indicates strong parasympathetic tone and recovery. |
| **HRV (RMSSD)** | **68** ms | Heart Rate Variability baseline metric. |
| **Current Weight** | **72.5** kg | Monitored for power-to-weight and hydration tracking. |

### 🧭 Current Status Interpretation
> 🟡 **Productive Training Zone** (Optimal adaptation & fitness build)

---

## 🏃🚴🏊 Recent Activity Log (Garmin / Intervals.icu)

| Date | Sport | Title | Distance | Duration | Avg HR | Power / Pace | Load / TSS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-09-20** | Ride | Saturday Long Road Aerobic Ride | 82.4 km | 3h 05m | 134 bpm | 195 W (Zone 2) | 142 |
| **2026-09-19** | Run | Quality Long Run with Fast Finish | 19.3 km | 1h 26m | 154 bpm | 7:10 / mi avg | 98 |
| **2026-09-17** | Run | Lactate Threshold Intervals 3x2mi | 14.5 km | 1h 02m | 164 bpm | 6:30 / mi reps | 85 |
| **2026-09-16** | Swim | CSS Threshold Intervals 5x200m | 2.5 km | 45m | 138 bpm | 1:34 / 100m | 52 |

---

## 🔄 How to Refresh Live Data

To refresh this dashboard with live data from your Garmin / Intervals.icu account:

```bash
# 1. Ensure your .env has INTERVALS_ATHLETE_ID and INTERVALS_API_KEY
# 2. Run the sync script:
python3 scripts/intervals_sync.py
```
