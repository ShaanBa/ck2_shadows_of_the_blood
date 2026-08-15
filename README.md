# Crusader Kings II: Shadows of the Blood (DLC 1)

> **"The throne is won with blood, but kept in the dark."**

An AGOT-inspired, modular high-intrigue expansion for **Crusader Kings II**.

---

## 🌟 Core Features

* **⚔️ The Generational Feud & Blood Debt Engine:** True multi-generational vendettas, honor duels, slander at royal banquets, and peace marriages.
* **🗡️ The Whispering Web (Leverage & Blackmail):** Infiltrate courts, plant moles, uncover dark secrets, and compel council votes without incurring tyranny.
* **🫅 Shadow Regencies & Puppet Politics:** Control weak, incapable, or child rulers from behind the throne, siphon royal revenues, and survive the sovereign's age-16 reckoning.
* **🕯️ Ancestral Karma & Dynastic Sins:** Sins and virtues of forefathers dynamically alter traits, dread, and trials across generations.

---

## 📂 Repository & Mod Structure

```
├── shadows_of_the_blood.mod              # CK2 Mod Launcher Descriptor
└── shadows_of_the_blood/                 # Mod Root Directory
    ├── common/
    │   ├── traits/                       # Custom traits (Nemesis, Feud Leader, Shadow Regent, Cursed Blood)
    │   ├── opinion_modifiers/            # Deep opinion modifiers
    │   ├── event_modifiers/              # Strategic realm/character modifiers
    │   ├── scripted_triggers/            # Optimized modular triggers
    │   ├── scripted_effects/             # Reusable effects & state management
    │   ├── minor_titles/                 # Shadow Council & Court Infiltrators
    │   ├── cb_types/                     # Blood Feud Casus Belli
    │   └── on_actions/                   # Hooked into executions, successions, feasts, etc.
    ├── decisions/                        # Intrigue decisions, Feud actions, Blackmail hooks
    ├── events/                           # Multi-stage narrative event chains
    └── localisation/                     # Full English CSV localization
```

---

## 🚀 How to Install & Playtest

1. Copy or symlink `shadows_of_the_blood.mod` and the `shadows_of_the_blood/` directory to your local CK2 mod folder:
   `Documents\Paradox Interactive\Crusader Kings II\mod\`
2. Enable **Shadows of the Blood** in the Crusader Kings II launcher under the **Mods** tab.
3. Launch the game and start any campaign!
