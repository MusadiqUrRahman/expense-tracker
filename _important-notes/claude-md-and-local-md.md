# 📜 CLAUDE.md & CLAUDE.local.md — Complete Guide

---

## 🤔 What is CLAUDE.md?

CLAUDE.md is a **special markdown file** that Claude Code reads **automatically**
every time you start a new conversation in your project.

> Think of it as a **instruction manual** you write for Claude.
> "Hey Claude, here are the rules for my project — follow them!"

---

## 📍 Where to Create CLAUDE.md?

You can place it in **3 locations** — each has a different scope:

### 1️⃣ Project Root (Most Common)
```
expense-tracker/CLAUDE.md
```
- ✅ Applies to **this project only**
- ✅ **Shared with team** (committed to git)
- ✅ Everyone on the team sees the same rules

### 2️⃣ Home Directory (Global)
```
~/.claude/CLAUDE.md
```
- ✅ Applies to **ALL your projects**
- ✅ Your **personal** global rules
- 📌 Example: "I prefer simple explanations"

### 3️⃣ Subdirectory (Folder-Specific)
```
expense-tracker/database/CLAUDE.md
```
- ✅ Applies **only when working in that folder**
- ✅ Rarely used, but useful for large projects

---

## ✍️ What to Write Inside CLAUDE.md?

```markdown
# CLAUDE.md

## Project Overview
- This is a Flask app called Spendly
- We use SQLite with raw SQL (no ORM)

## Commands
- Run: python3 app.py
- Test: pytest

## Rules
- All routes go in app.py
- Currency is in rupees (₹)
- Don't add new dependencies without asking
```

### ✅ Good Things to Include:
| What | Example |
|------|---------|
| 🛠️ Setup commands | `source venv/bin/activate` |
| 🏗️ Architecture | "All routes in app.py, no blueprints" |
| 📏 Coding rules | "Use raw SQL, no ORM" |
| ⛔ Things to avoid | "Don't modify CSS file" |
| 🧪 Test commands | `pytest tests/test_file.py` |

### ❌ Don't Include:
- Obvious things ("write clean code")
- Entire file listings (Claude can discover those)
- Sensitive info (API keys, passwords)

---

## 🔒 What is CLAUDE.local.md?

CLAUDE.local.md is the **private/personal version** of CLAUDE.md.

> Think of it as your **personal sticky note** that only YOU can see.
> Your team members will NOT see this file.

---

## 🆚 CLAUDE.md vs CLAUDE.local.md

```
┌──────────────────────────────────────────────────────────┐
│                                                            │
│   📜 CLAUDE.md                                            │
│   ├── 👥 Shared with team (committed to git)              │
│   ├── 📏 Project rules everyone follows                   │
│   ├── 🏗️ Architecture & setup commands                    │
│   └── ✅ Example: "Use raw SQL, no ORM"                   │
│                                                            │
│   🔒 CLAUDE.local.md                                      │
│   ├── 🙋 Personal to YOU (NOT committed to git)           │
│   ├── 🎯 Your personal preferences                        │
│   ├── 🧪 Your debugging shortcuts                         │
│   └── ✅ Example: "Explain things simply, I'm a student"  │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

| Feature | CLAUDE.md | CLAUDE.local.md |
|---------|-----------|-----------------|
| 👀 Who sees it? | **Everyone** (team) | **Only you** |
| 📦 Git committed? | ✅ Yes | ❌ No (add to .gitignore) |
| 📍 Location | Project root | Same folder as CLAUDE.md |
| ✍️ Who writes it? | Team lead / anyone | You personally |
| 🎯 Purpose | Project rules | Personal preferences |

---

## 📂 How They Sit Together

```
expense-tracker/
├── CLAUDE.md              ← 👥 Team rules (in git)
├── CLAUDE.local.md        ← 🔒 Your personal rules (NOT in git)
├── app.py
├── database/
└── ...
```

---

## ✍️ Example: CLAUDE.local.md

```markdown
# My Personal Claude Settings

## About Me
- I'm a student learning Flask for the first time
- I prefer simple explanations with examples

## My Preferences  
- Explain code line by line when I ask
- Use comments in code so I understand
- Don't use advanced Python features I haven't learned

## My Shortcuts
- I test with: pytest -v
- My browser is Chrome at localhost:5001
```

---

## 🔄 Loading Order (How Claude Reads Them)

Claude reads files in this order and **merges all of them** together:

```
Step 1️⃣  →  ~/.claude/CLAUDE.md           (global rules)
Step 2️⃣  →  expense-tracker/CLAUDE.md      (project rules)
Step 3️⃣  →  expense-tracker/CLAUDE.local.md (your personal rules)
Step 4️⃣  →  subfolder/CLAUDE.md            (folder rules, if any)
```

> All rules combine together. If there's a conflict,
> the **more specific file wins** (local > project > global).

---

## ⚡ Quick Comparison Table

| Question | CLAUDE.md | CLAUDE.local.md |
|----------|-----------|-----------------|
| What is it? | Team instruction file | Personal instruction file |
| Who reads it? | Claude Code | Claude Code |
| Shared? | ✅ Yes (git) | ❌ No (private) |
| Required? | ❌ Optional | ❌ Optional |
| Who creates it? | You / team | Only you |
| Auto-created? | ❌ You make it | ❌ You make it |
| Content? | Project rules | Personal preferences |

---

## 💡 Pro Tips

1. ✅ Start with just `CLAUDE.md` — add `CLAUDE.local.md` later when needed
2. ✅ Keep both files **short** — Claude reads them every conversation
3. ✅ Add `CLAUDE.local.md` to your `.gitignore` so it stays private
4. ✅ Update them as your project grows
5. ✅ You can have CLAUDE.md in **multiple folders** — each scopes to that folder

---

## 🇵🇰 اردو میں خلاصہ (Summary in Urdu)

### CLAUDE.md کیا ہے؟
> CLAUDE.md ایک خاص فائل ہے جو آپ اپنے پروجیکٹ میں بناتے ہیں۔
> جب بھی آپ Claude Code کے ساتھ نئی بات چیت شروع کرتے ہیں،
> Claude **خود بخود** اس فائل کو پڑھتا ہے۔
> اس میں آپ اپنے پروجیکٹ کے **قواعد اور ہدایات** لکھتے ہیں۔

### CLAUDE.local.md کیا ہے؟
> یہ CLAUDE.md کا **ذاتی ورژن** ہے۔
> یہ صرف **آپ کے لیے** ہے — آپ کی ٹیم اسے نہیں دیکھ سکتی۔
> اس میں آپ اپنی **ذاتی پسند** لکھتے ہیں۔
> مثال: "میں طالب علم ہوں، آسان الفاظ میں سمجھاؤ"

### فرق:
> - 📜 `CLAUDE.md` = ٹیم کے قواعد (سب دیکھ سکتے ہیں) — git میں جاتی ہے
> - 🔒 `CLAUDE.local.md` = آپ کے ذاتی قواعد (صرف آپ) — git میں نہیں جاتی

### سادہ الفاظ میں:
> CLAUDE.md ایسے ہے جیسے کلاس کے **قواعد** جو بورڈ پر لکھے ہوں (سب کے لیے)۔
> CLAUDE.local.md ایسے ہے جیسے آپ کی **ذاتی ڈائری** میں لکھے ہوئے نوٹس (صرف آپ کے لیے)۔

---
