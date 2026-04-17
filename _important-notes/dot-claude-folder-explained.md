# 📂 .claude Folder Structure — Explained

---

## 🤔 What is the `.claude` folder?

The `.claude` folder is a **hidden folder** that Claude Code creates automatically.
It stores Claude's **internal data** — like its brain, memory, and plans.

> Think of it like a **diary** that Claude keeps for itself to remember things
> about your project and how you like to work.

---

## 📍 Where does it exist?

It can exist in **two places**:

### 1️⃣ Inside your Home Directory (Global)
```
~/.claude/
```
- This is your **personal** `.claude` folder
- It applies to **ALL your projects**
- Stores your global settings and memory

### 2️⃣ Inside your Project (Project-level)
```
expense-tracker/.claude/
```
- This is **project-specific**
- Only applies to **this one project**
- Stores plans and project-related data

---

## 🏗️ What's Inside? (Full Structure)

```
~/.claude/                          ← 🏠 Home (Global)
│
├── CLAUDE.md                       ← 📜 Global instructions for ALL projects
│
├── settings.json                   ← ⚙️ Your personal Claude Code settings
│
├── projects/                       ← 📁 Per-project memory storage
│   └── <project-name>/
│       └── memory/
│           ├── MEMORY.md           ← 📋 Index of all memories
│           └── user_role.md        ← 🧠 Individual memory files
│           └── feedback_testing.md
│           └── project_info.md
│
└── credentials/                    ← 🔑 Auth tokens (auto-managed)


expense-tracker/.claude/            ← 📂 Project-level
│
├── plans/                          ← 📝 Implementation plans Claude creates
│   └── some-plan.md
│
└── settings.json                   ← ⚙️ Project-specific settings
```

---

## 🧩 Each Part Explained

### 📜 `CLAUDE.md` (inside `~/.claude/`)
- **What:** Global rules for Claude across all projects
- **Example:** "I prefer English responses" or "Always use tabs"
- **Who writes it:** YOU write it

### ⚙️ `settings.json`
- **What:** Configuration for Claude Code behavior
- **Example:** Permission settings, model preferences
- **Who writes it:** Claude Code manages it (you can edit too)

### 🧠 `memory/` folder
- **What:** Claude's memory system — remembers things across conversations
- **Example:** "User is a student", "User prefers simple explanations"
- **Who writes it:** CLAUDE writes it automatically
- **Contains:**
  - `MEMORY.md` → Index file (list of all memories)
  - Individual `.md` files → One file per memory topic

### 📝 `plans/` folder
- **What:** Step-by-step implementation plans Claude creates
- **Example:** "Plan to build login system" with detailed steps
- **Who writes it:** CLAUDE writes when planning a big task
- **Temporary** — plans are for current work, not permanent

---

## ❓ Why Does It Exist?

| Reason | Explanation |
|--------|-------------|
| 🧠 **Memory** | So Claude remembers you across conversations |
| 📝 **Planning** | So Claude can plan big tasks step by step |
| ⚙️ **Settings** | So your preferences are saved |
| 🔄 **Continuity** | So you don't repeat yourself every time |

---

## ⚡ Key Differences to Remember

```
┌─────────────────────────────────────────────────┐
│                                                   │
│   CLAUDE.md  →  YOU write it (your rules)        │
│   .claude/   →  CLAUDE creates it (its brain)    │
│                                                   │
│   CLAUDE.md  →  Instructions for Claude          │
│   .claude/   →  Claude's internal storage        │
│                                                   │
│   CLAUDE.md  →  Commit to git ✅ (share with team)│
│   .claude/   →  Don't commit ❌ (personal data)   │
│                                                   │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Simple Summary

> The `.claude` folder is like **Claude's personal notebook**.
> It keeps memories, plans, and settings inside it.
> You don't need to touch it — Claude manages it on its own.
> Just know it exists and let Claude do its thing! ✨

---

## 💡 Pro Tips

1. ✅ The `.claude/plans/` folder is already in `.gitignore` — good!
2. ✅ You never need to manually create the `.claude` folder
3. ✅ Claude creates it automatically when needed
4. ✅ If you delete it, Claude will recreate it — no worries!
5. ✅ Memory files help Claude give you better answers over time
