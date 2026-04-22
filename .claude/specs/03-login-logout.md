# Spec: Login and Logout

## Overview
Turn the existing `GET /login` page and the `/logout` stub into a full session-based authentication flow. Users submit email and password from `login.html`; the server looks the user up by email, verifies the hash with werkzeug, stores `user_id` in the Flask session, and redirects to `/profile`. `GET /logout` clears the session and redirects back to `/login` with a flash. This closes the loop opened by Step 2 (Registration) and is the gating dependency for every logged-in-only route that follows — profile (Step 4), add/edit/delete expenses (Steps 7–9).

## Depends on
- Step 1 — Database setup (`users` table, `get_db()`, `init_db()`, `seed_db()`).
- Step 2 — Registration (users can be created with a werkzeug password hash, `app.secret_key` is already configured).

## Routes
- `GET /login` — already implemented — public — renders `login.html`. Handler signature needs to grow to accept `POST`.
- `POST /login` — **new** — public — validates form input, looks up the user by email, verifies the password hash, sets `session["user_id"]` and `session["user_name"]`, flashes a welcome message, and redirects to `/profile`. On bad credentials or missing fields, re-renders `login.html` with a generic `error` message (do not leak which field was wrong).
- `GET /logout` — **replace stub** — logged-in — calls `session.clear()`, flashes a sign-out confirmation, and redirects to `/login`. Accessing while already logged out is harmless — still redirect to `/login`.

## Database changes
No database changes. The existing `users` table already has `email` (UNIQUE) and `password_hash`, which is everything authentication needs. Verified against `database/db.py:26-36`.

## Templates
- **Create:** none.
- **Modify:**
  - `templates/login.html` — change the hardcoded `action="/login"` to `action="{{ url_for('login') }}"` to satisfy the "never hardcode URLs" rule in CLAUDE.md. Existing `{% if error %}` block is reused as-is.
  - `templates/base.html` — update the navbar so it shows "Sign in / Get started" when logged out and "Profile / Log out" when logged in. The flash block already exists and needs no change.

## Files to change
- `app.py`
  - Extend the `login` view to accept `POST`. Import `session` from flask and `check_password_hash` from `werkzeug.security` (alongside existing `generate_password_hash`).
  - Replace the `logout` stub with a real handler that clears the session and redirects to `/login`.
  - Keep all SQL in the route via `get_db()` — no new helper in `db.py` for this step.
- `templates/login.html` — swap the hardcoded form action for `url_for('login')`.
- `templates/base.html` — conditionally render navbar links based on `session.get('user_id')`.

## Files to create
None.

## New dependencies
No new dependencies. `werkzeug.security.check_password_hash` is already available.

## Rules for implementation
- No SQLAlchemy or ORMs — use `sqlite3` through `get_db()`.
- Parameterised queries only — `?` placeholders, never f-strings in SQL.
- Passwords verified with `werkzeug.security.check_password_hash` — never compare hashes with `==`, never re-hash the input and compare hashes.
- Use CSS variables for any new styling — never hardcode hex values.
- All templates extend `base.html`.
- Always close the DB connection (use `try/finally`) even on the error path.
- Validation server-side:
  - `email` — required, trimmed, lowercased before lookup.
  - `password` — required, non-empty (no length rule on login — length rules belong on registration only).
- Generic error message on bad credentials: `"Invalid email or password."` — do **not** differentiate between "no such user" and "wrong password".
- Session contents: store `session["user_id"]` (int) and `session["user_name"]` (str) only — never store the password hash or email in the session.
- `logout` must use `session.clear()` (not `session.pop("user_id")`) so future session keys don't linger.
- Do **not** add a `@login_required` decorator in this step — profile and expense routes will gain auth in their own steps. Scope creep is out.
- Use `flash(..., "success")` for the post-login welcome and post-logout confirmation; use the existing `error` template variable (not `flash`) for bad-credential messages, matching the pattern already used in `register` and `login`.

## Definition of done
- [ ] Submitting valid credentials for the seeded demo user (`demo@spendly.com` / `demo123`) sets `session["user_id"]` and redirects to `/profile` (HTTP 302).
- [ ] Submitting a wrong password re-renders `login.html` with `"Invalid email or password."` and no session is created.
- [ ] Submitting an unknown email re-renders `login.html` with the **same** `"Invalid email or password."` message (no user-enumeration leak).
- [ ] Submitting with missing email or missing password re-renders with a visible error and sets no session.
- [ ] Email lookup is case-insensitive — logging in as `DEMO@SPENDLY.COM` works.
- [ ] `GET /logout` clears the session, flashes a sign-out message, and redirects to `/login` (HTTP 302).
- [ ] After logout, hitting a future protected route would not find `session["user_id"]` (verify via `session.get("user_id") is None` in a debug print or test).
- [ ] `login.html` uses `url_for('login')` in the form action — no hardcoded URLs remain.
- [ ] Navbar in `base.html` shows "Sign in / Get started" when logged out and "Profile / Log out" when logged in.
- [ ] `python app.py` starts without errors on port 5001; the registration flow from Step 2 still works end-to-end.
- [ ] Manual check in sqlite: logging in does not mutate the `users` table (row count and `password_hash` unchanged).
