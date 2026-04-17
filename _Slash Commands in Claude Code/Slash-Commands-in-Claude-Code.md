# Slash Commands & Session Management in Claude Code

## Table of Contents
- [CLI Flags for Session Management](#cli-flags-for-session-management)
- [Slash Commands Inside a Session](#slash-commands-inside-a-session)
- [Conversation History & Context Management](#conversation-history--context-management)
- [Complete List of ALL Slash Commands](#complete-list-of-all-slash-commands)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Best Practices](#best-practices)

---

## CLI Flags for Session Management

These are commands you run **in your terminal** (outside a Claude session).

### `claude -c` / `claude --continue`

**Purpose**: Load and resume the **most recent** conversation in the current directory.

**What it does**:
- Restores the entire conversation history from the most recent session
- Picks up exactly where you left off with the same session ID
- Preserves all previous context, tool usage, and results

**How to use**:
```bash
claude --continue
claude -c
claude -c -p "query"  # Continue in non-interactive mode with a prompt
```

---

### `claude -r` / `claude --resume`

**Purpose**: Resume a **specific** session by ID or name, or open an **interactive picker** to choose from available sessions.

**What it does**:
- Allows you to resume **any** previous session, not just the most recent one
- Can resume by session name or ID
- Opens an interactive session picker when called without arguments
- Restores full conversation history and context

**How to use**:
```bash
# Open the interactive session picker (shows a list of all past sessions)
claude --resume
claude -r

# Resume a specific named session
claude --resume auth-refactor
claude -r "auth-refactor"

# Resume a session by ID
claude --resume "550e8400-e29b-41d4-a716-446655440000"

# Resume in non-interactive mode
claude -r "session-name" "query"
```

**Session Picker Keyboard Shortcuts**:

| Shortcut | Action |
|----------|--------|
| Up/Down | Navigate between sessions |
| Right/Left | Expand or collapse grouped sessions |
| Enter | Select and resume the highlighted session |
| P | Preview the session content |
| R | Rename the highlighted session |
| / | Search to filter sessions |
| A | Toggle between current directory and all projects |
| B | Filter to sessions from your current git branch |
| Esc | Exit the picker or search mode |

---

### `claude --fork-session`

**Purpose**: Create a new session ID while preserving conversation history up to that point.

**What it does**:
- Creates a branching point in your work
- Preserves all conversation history up to that point
- Gives you a new, independent session ID
- Original session remains unchanged

**How to use**:
```bash
# Fork the most recent session
claude --continue --fork-session

# Fork a specific named session
claude --resume auth-refactor --fork-session

# Fork via non-interactive mode
claude -c --fork-session -p "Try a different approach"
```

---

### `claude --from-pr <number>`

**Purpose**: Resume sessions linked to a specific GitHub pull request.

```bash
claude --from-pr 123
claude --from-pr https://github.com/owner/repo/pull/123
```

---

### `claude -n` / `claude --name`

**Purpose**: Set a display name for a session so you can find it later easily.

```bash
claude -n "auth-refactor"
claude --name "payment-integration"
```

---

### `claude --session-id`

**Purpose**: Use a specific session ID (UUID) for the conversation (advanced).

```bash
claude --session-id "550e8400-e29b-41d4-a716-446655440000"
```

---

### Other CLI Flags Related to Sessions

| Flag | Purpose |
|------|---------|
| `--bare` | Minimal mode: skip auto-discovery of hooks, skills, plugins |
| `--init` | Run initialization hooks and start interactive mode |
| `--init-only` | Run initialization hooks and exit (no session) |
| `--no-session-persistence` | Don't save sessions to disk (non-interactive mode only) |
| `--worktree` / `-w` | Start in isolated git worktree |
| `--tmux` | Create tmux session for worktree |
| `--permission-mode` | Begin in specified permission mode |
| `--debug` | Enable debug mode |
| `--verbose` | Enable verbose logging |

---

## Slash Commands Inside a Session

These are commands you type **inside** a running Claude Code session (after the `>` prompt).

### `/resume [session]`

**Purpose**: Switch to or resume a different conversation from within your current session.

**What it does**:
- Opens an interactive session picker to choose a different conversation
- Can resume by session name or ID
- Shows metadata: session name, time elapsed, message count, git branch
- Alias: `/continue`

**How to use**:
```
/resume
/resume auth-refactor
```

---

### `/rename [name]`

**Purpose**: Rename the current session.

```
/rename auth-refactor
/rename           # Auto-generates a name from conversation content
```

---

### `/branch [name]` / `/fork`

**Purpose**: Create a branch of the current conversation at this point.

```
/branch alternative-approach
/fork
```

---

### `/rewind` / `/checkpoint`

**Purpose**: Rewind the conversation and/or code to a previous point.

```
/rewind
# Or press: Esc + Esc (press Esc twice)
```

---

### `/clear` / `/reset` / `/new`

**Purpose**: Clear conversation history and free up context. Starts a fresh conversation.

---

### `/compact [instructions]`

**Purpose**: Compact conversation with optional focus instructions to manage context usage.

```
/compact
/compact focus on authentication code
```

---

### `/context`

**Purpose**: Visualize current context usage as a colored grid. Shows what's using space.

---

### `/export [filename]`

**Purpose**: Export the current conversation as plain text.

---

### `/cost`

**Purpose**: Show token usage statistics for the current session.

---

### `/status`

**Purpose**: Show version, model, account, and connectivity status.

---

## Complete List of ALL Slash Commands

| Command | Purpose | Aliases |
|---------|---------|---------|
| `/add-dir <path>` | Add a new working directory to the session | |
| `/agents` | Manage agent/subagent configurations | |
| `/btw <question>` | Ask a quick side question | |
| `/branch [name]` | Branch the current conversation | `/fork` |
| `/chrome` | Configure Claude in Chrome | |
| `/clear` | Clear conversation history | `/reset`, `/new` |
| `/color [color]` | Set the prompt bar color | |
| `/compact [instructions]` | Compact conversation to save context | |
| `/config` | Open Settings interface | `/settings` |
| `/context` | Visualize context usage | |
| `/copy [N]` | Copy last response to clipboard | |
| `/cost` | Show token usage stats | |
| `/desktop` | Continue in Claude Code Desktop app | `/app` |
| `/diff` | Open interactive diff viewer | |
| `/doctor` | Diagnose your installation | |
| `/effort [level]` | Set model effort (low/medium/high/max/auto) | |
| `/exit` | Exit the CLI | `/quit` |
| `/export [filename]` | Export conversation as text | |
| `/extra-usage` | Configure extra usage for rate limits | |
| `/fast [on\|off]` | Toggle fast mode | |
| `/feedback [report]` | Submit feedback | `/bug` |
| `/help` | Show help and available commands | |
| `/hooks` | View hook configurations | |
| `/ide` | Manage IDE integrations | |
| `/init` | Initialize project with CLAUDE.md | |
| `/insights` | Generate session analysis report | |
| `/install-github-app` | Set up Claude GitHub Actions app | |
| `/install-slack-app` | Install Claude Slack app | |
| `/keybindings` | Open keybindings config | |
| `/login` | Sign in to Anthropic account | |
| `/logout` | Sign out from Anthropic account | |
| `/mcp` | Manage MCP server connections | |
| `/memory` | Edit CLAUDE.md memory files | |
| `/mobile` | Show QR code for mobile app | `/ios`, `/android` |
| `/model [model]` | Select or change the AI model | |
| `/passes` | Share a free week of Claude Code | |
| `/permissions` | View or update permissions | `/allowed-tools` |
| `/plan [description]` | Enter plan mode | |
| `/plugin` | Manage Claude Code plugins | |
| `/pr-comments [PR]` | Fetch GitHub PR comments | |
| `/privacy-settings` | View/update privacy settings | |
| `/release-notes` | View the changelog | |
| `/reload-plugins` | Reload active plugins | |
| `/remote-control` | Enable remote control from claude.ai | `/rc` |
| `/remote-env` | Configure remote environment | |
| `/rename [name]` | Rename current session | |
| `/resume [session]` | Resume a conversation | `/continue` |
| `/rewind` | Rewind to previous point | `/checkpoint` |
| `/sandbox` | Toggle sandbox mode | |
| `/schedule [description]` | Manage scheduled tasks | |
| `/security-review` | Analyze changes for security issues | |
| `/skills` | List available skills | |
| `/stats` | Visualize usage and streaks | |
| `/status` | Show version/model/account info | |
| `/statusline` | Configure status line | |
| `/stickers` | Order Claude Code stickers | |
| `/tasks` | List and manage background tasks | |
| `/terminal-setup` | Configure terminal keybindings | |
| `/theme` | Change color theme | |
| `/upgrade` | Open upgrade page | |
| `/usage` | Show plan usage and rate limits | |
| `/vim` | Toggle Vim editing mode | |
| `/voice` | Toggle push-to-talk voice dictation | |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Esc + Esc | Rewind or summarize (same as `/rewind`) |
| Ctrl+C | Cancel current input or generation |
| Ctrl+D | Exit Claude Code session |
| Ctrl+L | Clear terminal screen (keeps conversation) |
| Ctrl+O | Toggle verbose output |
| Ctrl+R | Reverse search command history |
| Ctrl+T | Toggle task list view |
| Shift+Tab or Alt+M | Cycle permission modes |
| Alt+P or Option+P | Switch model |
| Alt+T or Option+T | Toggle extended thinking |
| Alt+O or Option+O | Toggle fast mode |

---

## Conversation History & Context Management

### How History Works
- All conversations are **automatically saved** locally with full message history
- Sessions are tied to your **working directory** (per-project)
- When you resume, the entire message history is restored
- Tool usage and results from previous conversations are preserved

### What's NOT Preserved When Resuming
- Session-scoped permissions (must be re-approved)
- Git state changes between sessions (you see the current branch's files)

### The Context Window
Claude's context holds: conversation history, file contents, command outputs, CLAUDE.md instructions, auto memory (first 200 lines), and system instructions.

**When context fills up**, older tool outputs are cleared first, then conversation may be summarized. Use `/compact` to manually free space.

---

## Best Practices

### Name Your Sessions
```bash
claude -n "auth-refactor"     # Name at startup
/rename payment-integration   # Rename during session
```

### Resume vs Fork
- **Resume** (`claude -r`): Continue from where you left off
- **Fork** (`--fork-session`): Try a different approach without affecting the original

### Finding Yesterday's Work
```bash
claude -r    # Opens picker, navigate to find your session
claude -c    # Quick resume of the most recent session
```

### Parallel Sessions
Use git worktrees to prevent collision:
```bash
claude --worktree feature-auth
claude --worktree bugfix-123
```
