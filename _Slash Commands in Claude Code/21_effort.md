# ⚡ /effort — Claude Code Command

## ⚠️ Important Note
- `/effort` controls **how much "thinking" Claude does** before answering
- Higher effort = **smarter + slower + more tokens**
- Lower effort = **faster + cheaper + less reasoning**
- Supported on **Opus 4.7, Opus 4.6, and Sonnet 4.6** only

---

## 📌 Purpose
`/effort` sets the **reasoning effort level** for the active model.

It tells Claude how hard to think before responding — from "just answer quickly" to "burn unlimited tokens thinking this through."

---

## ⚙️ What It Does
- Adjusts Claude's **adaptive reasoning depth**
- Controls **internal thinking tokens** before the visible reply
- Affects both normal responses **and** tool-call explanations
- Trades **speed + cost** against **intelligence**

---

## 🚀 Usage

```
/effort                  # opens an interactive slider
/effort low              # set directly to a level
/effort medium
/effort high
/effort xhigh            # Opus 4.7 only
/effort max              # session-only unless env var is set
/effort auto             # reset to model default
```

You can also adjust effort with the **left/right arrow keys** inside `/model`.

---

## 🎚️ Effort Levels

### Supported levels per model

| Model | Available levels |
|---|---|
| 🧠 **Opus 4.7** | `low`, `medium`, `high`, `xhigh`, `max` |
| 🧠 **Opus 4.6** | `low`, `medium`, `high`, `max` |
| ⚡ **Sonnet 4.6** | `low`, `medium`, `high`, `max` |

> If you set `xhigh` on a model that doesn't support it, Claude Code falls back to the highest supported level (e.g. `high` on Opus 4.6).

### 🎯 When to use each level

| Level | 💡 When to use | 💰 Cost | 🧠 Intelligence |
|---|---|---|---|
| 🟢 **low** | Short, simple, latency-sensitive tasks where smarts don't matter | 💲 | ⭐ |
| 🟡 **medium** | Cost-sensitive work — trade off some smarts for fewer tokens | 💲💲 | ⭐⭐ |
| 🟠 **high** | **Balanced** default for intelligence-sensitive coding | 💲💲💲 | ⭐⭐⭐ |
| 🔴 **xhigh** | **Best for most coding** on Opus 4.7 — recommended default | 💲💲💲💲 | ⭐⭐⭐⭐ |
| 🟣 **max** | **Demanding** reasoning problems; can overthink, so test first | 💲💲💲💲💲 | ⭐⭐⭐⭐⭐ |
| 🤖 **auto** | Reset to the model's default effort | — | — |

---

## 🗓️ Default Effort Levels

| Model | Default |
|---|---|
| Opus 4.7 (all plans) | `xhigh` |
| Opus 4.6 / Sonnet 4.6 | `high` |
| Opus 4.6 / Sonnet 4.6 on **Pro & Max plans** | `medium` |

> When you first run Opus 4.7, Claude Code applies `xhigh` even if you had a different level set for earlier models. Run `/effort` again to customize.

---

## 💾 Persistence

| Level | Persists across sessions? |
|---|---|
| `low` | ✅ Yes |
| `medium` | ✅ Yes |
| `high` | ✅ Yes |
| `xhigh` | ✅ Yes |
| **`max`** | ❌ **Current session only** (unless set via env var) |

---

## 🎮 6 Ways to Set Effort

```
1. /effort <level>                         ← during session (slider or direct)
2. /model                                  ← adjust slider inside model picker
3. claude --effort <level>                 ← at launch
4. export CLAUDE_CODE_EFFORT_LEVEL=<level> ← environment variable
5. settings.json { "effortLevel": "..." }  ← permanent setting
6. Skill / subagent frontmatter            ← per-skill override
```

### 🥇 Priority order (who wins?)
```
Environment variable  >  Configured level  >  Model default
```
Frontmatter effort applies **only while that skill/subagent is active**, overriding the session level but not the env var.

---

## ✨ "ultrathink" — One-off deep reasoning

Want more thinking on a single prompt **without** changing your session level?

```
"Please solve this recursion bug. ultrathink"
```

Add `ultrathink` anywhere in your message. Claude reasons harder on that turn only. It does **not** change the API effort level — just nudges the model in-context.

---

## 👀 How to See Your Current Level

- Shown **next to the logo and spinner**: `with low effort`, `with max effort`, etc.
- Also visible in `/model` picker
- Confirmed in status line (if configured)

---

## 🧠 Adaptive vs Fixed Reasoning

Claude Code uses **adaptive reasoning** — the model decides per-step whether and how much to think.

- **Opus 4.7** → always adaptive (cannot be disabled)
- **Opus 4.6 / Sonnet 4.6** → adaptive by default; can revert to fixed thinking budget via:
  ```
  export CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1
  ```
  Then `MAX_THINKING_TOKENS` controls the budget.

---

## 💡 Pro Tips

1. ✅ **Default is fine for most tasks** — only override when you have a reason
2. ✅ **Use `max` sparingly** — prone to overthinking, diminishing returns
3. ✅ **Use `low`** for boilerplate, renames, file-listing tasks
4. ✅ **Use `xhigh`/`max`** for architectural debugging, tricky algorithms
5. ✅ **Add `ultrathink`** to a single prompt instead of changing level
6. ✅ **Check the spinner** to confirm which level is active
7. ✅ **Skill frontmatter** can pin a skill to a specific effort level

---

## 🔁 /effort vs /model vs ultrathink

```
┌────────────────────────────────────────────────────┐
│                                                      │
│  ⚡ /effort                                          │
│  ├── Changes HOW HARD the model thinks              │
│  ├── Session-wide (except max)                      │
│  ├── Persists across sessions (low/med/high/xhigh)  │
│  └── "Thinking depth knob"                          │
│                                                      │
│  🧠 /model                                          │
│  ├── Changes WHICH model you use                    │
│  ├── Opus / Sonnet / Haiku                          │
│  ├── Includes effort slider inside                  │
│  └── "Brain selector"                               │
│                                                      │
│  ✨ ultrathink                                      │
│  ├── Keyword added to a single prompt               │
│  ├── One-turn effect only                           │
│  ├── Doesn't change the API level                   │
│  └── "Quick deep-think nudge"                       │
│                                                      │
└────────────────────────────────────────────────────┘
```

---

## ❓ Common Questions

| Q | A |
|---|---|
| 🤔 Does `/effort` work on Haiku? | ❌ No — only Opus 4.7, Opus 4.6, Sonnet 4.6. |
| 🤔 Does higher effort guarantee better answers? | 🙅 Not always — `max` can **overthink** simple tasks. |
| 🤔 Does effort cost more tokens? | ✅ Yes — more thinking = more internal tokens billed. |
| 🤔 Can I set different effort per skill? | ✅ Yes — via `effort:` in skill frontmatter. |
| 🤔 Does `max` persist? | ❌ Only for the current session (unless set via env var). |
| 🤔 What if I set `xhigh` on Sonnet 4.6? | ⤵️ Falls back to `high` automatically. |

---

## 📚 Summary
`/effort` = Reasoning depth dial. Low = fast & cheap. Max = deepest reasoning, session-only.

> **Default is good. Tune only when you have a reason.**

---

## 🇵🇰 اردو خلاصہ

### ⚡ `/effort` کیا ہے؟
> یہ command Claude کو بتاتی ہے کہ **جواب دینے سے پہلے کتنا سوچنا ہے**۔
> زیادہ effort = **زیادہ ذہین + سست + زیادہ tokens**
> کم effort = **تیز + سستا + کم سوچ بچار**

---

### 🎯 کن models پر کام کرتی ہے؟
> صرف ان **تین models** پر:
> - 🧠 **Opus 4.7**
> - 🧠 **Opus 4.6**
> - ⚡ **Sonnet 4.6**
>
> **Haiku** پر کام نہیں کرتی۔

---

### 🎚️ پانچ levels

| Level | کب استعمال کریں؟ |
|---|---|
| 🟢 **low** | چھوٹے، سادے، تیز کام (جیسے rename، typo) |
| 🟡 **medium** | tokens بچانا ہوں لیکن تھوڑی سوچ بھی چاہیے |
| 🟠 **high** | **زیادہ تر coding کام** کے لیے متوازن option |
| 🔴 **xhigh** | Opus 4.7 پر **بہترین coding نتائج** (صرف Opus 4.7) |
| 🟣 **max** | بہت پیچیدہ مسائل — لیکن **سوچ سوچ کر خراب** بھی کر سکتا ہے |

---

### 🚀 کیسے استعمال کریں؟

```
/effort              ← interactive slider
/effort high         ← براہ راست level set کریں
/effort auto         ← default پر واپس
```

### 🎮 6 طریقے set کرنے کے:
> 1. `/effort <level>` — session میں
> 2. `/model` — picker کے اندر slider
> 3. `claude --effort <level>` — launch پر
> 4. `CLAUDE_CODE_EFFORT_LEVEL` — environment variable
> 5. `settings.json` میں `effortLevel`
> 6. Skill / subagent frontmatter میں `effort:`

---

### ✨ "ultrathink" — ایک بار کی گہری سوچ
> اگر صرف **ایک prompt** کے لیے زیادہ سوچ چاہیے، اپنے message میں `ultrathink` لکھ دیں:
> ```
> "اس bug کو حل کرو۔ ultrathink"
> ```
> یہ صرف اس **ایک turn** پر اثر کرے گا۔

---

### 💾 Persistence
> - `low`, `medium`, `high`, `xhigh` → **اگلی session میں بھی یاد** رہتا ہے
> - `max` → **صرف موجودہ session** کے لیے (env variable استثنا ہے)

---

### 💡 اہم tips
> 1. ✅ **Default (`high` یا `xhigh`) کافی ہے** — بغیر وجہ مت بدلیں
> 2. ⚠️ **`max` بہت کم استعمال کریں** — over-thinking کا خطرہ
> 3. ✅ **`low` بہترین** ہے: rename، typo، boilerplate کے لیے
> 4. ✅ **`xhigh`/`max`** رکھیں: complex algorithms، tricky debugging کے لیے
> 5. ✅ **`ultrathink` استعمال** کریں جب level مستقل نہیں بدلنا

---

### 🧠 سنہری اصول
> **`/effort` = سوچ کا knob**
> - زیادہ گھما ← **زیادہ ذہین، زیادہ سست، زیادہ مہنگا**
> - کم گھما ← **کم ذہین، زیادہ تیز، زیادہ سستا**
>
> **Default اکثر بہترین ہوتا ہے۔ صرف ضرورت پر تبدیل کریں۔**

### سادہ الفاظ میں:
> `/effort` Claude کو بتاتا ہے: **"کتنی توانائی سے سوچنا ہے؟"**
> ہلکا کام = ہلکی سوچ۔ مشکل کام = گہری سوچ۔

---

## 📖 Sources
- [Model configuration — Claude Code Docs](https://code.claude.com/docs/en/model-config)
- [Effort — Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/effort)


/effort کمانڈ Claude Code میں اس لیے استعمال ہوتی ہے تاکہ آپ یہ کنٹرول کر سکیں کہ Claude کسی کام پر کتنی گہرائی سے سوچے اور کتنے وسائل (tokens اور وقت) استعمال کرے۔

اگر آپ کم effort استعمال کرتے ہیں تو Claude تیزی سے جواب دیتا ہے لیکن اس میں گہرائی کم ہوتی ہے، جبکہ زیادہ effort دینے پر Claude زیادہ تفصیل سے سوچتا ہے، بہتر تجزیہ کرتا ہے اور زیادہ accurate جواب دیتا ہے، لیکن اس میں وقت اور cost زیادہ لگتی ہے۔

یہ خاص طور پر اس لیے ضروری ہے کیونکہ ہر کام ایک جیسا نہیں ہوتا — کچھ کام سادہ ہوتے ہیں جن کے لیے زیادہ سوچ کی ضرورت نہیں ہوتی، جبکہ کچھ کام پیچیدہ ہوتے ہیں جن کے لیے گہری reasoning ضروری ہوتی ہے۔

اس کمانڈ کے ذریعے آپ اپنے کام کے مطابق Claude کی سوچ کو adjust کر سکتے ہیں، جس سے آپ بہتر performance، کم خرچ اور زیادہ accurate results حاصل کر سکتے ہیں۔
