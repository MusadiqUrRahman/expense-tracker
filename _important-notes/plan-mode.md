# 🧭 Plan Mode in Claude Code

---

## 🎬 Introduction: Why Plan Before Code?

When you ask an AI coding assistant to build something non-trivial, two things can happen:

### ⚡ Straight-to-Code (The Risky Way)
> "Hey Claude, set up the database" → AI instantly starts writing files

Feels fast. But the AI may misread the spec, pick the wrong schema, touch files you didn't want touched, and by the time you notice, the damage is already in your diff.

### 🧭 Plan-First (The Safe Way)
> "Hey Claude, **/plan** — set up the database" → AI researches, asks questions, writes a plan, waits for approval

You see the *blueprint* before a single line of production code is written. You accept, tweak, or reject. **Only after approval** does Claude start editing.

**The key difference:** Straight-to-code trusts the AI's first instinct. Plan Mode makes the AI **prove it understood** before touching your codebase.

---

## 🤔 What is Plan Mode?

Plan Mode is a **read-only, think-first** operating mode built into Claude Code.

When Plan Mode is active:
- ✅ Claude **can** read files, search the codebase, run safe commands, ask questions
- ✅ Claude **can** write a plan document to `.claude/plans/`
- ❌ Claude **cannot** edit source files
- ❌ Claude **cannot** create new code files
- ❌ Claude **cannot** run destructive shell commands

Think of it as **"pencil-and-paper mode"** — Claude sketches the approach, you sign off, and *then* the real work starts.

### 🔑 The core idea
> **First plan → then approval → then execute.**
> No code changes until the human gives a green light.

---

## 🚦 How to Enter & Exit Plan Mode

| Action | How |
| --- | --- |
| ▶️ Enter Plan Mode | Run `/plan` in chat, **or** press `Shift+Tab` to cycle modes |
| 💾 Save the plan | Claude writes it to `.claude/plans/<name>.md` automatically |
| ✅ Approve & execute | Claude calls `ExitPlanMode` — you accept in the UI |
| ❌ Reject / revise | Ask for changes; Claude updates the plan in place |
| 🔚 Cancel | Reply "cancel" or toggle modes again |

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

### Stage details

1. **🚪 Enter** — You trigger Plan Mode with `/plan` or the shortcut. Claude acknowledges and stops making edits.
2. **🔍 Explore** — Claude reads the spec (`.claude/specs/`), opens the files it will touch, runs `Grep`/`Glob` to understand existing patterns. It may ask clarifying questions via `AskUserQuestion`.
3. **🧠 Design** — Claude drafts a structured plan: files to change, functions to add, edge cases, verification steps, risks.
4. **💾 Persist** — The plan lives as a markdown file in `.claude/plans/`, so it survives the session, shows up in `git diff`, and can be reviewed later.
5. **👀 Approve** — You read the plan. Accept as-is, request tweaks, or reject entirely. Nothing ships without your nod.
6. **🛠️ Execute** — On approval, Plan Mode exits and Claude implements exactly what was agreed.

---

## ✅ What You Can & ❌ Cannot Do in Plan Mode

| Tool / Action | Plan Mode? |
| --- | --- |
| `Read` files | ✅ Allowed |
| `Grep` / `Glob` search | ✅ Allowed |
| `Bash` read-only commands (`ls`, `git log`, `SELECT …`) | ✅ Allowed |
| `WebFetch` / `WebSearch` | ✅ Allowed |
| `AskUserQuestion` | ✅ Allowed |
| Write the plan doc itself | ✅ Allowed |
| `Edit` source files | ❌ Blocked |
| `Write` new source files | ❌ Blocked |
| `Bash` destructive commands (`rm`, `git push`, installs) | ❌ Blocked |
| Commit / push to git | ❌ Blocked |

---

## 🎯 When to Use Plan Mode

Use it when **any** of these are true:

- 🏗️ The task touches **multiple files** or multiple layers.
- 🧩 There are **architectural choices** to make (schema, auth strategy, file layout).
- 📚 The feature has a **spec** you want Claude to read carefully first.
- 🎓 You're on a **course project** where each step deserves instructor-style review.
- 🔐 The blast radius is large — DB migrations, refactors, deletions.
- 🤷 You're **not 100% sure** what the AI will do and want to see it in prose first.

### 🚫 When to Skip Plan Mode

- Tiny fixes: typos, one-line bugs, renaming a variable.
- Pure Q&A: "how does this function work?"
- Tasks where the spec is so exhaustive there's nothing to design.

---

## 💎 Why Plan Mode is Valuable

| Problem without a plan | How Plan Mode fixes it |
| --- | --- |
| 🏃 AI dives into edits before reading the code | Forces a research pass first |
| 🌪️ Large tasks produce sprawling, off-target diffs | You review approach **before** any byte is written |
| 🤐 Architectural choices get locked in silently | Trade-offs surface in plain English for approval |
| 🔥 Dead-end attempts waste tokens and time | Dead ends are caught in prose, not in code |
| 📜 No paper trail for *why* a decision was made | `.claude/plans/` becomes durable documentation |

---

## 🗂️ Plan Mode in This Project

In **Spendly**, each course step has:

- 📄 A spec at `.claude/specs/0X-xxx.md` (what to build)
- 📝 A plan at `.claude/plans/0X-xxx.md` (how to build it)
- 💻 The actual implementation in Python/HTML/CSS

For example, Step 1 (Database Setup):

1. Instructor-provided spec → `.claude/specs/01-database-setup.md`
2. You run `/plan` → Claude reads the spec, asks clarifying questions (e.g. "spendly.db vs expense_tracker.db?"), and writes `.claude/plans/01-database-setup.md`.
3. You review the plan → approve.
4. Claude implements `database/db.py` and wires `app.py`.

This is exactly why this step is going into Plan Mode first instead of straight-coding the DB helpers.

---

## 🧠 Mental Model

> **Plan Mode = The architect's pencil.**
> Regular mode = the builder's hammer.
> You don't swing the hammer until the blueprint is signed off.

---

## 🌙 اردو خلاصہ (Urdu Summary)

### 📌 Plan Mode کیا ہے؟
Plan Mode، Claude Code کا ایک خاص **"صرف پڑھنے والا" (read-only) موڈ** ہے۔ اس میں Claude پہلے **سوچتا ہے، تحقیق کرتا ہے، اور ایک تفصیلی منصوبہ بناتا ہے** — لیکن کوڈ میں کوئی تبدیلی نہیں کرتا جب تک آپ منظوری نہ دیں۔

### 🎯 کیوں ضروری ہے؟
- بڑے یا پیچیدہ کاموں میں سیدھا کوڈ لکھنا اکثر **غلط سمت** لے جاتا ہے۔
- Plan Mode پہلے **spec پڑھتا ہے، فائلیں جانچتا ہے، اور سوالات پوچھتا ہے**۔
- پھر ایک **مرحلہ وار منصوبہ** `.claude/plans/` میں محفوظ کرتا ہے۔
- آپ منصوبہ پڑھ کر **قبول، ترمیم، یا رد** کر سکتے ہیں۔
- منظوری کے بعد ہی Claude اصل کوڈ لکھنا شروع کرتا ہے۔

### 🛠️ کیسے استعمال کریں؟
1. چیٹ میں `/plan` لکھیں، یا `Shift+Tab` دبائیں۔
2. Claude فائلیں پڑھے گا اور سوالات کرے گا۔
3. منصوبہ `.claude/plans/` میں محفوظ ہوگا۔
4. آپ منظوری دیں گے، پھر کوڈ لکھا جائے گا۔

### ✅ فائدے
- 🛡️ کوڈ خراب ہونے سے بچتا ہے
- 👀 آپ کو مکمل **نظرثانی کا موقع** ملتا ہے
- 📚 ہر فیصلے کی **تحریری دستاویز** بن جاتی ہے
- 🎓 Course projects (جیسے Spendly) کے لیے بہترین

### 🚫 کب استعمال نہ کریں؟
- معمولی typo یا ایک لائن کی اصلاح
- صرف سوال جواب والے کام
- ایسے کام جہاں spec پہلے سے ہر تفصیل طے کر چکا ہو

### 🧠 سنہری اصول
> **پہلے منصوبہ → پھر منظوری → پھر عمل۔**
> کوڈ میں ہاتھ ڈالنے سے پہلے، بلیو پرنٹ پر دستخط لازمی ہیں۔
