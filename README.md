# ⚡ Endurance Blueprint

A modular, version-controlled training framework designed for hybrid endurance athletes balancing **running performance**, **cycling volume**, **swimming endurance**, and **stacked calisthenics strength**.

---

## 📁 Repository Structure

```text
.
├── README.md
├── current-block.md                   <-- Active weekly schedule (copy or symlink)
├── benchmarks.md                      <-- Pace charts, HR zones, target splits, swim CSS
└── blocks/
    ├── 2026-q4-sub130-hm.md           <-- Sub-1:30 Half Marathon Master Schedule
    ├── 2027-q1-oceanside-703.md       <-- IRONMAN 70.3 Oceanside (April 3, 2027)
    ├── 2027-q2-danube-bike.md         <-- Danube Cycle Path Bikepacking / Touring
    ├── 2027-q3-ironman-california.md  <-- IRONMAN California (October 18, 2027)
    └── template.md                    <-- Master reusable schedule template
```

---

## 🧭 Overview & File Guide

| File | Goal Event / Purpose | Key Highlights |
| :--- | :--- | :--- |
| [**`current-block.md`**](current-block.md) | Active Daily Execution | Active weekly schedule for daily reference. |
| [**`benchmarks.md`**](benchmarks.md) | Central Benchmark Truth | Target splits (Sub-1:30 HM, 70.3 Oceanside, IRONMAN California), 5-zone HR models, CSS swim zones, cycling FTP, fueling & strength standards. |
| [**`blocks/2026-q4-sub130-hm.md`**](blocks/2026-q4-sub130-hm.md) | Sub-1:30 Half Marathon | Lactate threshold intervals ($3 \times 2\text{ mi}$), V̇O₂ max track repeats, long base rides, stacked leg & posterior calisthenics. |
| [**`blocks/2027-q1-oceanside-703.md`**](blocks/2027-q1-oceanside-703.md) | IRONMAN 70.3 Oceanside *(April 3, 2027)* | Harbor swim CSS intervals, Camp Pendleton rolling hill surges, Saturday aero long rides + brick runs off the bike, swim propulsion calisthenics. |
| [**`blocks/2027-q2-danube-bike.md`**](blocks/2027-q2-danube-bike.md) | Danube Cycle Path Bikepacking | Back-to-back loaded endurance rides (80–120 km), saddle fatigue resilience, scapular anti-slouch calisthenics, running maintenance. |
| [**`blocks/2027-q3-ironman-california.md`**](blocks/2027-q3-ironman-california.md) | IRONMAN California *(October 18, 2027)* | 4,000m continuous river swim rhythm, 112-mile non-coasting delta aero rides, brick runs, neck extensor durability ("Shermer's Neck" prevention), high-intake gut training ($80\text{--}95\text{g}$ carbs/hr). |
| [**`blocks/template.md`**](blocks/template.md) | Training Block Template | Modular starting point for planning any future endurance or hybrid block. |

---

## 🗓️ 2026–2027 Athletic Roadmap

```text
[Q4 2026] ──> Sub-1:30 Half Marathon Block (Running threshold speed + road bike aerobic base)
      │
[Q1 2027] ──> IRONMAN 70.3 Oceanside (April 3, 2027 - Harbor swim + Pendleton hills + brick runs)
      │
[Q2 2027] ──> Danube Cycle Path Tour (May/June 2027 - High-volume loaded touring & fat oxidation)
      │
[Q3 2027] ──> IRONMAN California (October 18, 2027 - 140.6 full-distance peak aero & marathon build)
```

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

### 1. Activating an Existing Block
To switch your active training block, update `current-block.md` with a copy (recommended for GitHub web viewing) or symlink:

```bash
# Point to 70.3 Oceanside:
cp blocks/2027-q1-oceanside-703.md current-block.md

# Point to IRONMAN California:
cp blocks/2027-q3-ironman-california.md current-block.md

# Or use relative symlinks:
ln -sf blocks/2027-q1-oceanside-703.md current-block.md
```

### 2. Creating a New Block from Template
When preparing for a new season or target race:

```bash
# 1. Duplicate the template
cp blocks/template.md blocks/YYYY-qX-block-name.md

# 2. Edit the schedule and workout details in the new file

# 3. Activate the new block
cp blocks/YYYY-qX-block-name.md current-block.md
```
