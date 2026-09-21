# 🔌 Intervals.icu Open API & Garmin Sync Guide

This directory contains automation tooling connecting **Endurance Blueprint** with **[Intervals.icu](https://www.intervals.icu/features/open-api/)**, which acts as a two-way synchronization bridge for Garmin Connect, Wahoo, Strava, and Zwift.

---

## 📖 Official OpenAPI Documentation References

* **Open API Feature Guide:** [https://www.intervals.icu/features/open-api/](https://www.intervals.icu/features/open-api/)
* **Interactive Swagger UI:** [https://intervals.icu/api/v1/docs/swagger-ui/index.html](https://intervals.icu/api/v1/docs/swagger-ui/index.html)
* **Community API Forum:** [https://forum.intervals.icu/t/api-access-to-intervals-icu/225](https://forum.intervals.icu/t/api-access-to-intervals-icu/225)

---

## 🔑 Authentication & Athlete ID

Intervals.icu supports HTTP Basic Authentication for personal API usage:

* **Username:** `API_KEY` (literal string)
* **Password:** Your personal API key, generated at:
  > **Intervals.icu $\to$ Settings $\to$ Developer Settings $\to$ API Keys**
* **Athlete ID:** You can use `0` as the Athlete ID to refer to the authenticated user.

---

## 📡 Endpoints Implemented

| Endpoint | Method | Purpose in Blueprint |
| :--- | :--- | :--- |
| `/api/v1/athlete/{id}` | `GET` | Fetches athlete profile, current FTP, LTHR, and Max HR. |
| `/api/v1/athlete/{id}/wellness` | `GET` | Fetches daily Fitness (CTL), Fatigue (ATL), Form (TSB), Ramp Rate, Resting HR, HRV, and Sleep metrics. |
| `/api/v1/athlete/{id}/activities` | `GET` | Pulls completed activities automatically uploaded by Garmin Connect (distance, moving time, normalized power, avg HR, TSS load). |
| `/api/v1/athlete/{id}/events` | `POST` | Uploads structured text workouts to your calendar, which Intervals.icu automatically pushes to your Garmin device! |

---

## 🚀 CLI Usage

### 1. Configure Credentials
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Edit `.env`:
```env
INTERVALS_ATHLETE_ID=0
INTERVALS_API_KEY=your_intervals_api_key
```

### 2. Pull Live Fitness & Activity Metrics
Generates or updates [`fitness-dashboard.md`](../fitness-dashboard.md):
```bash
python3 scripts/intervals_sync.py
```

### 3. Push a Structured Workout to Garmin
Intervals.icu features an automated text workout parser that compiles Markdown text into step-by-step Garmin workouts:

```bash
python3 scripts/intervals_sync.py --push-workout "Tuesday Threshold Run" \
"Warmup
- 15m Z2 175spm

Main Set 3x
- 2mi 6:30/mi
- 2m Z1 jog

Cooldown
- 10m Z2" \
--sport Run \
--date 2026-09-22T06:00:00
```

---

## 📝 Intervals.icu Workout Text Format Quick Reference

The workout builder recognizes human-readable training syntax:

* **Duration:** `h`, `m`, `s` (e.g., `1h`, `15m`, `45s`)
* **Distance:** `km`, `mi`, `mtr` (e.g., `2mi`, `1km`, `400mtr`)
* **Targets:**
  * Pace: `6:30/mi`, `4:15/km`, or `% pace`
  * Power: Watts (e.g., `210W`) or `% FTP` (e.g., `85%`)
  * Zones: `Z1`, `Z2`, `Z3`, `Z4`, `Z5`
  * Cadence: `90rpm`, `180spm`
* **Repeats:** `Nx` on the section line (e.g., `Main Set 4x` or `5x`)
