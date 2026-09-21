# ⚡ Endurance Blueprint

A modular, version-controlled training framework designed for hybrid endurance athletes balancing **running performance**, **cycling volume**, and **stacked calisthenics strength**.

---

## 📁 Repository Structure

```text
.
├── README.md
├── current-block.md               <-- Link or copy of your active schedule
├── benchmarks.md                  <-- Pace charts, HR zones, target splits
└── blocks/
    ├── 2026-q4-sub130-hm.md       <-- Master Weekly Schedule file
    ├── 2027-q2-danube-bike.md
    └── template.md
```

---

## 🧭 Overview & File Guide

| File | Purpose |
| :--- | :--- |
| [**`current-block.md`**](current-block.md) | Symlink or copy pointing to your active weekly training schedule. Open this for daily execution. |
| [**`benchmarks.md`**](benchmarks.md) | Single source of truth for target race splits (Sub-1:30 HM, Sub-40 10K, Sub-20 5K), 5-zone HR models, cycling power/cadence, fueling rules, and calisthenics baselines. |
| [**`blocks/2026-q4-sub130-hm.md`**](blocks/2026-q4-sub130-hm.md) | Active Master Weekly Schedule for the Sub-1:30 Half Marathon block combining threshold/speedwork with aerobic road cycling. |
| [**`blocks/2027-q2-danube-bike.md`**](blocks/2027-q2-danube-bike.md) | Master Weekly Schedule for the Danube Cycle Path (Donauradweg) multi-day bikepacking and high-volume touring block. |
| [**`blocks/template.md`**](blocks/template.md) | Reusable template for planning and spinning up new training blocks. |

---

## 🧱 The Hybrid Training Philosophy

1. **Polarized & Threshold Conditioning**
   * ~80% of cardio volume is strictly low-intensity Zone 2 (aerobic base, mitochondrial density, fat oxidation).
   * ~20% is dedicated to targeted lactate threshold (Zone 4) and V̇O₂ max (Zone 5) stimulus.
2. **Cardio Synergy (Run + Bike)**
   * Cycling provides substantial cardiovascular and metabolic training volume with zero eccentric impact, safeguarding joints and connective tissues while sharpening aerobic capacity.
3. **Stacked Calisthenics ("Keep Hard Days Hard")**
   * Resistance training is stacked directly after cardio sessions rather than on separate days. This consolidates neuromuscular fatigue into dedicated training windows and leaves recovery days (like Monday) truly restorative.
4. **Postural & Structural Integrity**
   * Focuses on vertical and horizontal pulling, anterior/posterior chain resilience, and ankle/tibialis durability to counteract repetitive motion fatigue and avoid overuse injuries.

---

## 🚀 Workflow: Switching or Creating Blocks

### 1. Activating an Existing Block
To switch your active training block, update the `current-block.md` symlink (or copy the file):

```bash
# Point to the Sub-1:30 HM Block:
ln -sf blocks/2026-q4-sub130-hm.md current-block.md

# Or point to the Danube Bikepacking Block:
ln -sf blocks/2027-q2-danube-bike.md current-block.md
```

### 2. Creating a New Block from Template
When preparing for a new season or target race:

```bash
# 1. Duplicate the template
cp blocks/template.md blocks/YYYY-qX-block-name.md

# 2. Edit the schedule and workout details in the new file

# 3. Activate the new block
ln -sf blocks/YYYY-qX-block-name.md current-block.md
```
