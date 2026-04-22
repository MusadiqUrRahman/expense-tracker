# Spec: Registration

## Overview
Turn the existing `GET /register` page into a fully working account-creation flow. Users submit name, email, and password from `register.html`; the server validates the input, hashes the password with werkzeug, inserts the new row into the `users` table, and redirects to `/login` with a success flash. This is the first step of Spendly's authentication layer and unblocks login (Step 3), session-aware profile (Step 4), and all user-scoped expense features that follow.

## Depends on
- Step 1 — Database setup (`users` table, `get_db()`, `init_db()`, `seed_db()` in `database/db.py`).

## Routes
- `GET /register` — already implemented — public — renders the registration form. No change to handler signature.
- `POST /register` — **new** — public — validates form input, creates a user, flashes a success message, redirects to `/login`. On validation error, re-renders `register.html` with an `error` message.

## Database changes
No database changes. The existing `users` table (`id`, `name`, `email UNIQUE`, `password_hash`, `created_at`) already supports everything this feature needs. Verified against `database/db.py:26-36`.

## Templates
- **Create:** none.
- **Modify:**
  - `templates/register.html` — change the form's hardcoded `action="/register"` to `action="{{ url_for('register') }}"` to comply with the "never hardcode URLs" rule in CLAUDE.md. No other structural changes.
  - `templates/base.html` — add a minimal flash-message block (if one doesn't already exist) so `/login` can display the "Account created, please sign in" confirmation after redirect.

## Files to change
- `app.py` — extend the `register` view to accept `POST`, add form validation, insert the user via `get_db()`, flash a success message, and redirect to `login`. Import `request`, `redirect`, `url_for`, `flash` from flask and `generate_password_hash` from `werkzeug.security`. Configure `app.secret_key` (required for `flash`) from an env var with a dev fallback.
- `templates/register.html` — swap the hardcoded action for `url_for()`.
- `templates/base.html` — render flashed messages (only if no flash rendering already exists).

## Files to create
None.

## New dependencies
No new dependencies. `werkzeug` is already installed.

## Rules for implementation
- No SQLAlchemy or ORMs — use `sqlite3` through `get_db()`.
- Parameterised queries only — `?` placeholders, never f-strings in SQL.
- Passwords hashed with `werkzeug.security.generate_password_hash` before insert; never store plaintext.
- Use CSS variables for any new styling — never hardcode hex values.
- All templates extend `base.html`.
- DB access lives in routes via `get_db()`; keep SQL in the route for this step (no new helper in `db.py` is required).
- Always close the connection (use `try/finally` or context management) even on error paths.
- Validation server-side (don't trust client required attributes):
  - `name` — required, trimmed, 1–80 chars.
  - `email` — required, trimmed, lowercased, contains `@`, max 120 chars.
  - `password` — required, minimum 8 chars.
  - Duplicate email → catch `sqlite3.IntegrityError` and re-render with a friendly error, not a 500.
- Use `abort()` only for unexpected errors — use `render_template(..., error=...)` for user-facing validation messages, matching the existing `{% if error %}` block in `register.html`.
- `app.secret_key` must be set before any call to `flash()`; read from `os.environ.get("SECRET_KEY", "dev-secret-change-me")`.

## Definition of done
- [ ] Submitting a valid registration form inserts exactly one row into `users` and redirects to `/login` (HTTP 302).
- [ ] The stored `password_hash` starts with `pbkdf2:` (or werkzeug's current default) — never equals the plaintext password.
- [ ] After redirect, `/login` displays a flash message confirming the account was created.
- [ ] Submitting with a duplicate email re-renders `register.html` with a visible error and inserts nothing (users row count unchanged).
- [ ] Submitting with missing `name`, missing `email`, invalid email, or password shorter than 8 chars re-renders with a visible error and inserts nothing.
- [ ] `GET /register` still renders the form unchanged for anonymous visitors.
- [ ] `register.html` uses `url_for('register')` in the form action — no hardcoded URLs remain.
- [ ] `python app.py` starts without errors; the app still listens on port 5001.
- [ ] Manual check in sqlite: `SELECT id, name, email, length(password_hash) FROM users WHERE email = ?` returns the newly created row with a non-trivial hash length (> 60 chars).
