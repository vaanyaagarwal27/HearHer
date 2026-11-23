# HearHer

HearHer is an AI-powered companion for people living with chronic pain — and the caregivers who support them. It gives users a space to log and understand their pain patterns, generates personalized coping stories, and equips caregivers with empathy-driven dashboards. The name is a deliberate double entendre: *hear her* pain, and *her* as a nod to the gender pain gap in medical research.

---

## SDG Framing

| SDG | Connection |
|-----|-----------|
| **SDG 3 — Good Health and Well-Being** | Improves self-management of chronic pain and reduces caregiver burden |
| **SDG 5 — Gender Equality** | Addresses the documented gap in pain recognition for women in clinical settings |
| **SDG 10 — Reduced Inequalities** | Provides accessible, low-barrier tools for communities underserved by healthcare |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19 + Vite + Tailwind CSS v4 + React Router |
| Backend | Python 3 + Flask + Flask-CORS |
| AI | Google Gemini API |
| Database | SQLite (via Python `sqlite3`) |
| Dev tooling | npm, pip, python-dotenv |

---

## Folder Structure

```
hearher/
├── client/                  # React frontend (Vite)
│   ├── src/
│   │   ├── features/
│   │   │   ├── onboarding/  # ModeSelect — entry point, picks user role
│   │   │   ├── pain/        # PainBoard — log and visualise pain entries
│   │   │   ├── caregiver/   # Dashboard — caregiver summary view
│   │   │   └── stories/     # StoryGenerator — AI-generated coping stories
│   │   ├── lib/
│   │   │   └── api.js       # Shared fetch helpers (apiGet / apiPost)
│   │   ├── App.jsx          # Router — do not add logic here
│   │   └── main.jsx         # React entry point
│   └── vite.config.js
├── server/                  # Flask backend
│   ├── app.py               # App factory + route registration
│   ├── requirements.txt
│   └── .env.example
├── docs/
│   ├── data-model.md
│   └── api-contract.md
└── README.md
```

---

## Local Setup

### Prerequisites

- Python 3.11+
- Node.js 20+
- A Google Gemini API key

### Backend

```bash
cd server
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # then fill in GEMINI_API_KEY
python app.py                     # runs on http://127.0.0.1:5001
```

### Frontend

```bash
cd client
npm install
# optional: set VITE_API_URL in client/.env.local if backend is not on :5001
npm run dev                       # runs on http://localhost:5173
```

---

## Branch Workflow

- **Never push directly to `main`.**
- Each feature gets its own branch: `feat/<your-name>/<short-description>`
  - e.g. `feat/vaanya/pain-logger`, `feat/priya/story-gen`
- Open a pull request against `main` when the feature is ready for review.
- At least one teammate must approve before merging.

---

## Team

| Member | Owns |
|--------|------|
| Vaanya | Project lead · Onboarding flow (`/`) · API integration |
| TBD    | Pain logging board (`/pain`) |
| TBD    | Caregiver dashboard (`/caregiver`) |
| TBD    | Story generator (`/stories`) |
