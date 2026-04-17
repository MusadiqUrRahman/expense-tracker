# 🧠 Auto Memory — Complete Guide

---

## 🤔 What is Auto Memory?

Auto Memory is Claude Code's **built-in memory system** that automatically
remembers important things about you **across conversations**.

> Think of it like Claude has a **personal diary** about you.
> Every time you tell Claude something important, it writes it down.
> Next time you talk to Claude, it reads the diary first — so it already knows you!

---

## ⚙️ How Does It Work?

```
Step 1️⃣  →  You say something important
              "I'm a student learning Flask"

Step 2️⃣  →  Claude notices it's worth remembering
              (not everything gets saved — only useful info)

Step 3️⃣  →  Claude saves it to a .md file
              Creates: user_role.md → "User is a student"

Step 4️⃣  →  Next conversation starts
              Claude reads ALL memory files automatically

Step 5️⃣  →  Claude already knows who you are!
              No need to repeat yourself ✨
```

---

## 📍 Where is Memory Stored?

Memory lives inside a **special folder** on your machine:

```
~/.claude/projects/<project-name>/memory/
│
├── MEMORY.md                ← 📋 Index file (list of all memories)
├── user_role.md             ← 🙋 "User is a student learning Flask"
├── feedback_testing.md      ← 💬 "User wants simple explanations"
├── project_info.md          ← 📁 "Project uses port 5001"
└── reference_links.md       ← 🔗 "Bugs tracked in Linear"
```

### 📋 MEMORY.md (The Index)
- This is the **main file** Claude reads first
- It contains **one-line pointers** to each memory file
- Like a **table of contents** for Claude's brain

### 📄 Individual Memory Files
- Each memory is saved in its **own .md file**
- Has a **name**, **description**, and **type**
- Contains the actual information Claude remembers

---

## 🧩 4 Types of Memory

### 1️⃣ 🙋 User Memory
**What:** Information about YOU — your role, skills, preferences

```markdown
Example memories:
- "User is a student learning Flask for the first time"
- "User has 10 years of Go experience but is new to React"
- "User prefers English responses"
```

**Why it helps:** Claude tailors explanations to YOUR level

---

### 2️⃣ 💬 Feedback Memory
**What:** Corrections and preferences about HOW Claude should work

```markdown
Example memories:
- "Don't add summaries at the end of responses"
- "User prefers one big PR over many small ones"
- "Always explain code line by line"
```

**Why it helps:** Claude doesn't repeat the same mistakes

---

### 3️⃣ 📁 Project Memory
**What:** Information about ongoing work, goals, deadlines

```markdown
Example memories:
- "Merge freeze starts March 5 for mobile release"
- "Auth rewrite is driven by legal compliance, not tech debt"
- "Database migration planned for next sprint"
```

**Why it helps:** Claude understands the bigger picture

---

### 4️⃣ 🔗 Reference Memory
**What:** Pointers to external tools and resources

```markdown
Example memories:
- "Pipeline bugs tracked in Linear project INGEST"
- "API latency dashboard at grafana.internal/d/api-latency"
- "Design specs in Figma project called Spendly-v2"
```

**Why it helps:** Claude knows where to find information

---

## 🎮 How to Control Memory

### ✅ Ask Claude to Remember
```
You: "Remember that I prefer tabs over spaces"
Claude: [saves feedback memory] ✅
```

### ❌ Ask Claude to Forget
```
You: "Forget that preference about tabs"
Claude: [removes the memory file] ✅
```

### 👀 Check What Claude Remembers
```
You: "What do you remember about me?"
Claude: [reads MEMORY.md and tells you] ✅
```

### 🔄 Claude Also Saves Automatically
- When you correct Claude → saves as feedback
- When you mention your role → saves as user info
- When you share project context → saves as project info
- You don't always need to say "remember" — Claude picks up on important things!

---

## 🆚 Auto Memory vs Other Systems

```
┌────────────────────────────────────────────────────────┐
│                                                          │
│  🧠 Auto Memory                                        │
│  ├── Claude writes it automatically                     │
│  ├── Persists across conversations                      │
│  ├── Personal to your machine                           │
│  └── Grows over time as Claude learns about you         │
│                                                          │
│  📜 CLAUDE.md                                           │
│  ├── YOU write it manually                              │
│  ├── Shared with team (in git)                          │
│  ├── Project rules and setup commands                   │
│  └── Fixed until you update it                          │
│                                                          │
│  📂 .claude/ folder                                     │
│  ├── Contains memory + plans + settings                 │
│  ├── Claude manages it                                  │
│  └── Auto Memory lives INSIDE this folder               │
│                                                          │
└────────────────────────────────────────────────────────┘
```

| Feature | Auto Memory | CLAUDE.md | Chat History |
|---------|-------------|-----------|--------------|
| Who writes? | 🤖 Claude | 👤 You | Both |
| Persists? | ✅ Forever | ✅ Forever | ❌ Resets each session |
| Shared? | ❌ Personal | ✅ Team (git) | ❌ Personal |
| What's inside? | Learned info | Project rules | Full conversation |
| Auto-created? | ✅ Yes | ❌ You make it | ✅ Yes |

---

## 📄 What a Memory File Looks Like Inside

```markdown
---
name: user_role
description: User is a student learning Flask
type: user
---

User is a student learning Flask for the first time.
They prefer simple explanations with examples.
They are comfortable with basic Python but new to web development.
```

Each file has:
- **name** → short identifier
- **description** → one-line summary (used to decide when to load)
- **type** → user / feedback / project / reference
- **content** → the actual memory

---

## ❓ What Does NOT Get Saved?

| Not Saved | Why |
|-----------|-----|
| 🚫 Code patterns | Can be found by reading the code |
| 🚫 Git history | Use `git log` instead |
| 🚫 Bug fix details | The fix is in the code already |
| 🚫 Temporary task info | Use tasks/plans for current work |
| 🚫 Things already in CLAUDE.md | No need to duplicate |

---

## 💡 Pro Tips

1. ✅ Memory is **read every conversation** — so it always has context about you
2. ✅ You can **ask Claude to remember or forget** anything
3. ✅ Claude is smart about **what's worth saving** — not every word gets stored
4. ✅ Memory files are **just markdown** — you can read/edit them yourself
5. ✅ Each project has its **own memory** — separate from other projects
6. ✅ The `MEMORY.md` index stays under **200 lines** to keep things fast

---

## 🇵🇰 اردو میں خلاصہ (Summary in Urdu)

### آٹو میموری کیا ہے؟
> آٹو میموری Claude Code کا **یادداشت کا نظام** ہے۔
> جب آپ Claude سے بات کرتے ہیں تو Claude اہم باتیں **خود بخود یاد** رکھتا ہے۔
> یہ یادداشت آپ کی مشین پر فائلوں میں محفوظ ہوتی ہے۔

### یہ کیسے کام کرتا ہے؟
> آپ کچھ اہم بتاتے ہیں → Claude اسے ایک `.md` فائل میں لکھ دیتا ہے
> اگلی بات چیت شروع ہوتی ہے → Claude پہلے وہ فائلیں پڑھتا ہے
> نتیجہ: Claude کو پہلے سے پتا ہوتا ہے کہ آپ کون ہیں اور کیا چاہتے ہیں!

### 4 قسم کی یادداشت:
> - 🙋 **صارف** — آپ کے بارے میں ("میں طالب علم ہوں")
> - 💬 **فیڈبیک** — آپ کی ہدایات ("آسان الفاظ استعمال کرو")
> - 📁 **پروجیکٹ** — کام کی تفصیلات ("ڈیڈ لائن 5 مارچ ہے")
> - 🔗 **حوالہ** — بیرونی ٹولز ("بگز Linear میں ٹریک ہوتے ہیں")

### آسان مثال:
> آٹو میموری ایسے ہے جیسے Claude کی **ذاتی ڈائری**۔
> جب بھی آپ کوئی اہم بات بتاتے ہیں، Claude اسے اپنی ڈائری میں لکھ لیتا ہے۔
> اگلی ملاقات میں وہ ڈائری پڑھ کر آتا ہے — اس لیے اسے سب یاد ہوتا ہے! 📖

### CLAUDE.md اور Auto Memory میں فرق:
> - 📜 `CLAUDE.md` = آپ لکھتے ہیں (پروجیکٹ کے قواعد)
> - 🧠 `Auto Memory` = Claude لکھتا ہے (آپ کے بارے میں سیکھی ہوئی باتیں)

---
