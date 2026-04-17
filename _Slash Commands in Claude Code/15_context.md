# ⚡ /context — Claude Code Command

## 📌 Purpose
`/context` is used to **visualize how much context (tokens) is being used in your current session**.

---

## ⚙️ What It Does
- Shows a visual grid of context usage  
- Displays used and remaining tokens  
- Breaks down usage by category  
- Helps you understand session memory  

---

## 🚀 Usage
/context

---

## 📊 What You See (Explained)

### 🔹 Colored Grid
- Shows how much context is used  
- Filled blocks = used space  
- Empty blocks = free space  

---

### 🔹 Token Usage
Example:
20.7k / 200k tokens (10%)

- 20.7k = used  
- 200k = total limit  
- 10% = usage percentage  

---

### 🔹 Categories Breakdown

#### 🧠 System Prompt
- Instructions given by Claude  
- Base system behavior  

#### 🛠️ System Tools
- Built-in tools and capabilities  
- Internal processing usage  

#### 📂 Memory Files
- Saved memory or project files  
- مثل MEMORY.md  

#### 🧩 Skills
- Claude’s learned abilities  
- Extra capabilities  

#### 💬 Messages
- Your chat messages  

#### 🟩 Free Space
- Remaining available context  

#### 🔄 Autocompact Buffer
- Reserved space for auto cleanup  
- Prevents overflow  

---

## 💡 When to Use
- When session becomes large  
- When Claude feels slow or confused  
- When managing token usage  
- When working on long projects  

---

## 🧠 Pro Tip
If context is too high, use `/compact` to reduce it and improve performance.

---

## ⚠️ Notes
- Context = memory of the session  
- More context = more tokens used  
- Too much context may reduce accuracy  

---

## 📚 Summary
`/context` = See session memory usage  

---

## 🇵🇰 اردو خلاصہ
یہ کمانڈ Claude Code میں آپ کے موجودہ سیشن کی memory (context) کو دیکھنے کے لیے استعمال ہوتی ہے۔  
اس کے ذریعے آپ کو واضح طور پر نظر آتا ہے کہ آپ نے کتنے tokens استعمال کیے ہیں اور کتنی جگہ باقی ہے، ساتھ ہی یہ بھی دکھاتا ہے کہ کون سی چیزیں زیادہ جگہ لے رہی ہیں جیسے system، tools یا messages۔  

یہ اس لیے بہت ضروری ہے کیونکہ اگر context زیادہ ہو جائے تو Claude سست ہو سکتا ہے یا درست جواب نہیں دے پاتا، اس لیے `/context` استعمال کر کے آپ اپنے سیشن کو بہتر طریقے سے manage کر سکتے ہیں اور وقت پر اسے optimize کر سکتے ہیں۔