# ⚡ Endurance Blueprint

A modular, version-controlled training framework designed for hybrid endurance athletes balancing **running performance**, **cycling volume**, **swimming endurance**, and **stacked calisthenics strength**.

> ### 📍 Active Training Block: [Sub-1:30 Half Marathon (Q4 2026)](blocks/2026-q4-sub130-hm.md)
> * **Current Goal:** Build lactate threshold speed ($3 \times 2\text{ mi}$ @ 6:25–6:35/mi) & road cycling aerobic base.
> * **Weekly Rhythm:** 4 Runs · 2 Rides · 3 Stacked Calisthenics Sessions · 1 Rest Day.
> 
> 🚀 **[Open Master Weekly Schedule](blocks/2026-q4-sub130-hm.md)** · 📊 **[Live Fitness Dashboard](fitness-dashboard.md)** · 🎯 **[Target Splits & Benchmarks](benchmarks.md)** · 🎒 **[Race Readiness](race-readiness.md)**

---

## 📁 Repository Structure

```text
.
├── README.md                          <-- Repo homepage & Active Block Banner
├── benchmarks.md                      <-- Pace charts, HR zones, target splits, swim CSS
├── fitness-dashboard.md               <-- Live CTL/ATL/TSB metrics & race countdowns
├── race-readiness.md                  <-- Gear checklist, transition bags (T1/T2) & race tactics
├── blocks/
│   ├── 2026-q4-sub130-hm.md           <-- Sub-1:30 Half Marathon Master Schedule
│   ├── 2027-q1-oceanside-703.md       <-- Sub-5:00 IRONMAN 70.3 Oceanside (April 3, 2027)
│   ├── 2027-q2-escape-alcatraz.md       <-- Escape From Alcatraz Triathlon (June 6, 2027)
│   ├── 2027-q3-ironman-california.md  <-- Sub-10:00 IRONMAN California (October 18, 2027)
│   ├── 2027-q4-sub3-marathon.md       <-- Sub-3:00 Marathon Block (Late 2027 PR / CIM)
│   └── template.md                    <-- Master reusable schedule template
├── logs/
│   └── template-weekly-log.md         <-- Weekly execution & wellness tracker
└── scripts/
    ├── README.md                      <-- Intervals.icu Open API & Garmin sync guide
    └── intervals_sync.py              <-- Intervals.icu & Garmin fitness sync engine
```

---

## 🧭 Overview & File Guide

| File | Goal Event / Purpose | Key Highlights |
| :--- | :--- | :--- |
| [**`fitness-dashboard.md`**](fitness-dashboard.md) | Live Training Dashboard | Live tracking of Fitness (CTL), Fatigue (ATL), Form (TSB), resting metrics, race countdowns, and recent workouts. |
| [**`race-readiness.md`**](race-readiness.md) | Race Week & Gear Packing | Comprehensive transition bag checklist (Morning clothes, T1 Bike, T2 Run, Special Needs), taper timeline, and course tactical plans. |
| [**`benchmarks.md`**](benchmarks.md) | Central Benchmark Truth | Target splits (Sub-1:30 HM, Sub-5:00 70.3, Sub-10:00 Ironman, Sub-3:00 Marathon), 5-zone HR models, CSS swim zones, cycling FTP, fueling & strength standards. |
| [**`blocks/2026-q4-sub130-hm.md`**](blocks/2026-q4-sub130-hm.md) | Sub-1:30 Half Marathon | Lactate threshold intervals ($3 \times 2\text{ mi}$), V̇O₂ max track repeats, long base rides, stacked leg & posterior calisthenics. |
| [**`blocks/2027-q1-oceanside-703.md`**](blocks/2027-q1-oceanside-703.md) | Sub-5:00 IRONMAN 70.3 Oceanside *(April 3, 2027)* | Harbor swim CSS intervals, Camp Pendleton rolling hill surges (San Mateo grade), Saturday aero long rides + brick runs off the bike, swim propulsion calisthenics. |
| [**`blocks/2027-q2-escape-alcatraz.md`**](blocks/2027-q2-escape-alcatraz.md) | Escape From Alcatraz Triathlon *(June 6, 2027)* | 1.5 mi open-water bay swim (Alcatraz island current), 18 mi hilly bike through the Presidio & Golden Gate Park, 8 mi waterfront run; sprint-race pace sharpening & transition speed. |
| [**`blocks/2027-q3-ironman-california.md`**](blocks/2027-q3-ironman-california.md) | Sub-10:00 IRONMAN California *(October 18, 2027)* | 4,000m continuous river swim rhythm, 112-mile non-coasting delta aero rides, brick runs, neck extensor durability ("Shermer's Neck" prevention), high-intake gut training ($80\text{--}95\text{g}$ carbs/hr). |
| [**`blocks/2027-q4-sub3-marathon.md`**](blocks/2027-q4-sub3-marathon.md) | Sub-3:00 Marathon *(Late 2027 PR / CIM)* | Converting peak Ironman aerobic engine to 6:49/mi marathon velocity, cruise intervals ($3 \times 2.5\text{ mi}$), 18–22 mile progressive long runs, eccentric hamstring durability. |
| [**`blocks/template.md`**](blocks/template.md) | Training Block Template | Modular starting point for planning any future endurance or hybrid block. |
| [**`logs/template-weekly-log.md`**](logs/template-weekly-log.md) | Weekly Log Template | Track planned vs actual TSS, volume per discipline, RPE, sleep quality, and calisthenics adherence. |
| [**`scripts/intervals_sync.py`**](scripts/intervals_sync.py) | Intervals.icu / Garmin Bridge | Zero-dependency Python script to pull live metrics from Intervals.icu and render `fitness-dashboard.md`. |
| [**`scripts/README.md`**](scripts/README.md) | Open API Documentation | Complete guide on Intervals.icu OpenAPI endpoints, Swagger links, and workout builder syntax. |

---

## 🗓️ 2026–2027 Athletic Roadmap

```text
[Q4 2026] ──> Sub-1:30 Half Marathon (Building threshold speed & running mechanics)
      │
[Q1 2027] ──> Sub-5:00 IRONMAN 70.3 Oceanside (April 3, 2027 - Harbor swim + Pendleton hills + brick runs)
      │
[Q2 2027] ──> Escape From Alcatraz Triathlon (June 6, 2027 – Sprint-triathlon: 1.5 mi swim / 18 mi bike / 8 mi run)
      │
[Q2–Q3 2027] ──> Sub-10:00 IRONMAN California (October 18, 2027 - 140.6 full-distance peak aero & marathon build)
      │
[Q4 2027] ──> Sub-3:00 Marathon Block (Late Fall / CIM Dec 2027 - Converting Ironman diesel engine to 6:49/mi marathon pace)
```

---

## 🔌 Integrations: Intervals.icu & Garmin Sync

This repository includes a direct integration with **[Intervals.icu Open API](https://www.intervals.icu/features/open-api/)** (which automatically aggregates activities from Garmin Connect, Wahoo, Strava, and Zwift).

### Quickstart
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Add your **Intervals.icu API Key** (from Intervals.icu $\to$ **Settings** $\to$ **Developer Settings**). You can leave `INTERVALS_ATHLETE_ID=0` (0 represents your authenticated user).
3. Run the sync tool to update [**`fitness-dashboard.md`**](fitness-dashboard.md):
   ```bash
   python3 scripts/intervals_sync.py
   ```
4. Push structured workouts straight to your Garmin watch or bike computer:
   ```bash
   python3 scripts/intervals_sync.py --push-workout "Tuesday Threshold" "Warmup\n- 15m Z2\n\nMain Set 3x\n- 2mi 6:30/mi\n- 2m Z1\n\nCooldown\n- 10m Z2"
   ```

### Automated GitHub Actions Sync
A pre-configured GitHub Actions workflow (`.github/workflows/intervals-sync.yml`) runs automatically every Monday at 06:00 UTC (or manually via `workflow_dispatch`).
* Add repository secrets `INTERVALS_ATHLETE_ID` and `INTERVALS_API_KEY` in **GitHub $\to$ Settings $\to$ Secrets and variables $\to$ Actions**.

---

## 🧱 The Hybrid Training Philosophy

1. **Polarized & Threshold Conditioning**
   * ~80% of cardio volume is strictly low-intensity Zone 2 (aerobic base, mitochondrial density, fat oxidation).
   * ~20% is dedicated to targeted lactate threshold (Zone 4) and V̇O₂ max (Zone 5) stimulus.
2. **Cardio Synergy (Swim + Bike + Run)**
   * Cycling and swimming provide massive aerobic volume and lung capacity with minimal orthopedic impact, allowing weekly training volume to exceed 12–16+ hours while keeping running legs resilient and injury-free.
3. **Stacked Calisthenics ("Keep Hard Days Hard")**
   * Resistance training is stacked directly after cardio sessions rather than on separate days. This consolidates neuromuscular fatigue into dedicated training windows and leaves recovery days (like Monday) truly restorative.
4. **Postural & Structural Integrity**
   * Focuses on vertical and horizontal pulling, anterior/posterior chain resilience, and neck/scapular durability to counteract prolonged aero positions and maintain upright running posture under extreme fatigue.

---

## 🚀 Workflow: Switching or Creating Blocks

### 1. Activating a Block
Each training block lives in **one single canonical file** inside `blocks/`. To switch your active training block:
* Simply update the **📍 Active Training Block** link at the top of this `README.md`.
* Every change made to a block schedule is immediately preserved without file duplication or desync issues.

### 2. Creating a New Block from Template
When preparing for a new season or target race:
```bash
# 1. Duplicate the template
cp blocks/template.md blocks/YYYY-qX-block-name.md

# 2. Edit the schedule and workout details in the new file

# 3. Update the Active Block link at the top of README.md
```
