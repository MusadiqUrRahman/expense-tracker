# 🧠 /memory — Claude Code Command

## ⚠️ Important Note
- `/memory` opens an **interactive editor** to view and edit your memory files
- Memory files are what Claude reads to **remember you** across conversations
- In **WSL2**, this command may show errors — use workarounds below

---

## 📌 Purpose
`/memory` is used to **view, edit, and manage Claude's auto memory files** — the files that help Claude remember things about you and your project.

---

## ⚙️ What It Does
- Opens an interactive editor for your memory files
- Shows all memory files Claude has saved about you
- Lets you add, edit, or delete memories
- Changes are saved and used in future conversations

---

## 🚀 Usage
```
/memory
```

---

## 🧠 How It Works
1. You type `/memory` inside a Claude Code session
2. Claude opens an **interactive editor** (like nano/vim)
3. You see the `MEMORY.md` index file
4. You can edit, add, or remove memories
5. Save and close → Claude uses updated memory next time

---

## 📂 Where Are Memory Files Stored?

### Linux / WSL2 Path:
```
~/.claude/projects/<project-name>/memory/
```

### Your Actual Path:
```
/home/win10/.claude/projects/-mnt-c-Users-win10-Desktop-Claude-Code-Course-expense-tracker/memory/
```

### Windows File Explorer Path:
```
\\wsl$\Ubuntu\home\win10\.claude\projects\-mnt-c-Users-win10-Desktop-Claude-Code-Course-expense-tracker\memory\
```

---

## 📄 What's Inside the Memory Folder?

```
memory/
├── MEMORY.md              ← 📋 Index file (list of all memories)
├── user_role.md           ← 🙋 Info about you
├── feedback_testing.md    ← 💬 Your preferences
├── project_info.md        ← 📁 Project details
└── reference_links.md     ← 🔗 External resources
```

### 📋 MEMORY.md (The Index)
- Main file Claude reads **first**
- Contains one-line pointers to each memory file
- Like a **table of contents**

### 📄 Individual Memory Files
Each file has this structure:
```markdown
---
name: user_role
description: User is a student learning Flask
type: user
---

User is a student learning Flask for the first time.
They prefer simple explanations with examples.
```

---

## 🧩 4 Types of Memories

| Type | Icon | What It Stores | Example |
|------|------|----------------|---------|
| **user** | 🙋 | About YOU | "User is a student" |
| **feedback** | 💬 | Your corrections & preferences | "Don't add summaries" |
| **project** | 📁 | Work context & deadlines | "Merge freeze on March 5" |
| **reference** | 🔗 | External tools & links | "Bugs tracked in Linear" |

---

## 🎮 3 Ways to Manage Memory

### Way 1: `/memory` Command
```
/memory
```
Opens interactive editor (may not work in WSL2)

### Way 2: Ask Claude Directly
```
"Remember that I prefer dark mode"     → Claude saves it
"Forget the tabs preference"           → Claude deletes it
"What do you remember about me?"       → Claude shows all
```

### Way 3: Edit Files Manually
```bash
# Open in VS Code
code ~/.claude/projects/-mnt-c-Users-win10-Desktop-Claude-Code-Course-expense-tracker/memory/MEMORY.md

# Open in Windows File Explorer
explorer.exe $(wslpath -w ~/.claude/projects/-mnt-c-Users-win10-Desktop-Claude-Code-Course-expense-tracker/memory/)
```

---

## ⚠️ WSL2 Error & Fix

### The Error:
```
❯ /memory
  ⎿ Error opening memory file: Error: setRawMode EIO
```

### Why It Happens:
- WSL2 terminal can't switch to interactive/editor mode
- This is a **WSL2 limitation**, not a Claude Code bug

### Workarounds:
| Method | Command |
|--------|---------|
| 🤖 Ask Claude | "Remember that I like tabs" |
| 📝 VS Code | `code ~/.claude/.../memory/MEMORY.md` |
| 📁 File Explorer | `explorer.exe \\wsl$\Ubuntu\home\win10\.claude\...` |
| 💻 Terminal | `nano ~/.claude/.../memory/MEMORY.md` |

---

## 🔄 Memory vs CLAUDE.md vs Chat History

```
┌─────────────────────────────────────────────────┐
│                                                   │
│  🧠 /memory (Auto Memory)                       │
│  ├── Claude writes it automatically              │
│  ├── Persists forever across conversations       │
│  ├── Personal to your machine                    │
│  └── "Claude's diary about you"                  │
│                                                   │
│  📜 CLAUDE.md                                    │
│  ├── YOU write it manually                       │
│  ├── Shared with team (in git)                   │
│  ├── Project rules and setup                     │
│  └── "Project rulebook"                          │
│                                                   │
│  💬 Chat History                                 │
│  ├── Created automatically each session          │
│  ├── Resets when you start new session           │
│  ├── Resume with /resume or claude -c            │
│  └── "Current conversation"                      │
│                                                   │
└─────────────────────────────────────────────────┘
```

---

## ❓ What Does NOT Get Saved in Memory?

| Not Saved | Reason |
|-----------|--------|
| 🚫 Code patterns | Claude can read the code directly |
| 🚫 Git history | Use `git log` instead |
| 🚫 File paths | Claude can discover with Glob/Grep |
| 🚫 Bug fix details | The fix is already in the code |
| 🚫 Temporary tasks | Use tasks/plans instead |
| 🚫 Stuff in CLAUDE.md | No need to duplicate |

---

## 💡 Pro Tips

1. ✅ You don't need `/memory` to manage memories — just **ask Claude**
2. ✅ Memory files are just **plain markdown** — you can edit them in any editor
3. ✅ Each project has **separate memories** — they don't mix
4. ✅ `MEMORY.md` index stays under **200 lines** for performance
5. ✅ Claude only saves **useful info** — not every word you say
6. ✅ Memory helps Claude give **better, personalized answers** over time

---

## 📚 Summary
`/memory` = View and edit Claude's brain (what it remembers about you)

---

## 🇵🇰 اردو خلاصہ

### `/memory` کیا ہے؟
> یہ کمانڈ Claude Code کی **یادداشت کی فائلیں** دیکھنے اور تبدیل کرنے کے لیے استعمال ہوتی ہے۔
> جب آپ Claude سے بات کرتے ہیں تو وہ اہم باتیں **خود بخود یاد** رکھتا ہے۔
> یہ یادداشت فائلوں میں محفوظ ہوتی ہے جو اگلی بات چیت میں بھی کام آتی ہے۔

### یادداشت کہاں محفوظ ہوتی ہے؟
> آپ کی مشین پر ایک چھپے ہوئے فولڈر میں:
> `~/.claude/projects/<پروجیکٹ>/memory/`
> یہ فائلیں صرف **آپ کے لیے** ہیں — ٹیم کے ساتھ شیئر نہیں ہوتیں۔

### 4 قسم کی یادداشت:
> - 🙋 **صارف** — آپ کے بارے میں ("میں طالب علم ہوں")
> - 💬 **فیڈبیک** — آپ کی ہدایات ("آسان الفاظ استعمال کرو")
> - 📁 **پروجیکٹ** — کام کی تفصیلات ("ڈیڈ لائن 5 مارچ ہے")
> - 🔗 **حوالہ** — بیرونی ٹولز ("بگز Linear میں ٹریک ہوتے ہیں")

### WSL2 میں مسئلہ:
> `/memory` کمانڈ WSL2 میں ایرر دے سکتی ہے۔
> اس کی بجائے آپ Claude سے کہیں: **"یاد رکھو کہ..."** اور وہ خود محفوظ کر لے گا۔
> یا فائلیں VS Code میں کھول کر خود ایڈٹ کریں۔

### سادہ الفاظ میں:
> `/memory` Claude کے دماغ میں جھانکنے کا طریقہ ہے۔
> Claude آپ کے بارے میں جو کچھ جانتا ہے — سب یہاں محفوظ ہوتا ہے۔
> آپ یہاں سے کچھ بھی شامل، ہٹا، یا تبدیل کر سکتے ہیں۔
