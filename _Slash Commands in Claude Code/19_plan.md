# 🧭 /plan — Claude Code Command

## ⚠️ Important Note
- `/plan` puts Claude into a **read-only "think-first"** mode
- Claude **cannot edit, create, or delete code** while Plan Mode is active
- Used to **design the approach first**, then execute **only after you approve**

---

## 📌 Purpose
`/plan` is used to **enable Plan Mode** or **view the current session's plan**.

In Plan Mode, Claude **researches the codebase, reads specs, asks clarifying questions, and writes a step-by-step implementation plan** — without touching any production code until you give the green light.

---

## ⚙️ What It Does
- Switches the session into **Plan Mode** (read-only for source code)
- Lets Claude read files, search, and ask questions
- Lets Claude write a plan document to `.claude/plans/`
- **Blocks** edits, new file creation, and destructive shell commands
- Shows the current plan if one already exists in the session

---

## 🚀 Usage
```
/plan
```

Then describe the task, for example:
```
/plan
Read .claude/specs/01-database-setup.md and generate an implementation plan.
Save it to .claude/plans/01-database-setup.md
```

You can also toggle Plan Mode with **`Shift+Tab`** (cycles through modes).

---

## 🧠 How It Works
1. You type `/plan` inside a Claude Code session
2. Claude acknowledges and enters **read-only mode**
3. Claude **explores** the codebase: reads specs, greps patterns, opens related files
4. Claude may **ask clarifying questions** (e.g. "which filename should the DB use?")
5. Claude **drafts a plan** — files to change, functions to add, verification steps
6. Plan is **saved** to `.claude/plans/<step-name>.md`
7. You **review** → accept, tweak, or reject
8. On approval, Claude **exits Plan Mode** and implements the plan

---

## 🔄 The Plan Mode Lifecycle

```
   ┌─────────────┐
   │  1. ENTER   │  user runs /plan
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │ 2. EXPLORE  │  read specs, grep code, ask questions
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │  3. DESIGN  │  draft step-by-step approach
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │ 4. PERSIST  │  save to .claude/plans/<step>.md
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │ 5. APPROVE  │  human reviews & accepts
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │ 6. EXECUTE  │  Claude switches to write-mode
   └─────────────┘
```

---

## ✅ What You CAN Do in Plan Mode

| Tool / Action | Allowed? |
|---|---|
| 📖 `Read` files | ✅ Yes |
| 🔍 `Grep` / `Glob` search | ✅ Yes |
| 💻 `Bash` read-only commands (`ls`, `git log`, `SELECT …`) | ✅ Yes |
| 🌐 `WebFetch` / `WebSearch` | ✅ Yes |
| ❓ `AskUserQuestion` | ✅ Yes |
| 📝 Write the plan doc itself | ✅ Yes |

## ❌ What You CANNOT Do in Plan Mode

| Tool / Action | Blocked? |
|---|---|
| ✏️ `Edit` source files | ❌ Blocked |
| 📄 `Write` new source files | ❌ Blocked |
| 🗑️ Destructive `Bash` (`rm`, installs, migrations) | ❌ Blocked |
| 🚀 Git push / commit | ❌ Blocked |

---

## 📂 Where Are Plans Stored?

### Project Path:
```
<project-root>/.claude/plans/
```

### Your Actual Path:
```
/mnt/c/Users/win10/Desktop/Claude-Code-Course/expense-tracker/.claude/plans/
```

### Typical File Layout:
```
.claude/
├── specs/                         ← 📋 Instructor-provided specs
│   └── 01-database-setup.md
└── plans/                         ← 📝 Claude-generated plans
    └── 01-database-setup.md
```

Plans are **plain markdown** — commit them to git if you want a durable paper trail.

---

## 🎯 When to Use `/plan`

Use it when **any** of these apply:

- 🏗️ Task touches **multiple files** or multiple layers
- 🧩 There are **architectural choices** (schema, auth, structure)
- 📚 The feature has a **spec** to digest carefully
- 🎓 Course projects where each step needs **instructor-style review**
- 🔐 Large blast radius — DB migrations, refactors, deletions
- 🤷 You're **not sure** what Claude will do and want to see it first

## 🚫 When to Skip `/plan`

| Don't use for | Why |
|---|---|
| 🐛 One-line bug fixes | Overhead > benefit |
| ✏️ Typos / renames | Trivial, obvious |
| ❓ Pure Q&A | Nothing to build |
| 📜 Fully specified tasks | Plan would just restate the spec |

---

## 💎 Why Plan Mode is Valuable

| Problem without a plan | How Plan Mode fixes it |
|---|---|
| 🏃 AI dives into edits before reading the code | Forces a **research pass** first |
| 🌪️ Large tasks → sprawling off-target diffs | You review approach **before** any code |
| 🤐 Architectural choices locked in silently | Trade-offs surface in **plain English** |
| 🔥 Dead-end attempts waste tokens | Dead ends caught in **prose, not code** |
| 📜 No paper trail for decisions | `.claude/plans/` = durable docs |

---

## 🎮 3 Ways to Enter Plan Mode

### Way 1: `/plan` Command
```
/plan
```
Cleanest — explicit and logged in chat.

### Way 2: `Shift+Tab` Shortcut
Cycles through modes: normal → plan → normal.

### Way 3: Ask Claude
```
"Before you touch any code, plan this out first."
```
Claude will mimic Plan Mode behavior even without the toggle.

---

## 🔄 Plan vs Spec vs Task

```
┌────────────────────────────────────────────────┐
│                                                  │
│  📋 Specs (.claude/specs/)                      │
│  ├── YOU / instructor write them                │
│  ├── Define WHAT to build                       │
│  ├── Committed to git                           │
│  └── "The blueprint request"                    │
│                                                  │
│  📝 Plans (.claude/plans/)                      │
│  ├── Claude writes them in Plan Mode            │
│  ├── Define HOW to build it                     │
│  ├── Reviewed and approved by you               │
│  └── "The architect's drawing"                  │
│                                                  │
│  ✅ Tasks (TaskCreate)                          │
│  ├── Claude uses them during execution          │
│  ├── Track step-by-step progress                │
│  ├── Session-scoped, not persistent             │
│  └── "The builder's checklist"                  │
│                                                  │
└────────────────────────────────────────────────┘
```

---

## ❓ Common Questions

| Q | A |
|---|---|
| 🤔 Does Plan Mode work for small fixes? | Yes, but it's overkill. Skip it for typos. |
| 🤔 Can I edit the plan myself? | Yes — it's just markdown in `.claude/plans/`. |
| 🤔 Does the plan persist across sessions? | Yes — the file survives until deleted. |
| 🤔 Can Claude skip Plan Mode if I approve mid-exploration? | Yes — Claude calls `ExitPlanMode` when ready. |
| 🤔 Does Plan Mode block *all* Bash? | No — only destructive/write commands. Read-only is fine. |

---

## 💡 Pro Tips

1. ✅ **Point Claude at the spec** — "Read `.claude/specs/01-xxx.md` then plan" works best
2. ✅ **Name the plan output path** — ensures it lands in `.claude/plans/`
3. ✅ **Review the plan carefully** — this is your last cheap checkpoint
4. ✅ **Use it with course steps** — every step in Spendly has spec + plan + code
5. ✅ **Combine with `AskUserQuestion`** — Claude will ask clarifying questions in Plan Mode
6. ✅ **Don't skip for DB / auth / refactor work** — the blast radius is too large

---

## 📚 Summary
`/plan` = Read-only "think-first" mode. Claude designs the approach, you approve, *then* it codes.

> **First plan → then approval → then execute.**

---

## 🇵🇰 اردو خلاصہ

### `/plan` کیا ہے؟
> یہ کمانڈ Claude Code کو **"صرف پڑھنے والا" (read-only) موڈ** میں ڈالتی ہے۔
> اس موڈ میں Claude پہلے **سوچتا ہے، تحقیق کرتا ہے، اور منصوبہ بناتا ہے** — کوڈ میں کوئی تبدیلی نہیں کرتا۔
> جب آپ منصوبہ منظور کر لیتے ہیں، تب جا کر Claude اصل کوڈ لکھتا ہے۔

### کیوں ضروری ہے؟
> - بڑے یا پیچیدہ کاموں میں سیدھا کوڈ لکھنا **غلط سمت** لے جا سکتا ہے۔
> - Plan Mode پہلے **spec پڑھتا ہے، فائلیں جانچتا ہے، سوالات پوچھتا ہے**۔
> - پھر ایک **مرحلہ وار منصوبہ** `.claude/plans/` میں محفوظ کرتا ہے۔
> - آپ منصوبہ دیکھ کر **قبول، ترمیم، یا رد** کر سکتے ہیں۔

### کیسے استعمال کریں؟
> 1. چیٹ میں `/plan` لکھیں، یا `Shift+Tab` دبائیں
> 2. کام کی تفصیل بتائیں (مثلاً: "spec پڑھ کر منصوبہ بناؤ")
> 3. Claude منصوبہ `.claude/plans/` میں محفوظ کرے گا
> 4. آپ منظوری دیں → Claude کوڈ لکھنا شروع کرے گا

### ✅ کن کاموں میں استعمال کریں؟
> - 🏗️ **بڑے features** جو کئی فائلیں بدلیں
> - 🧩 **Architectural فیصلے** (schema، auth، structure)
> - 🎓 **Course projects** جہاں ہر step کی نظرثانی ضروری ہے
> - 🔐 **خطرناک کام** (DB migration، refactor، deletion)

### 🚫 کن کاموں میں نہ کریں؟
> - 🐛 معمولی bug fix یا typo
> - ❓ صرف سوال جواب
> - 📜 ایسے کام جہاں spec پہلے سے ہر تفصیل طے کر چکا ہو

### سنہری اصول:
> **پہلے منصوبہ → پھر منظوری → پھر عمل۔**
> کوڈ میں ہاتھ ڈالنے سے پہلے، **بلیو پرنٹ پر دستخط لازمی ہیں**۔

### سادہ الفاظ میں:
> `/plan` Claude کو کہتا ہے: **"پہلے سوچو، پھر لکھو۔"**
> یہ ایک **چیک پوائنٹ** ہے — AI کا کام شروع ہونے سے پہلے۔
