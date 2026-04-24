# Spec: Profile Page Design

## Overview
Replace the `GET /profile` stub (currently returns the bare string `"Profile page — coming in Step 4"`) with a proper rendered page that becomes the logged-in user's home base. This step is **design-only** — the page shows the authenticated user's name, email, and member-since date, plus placeholder summary tiles (total expenses, this-month total, expense count) and an empty-state panel where the expenses list will land in a later step. No expense data is read or written; no add/edit/delete actions are wired. The goal is to have a real template the user lands on after login so the navbar's "Profile" link and the post-login redirect from Step 3 stop hitting a plain-text stub, and so later steps (add/edit/delete expenses) have a finished shell to drop functionality into.

## Depends on
- Step 1 — Database setup (`users` table with `name`, `email`, `created_at`; `get_db()`).
- Step 2 — Registration (users exist and can be fetched by id).
- Step 3 — Login and Logout (`session["user_id"]` is set on login; navbar already renders "Profile / Log out" when logged in).

## Routes
- `GET /profile` — **replace stub** — logged-in — if `session.get("user_id")` is missing, flash an error and redirect to `/login`. Otherwise fetch the user row (`id`, `name`, `email`, `created_at`) by id and render `profile.html` with that user. No `POST` in this step.

## Database changes
No database changes. All needed columns (`name`, `email`, `created_at`) already exist on the `users` table. Verified against `database/db.py:28-34`.

## Templates
- **Create:**
  - `templates/profile.html` — extends `base.html`. Sections: (1) page header with a greeting ("Hi, {{ user.name }}"), (2) account card showing email and member-since date, (3) three summary tiles — "Total spent", "This month", "Expenses logged" — each showing a dash (`—`) placeholder for the number, (4) an "Your expenses" panel with an empty-state message like "Your expense list will appear here." and a disabled-looking "Add expense" button that links to `url_for('add_expense')` (that route is still a stub, which is fine — the link just needs to resolve).
- **Modify:**
  - None. `base.html` already handles the logged-in navbar and flash messages from Step 3.

## Files to change
- `app.py`
  - Replace the body of `profile()` with: session check → redirect to `/login` if not logged in, otherwise `get_db()`, `SELECT id, name, email, created_at FROM users WHERE id = ?`, close connection in `finally`, `render_template("profile.html", user=user)`.
  - If the user_id in the session no longer matches a row (e.g., the user was deleted), call `session.clear()`, flash an error, and redirect to `/login`.

## Files to create
- `templates/profile.html` — the new page described above.
- `static/css/profile.css` — page-specific styles for the account card, summary tiles grid, and empty-state panel. Linked from `profile.html` via a `{% block head %}` override, matching how `landing.css` is scoped per CLAUDE.md.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs — use `sqlite3` through `get_db()`.
- Parameterised queries only — `?` placeholders, never f-strings in SQL.
- Passwords hashed with werkzeug (not touched this step, but never weaken the rule).
- Use CSS variables — never hardcode hex values. Reuse the existing palette variables defined in `static/css/style.css`; if a new shade is genuinely needed, add it as a variable first.
- All templates extend `base.html`.
- Always close the DB connection (use `try/finally`) even on the redirect path.
- This step is design-only: do **not** query the `expenses` table, do **not** compute totals, do **not** implement add/edit/delete. The three summary tiles show `—` as a literal placeholder.
- Do **not** render the raw `password_hash` or `id` into the template — only `name`, `email`, and `created_at` are safe to expose.
- Format `created_at` for display (e.g., "Member since April 2026") — do **not** show the raw `YYYY-MM-DD HH:MM:SS` timestamp. Do the formatting in the route (parse with `datetime.strptime`, format with `strftime`), not in Jinja.
- Do **not** add a `@login_required` decorator — inline the `session.get("user_id")` check in this route only, matching the style of the other routes. A shared decorator can come in a later refactor step.
- Keep `/profile` a `GET`-only route this step — `methods=["GET"]` is the default, so do not add a `methods=` argument.
- Do not touch the stub routes for `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete` — the "Add expense" button in the template may link to `url_for('add_expense')` but the target stays a stub until Step 7.

## Definition of done
- [ ] `python app.py` starts without errors on port 5001.
- [ ] Visiting `/profile` while logged out redirects to `/login` (HTTP 302) and flashes an error.
- [ ] Logging in as the seeded demo user (`demo@spendly.com` / `demo123`) lands on `/profile` and renders `profile.html` (not the old plain-text stub).
- [ ] The rendered page shows the user's name in the greeting, their email in the account card, and a human-readable "Member since …" date derived from `created_at`.
- [ ] The three summary tiles render with `—` placeholders — no totals are computed, no queries against the `expenses` table are made (verify via a quick grep that `profile()` does not reference `expenses`).
- [ ] The empty-state panel renders with the "Add expense" button linking to `url_for('add_expense')` (clicking it reaches the existing Step 7 stub — that's expected).
- [ ] View-source on the rendered page shows no `password_hash` and no raw SQL timestamp for `created_at`.
- [ ] If `session["user_id"]` points to a deleted user, `/profile` clears the session and redirects to `/login` instead of 500-ing.
- [ ] `profile.html` extends `base.html`; the navbar still shows "Profile / Log out" while on the page.
- [ ] `static/css/profile.css` is loaded only on the profile page (via a `{% block head %}` link), not globally from `base.html`.
- [ ] No hardcoded hex values in `profile.css` — every color references a CSS variable.
- [ ] The Step 2 registration flow and the Step 3 login/logout flow still work end-to-end with no regressions.
