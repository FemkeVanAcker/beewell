# BeeWell

**BeeWell** is a calm, modular wellbeing web app for adults with ADHD, autism or other forms of neurodivergence.

Instead of juggling five separate apps, BeeWell brings medication tracking, a mood journal, overstimulation logging, breathing exercises, gentle nudges, notes, focus tools, household chores and routines into one place. You choose which modules you want, and the rest stays out of sight. A calm mode turns off all animations, and nothing punishes you for a missed day. Buzz the bee cheers you on instead.

> 🚧 **Status:** in development. A clickable frontend concept of all screens exists; the app is now being rebuilt with a real database and user accounts.

## Modules

Every module is optional. On first use, BeeWell asks which ones you want, and you can switch them on or off at any time. Switched-off modules disappear from the menu and dashboard, but their data is kept.

| Module              | What it does                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| **Dashboard**       | A honeycomb overview of your active modules, what's up next and today's mood                           |
| **Medication**      | Check off doses, see your history in a calendar, add medications with times                            |
| **Journal**         | Daily mood check-in, notes and wins, mood chart, export to CSV                                         |
| **Overstimulation** | Log episodes with intensity and triggers, see patterns, and a 5-4-3-2-1 grounding exercise             |
| **Breathing**       | Guided breathing exercises with a calm orb that grows as you breathe in and shrinks as you breathe out |
| **Nudges**          | Gentle reminders to drink water, stretch or take a break                                               |
| **Notes**           | Quick lists you can swipe to tick off or delete                                                        |
| **Focus**           | Break tasks into subtasks and work with a pomodoro timer                                               |
| **Household**       | Budget overview and a weekly chore grid                                                                |
| **Routines**        | Long-term recurring tasks (dentist, car check-up) coloured by urgency                                  |

### Design principles

- **One app, but modular:** only see what you turned on.
- **Calm by default:** a calm mode switches off every animation and decoration with one click.
- **Gentle, not punishing:** no lost points or broken streaks.
- **Your data stays yours:** hosted in the EU, no ads or tracking, export your own data.

## Tech stack

| Layer                 | Choice                          | Why                                                                                                                                                                                    |
| --------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Language              | Python 3.13                     | One language for the interface, the logic and the database layer                                                                                                                       |
| Frontend + web server | NiceGUI (on FastAPI)            | UI written in Python; a live websocket connection makes timers, live charts, the breathing orb and instant updates simple. FastAPI underneath allows a REST API for a mobile app later |
| ORM                   | SQLAlchemy 2.x                  | Works with any framework and supports async code, which NiceGUI uses                                                                                                                   |
| Migrations            | Alembic                         | Database changes are versioned and applied the same way everywhere                                                                                                                     |
| Database              | PostgreSQL (psycopg 3)          | Reliable relational database that handles multiple users; available on the host                                                                                                        |
| Validation / config   | Pydantic v2 + pydantic-settings | Checks input before it reaches the database; reads secrets from `.env`                                                                                                                 |
| Password hashing      | argon2-cffi (Argon2id)          | Current recommended password hashing algorithm                                                                                                                                         |
| Logging               | Loguru                          | Simple to use (no logger setup per module); library logs are routed through it too                                                                                                     |
| Charts                | ECharts (built into NiceGUI)    | Interactive charts without writing JavaScript                                                                                                                                          |
| Tests                 | pytest + NiceGUI `User` fixture | Tests services and pages without a browser                                                                                                                                             |
| Package manager       | uv                              | Locked, reproducible installs via `pyproject.toml` + `uv.lock`                                                                                                                         |
| Hosting               | Railway (EU West)               | Supports long-running servers with websockets (needed for NiceGUI); EU hosting for health data                                                                                         |

## Getting started

### Requirements

- [uv](https://docs.astral.sh/uv/) (installs the right Python version for you)
- PostgreSQL running locally

### Tests

```bash
uv run pytest
```

## Project structure (planned)

```
src/beewell/
├── main.py            # app entry point
├── config.py          # settings from .env
├── logging_config.py  # Loguru setup
├── db.py              # database engine and session
├── models/            # what is stored (SQLAlchemy)
├── schemas/           # what input is allowed (Pydantic)
├── services/          # what happens (business logic, no UI code)
├── pages/             # what you see (NiceGUI)
├── ui/                # theme and shared components
└── static/            # images, fonts, Buzz
alembic/               # database migrations
tests/                 # mirrors the code folders
```

Imports only point downward: `pages → services → models/schemas → db/config`.

## Privacy

BeeWell stores sensitive health data (GDPR article 9). Passwords are hashed with Argon2id, secrets live in `.env` and are never committed, and logs only contain IDs and actions, never health data or passwords.

> BeeWell is a self-tracking tool, not a medical device, and does not give medical advice.
