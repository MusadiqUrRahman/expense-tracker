# GitHub Commands — Quick Reference

A short guide for pushing code to GitHub from WSL.

---

## 🚀 Daily workflow (3 commands)

Every time you make changes:

```bash
git add .
git commit -m "what you changed"
git push
```

**Example:**
```bash
git add .
git commit -m "added logout button"
git push
```

---

## 🛠️ First-time setup (only once per project)

### 1. Configure your identity
```bash
git config --global user.name "YourGitHubUsername"
git config --global user.email "your-email@example.com"
```

### 2. Initialize the repo
```bash
git init
git branch -M main
```

### 3. Connect to GitHub (with token)
```bash
git remote add origin https://USERNAME:TOKEN@github.com/USERNAME/REPO.git
```

### 4. First push
```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 🔑 Personal Access Token

1. Go to: https://github.com/settings/tokens
2. **Generate new token (classic)**
3. ✅ Check the **`repo`** scope (required for push)
4. Copy the token — starts with `ghp_`
5. **Never share it publicly**

---

## 📋 Useful commands

| Command | What it does |
|---|---|
| `git status` | Show what changed |
| `git log --oneline` | List all commits |
| `git remote -v` | Show connected remote URL |
| `git branch` | Show current branch |
| `git pull` | Download latest from GitHub |
| `git diff` | Show line-by-line changes |

---

## ⚠️ Common errors

| Error | Fix |
|---|---|
| `Could not resolve host: github.com` | WSL internet issue — run `wsl --shutdown` in PowerShell |
| `Permission denied (403)` | Token missing `repo` scope — regenerate it |
| `Authentication failed` | Wrong token or username — check and retry |
| `remote origin already exists` | Use `git remote set-url origin <url>` instead of `add` |
| `nothing to commit, working tree clean` | No new changes — not an error |

---

## 🔒 Security rules

- ❌ **Never paste tokens in chat, code, or README**
- ❌ **Never commit `.env` or secret files** — add them to `.gitignore`
- ✅ **Use short token expiration** (30–90 days)
- ✅ **Revoke leaked tokens immediately** at https://github.com/settings/tokens
