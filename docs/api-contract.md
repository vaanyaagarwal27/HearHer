# API Contract

Base URL: `http://127.0.0.1:5001` (dev) · set `VITE_API_URL` in `client/.env.local` to override.

Protected routes require the header:
```
Authorization: Bearer <token>
```

---

## Auth

### `POST /api/auth/register`

Create a new account.

**Request**
```json
{ "email": "user@example.com", "password": "secret", "role": "individual" }
```

**Response `201`**
```json
{ "token": "<jwt>", "user": { "id": 1, "email": "user@example.com", "role": "individual" } }
```

---

### `POST /api/auth/login`

Exchange credentials for a token.

**Request**
```json
{ "email": "user@example.com", "password": "secret" }
```

**Response `200`**
```json
{ "token": "<jwt>", "user": { "id": 1, "email": "user@example.com", "role": "individual" } }
```

---

## Profiles

### `GET /api/profiles` 🔒

Returns all profiles accessible to the authenticated user (own profile, or profiles linked via `CaregiverLink`).

**Response `200`**
```json
[
  { "id": 1, "name": "Priya", "age": 28, "comprehension_level": "standard", "accessibility_prefs": {}, "created_at": "2026-11-23T10:00:00Z" }
]
```

---

### `POST /api/profiles` 🔒

Create a new profile.

**Request**
```json
{ "name": "Priya", "age": 28, "comprehension_level": "standard" }
```

**Response `201`**
```json
{ "id": 1, "name": "Priya", "age": 28, "comprehension_level": "standard", "accessibility_prefs": {}, "created_at": "2026-11-23T10:00:00Z" }
```

---

## Pain Entries

### `POST /api/pain` 🔒

Log a new pain entry.

**Request**
```json
{
  "profile_id": 1,
  "location": "lower_abdomen",
  "quality": "cramping",
  "intensity": "moderate",
  "timing": "comes_and_goes",
  "reported_by": "individual"
}
```

**Response `201`**
```json
{
  "id": 42,
  "profile_id": 1,
  "location": "lower_abdomen",
  "quality": "cramping",
  "intensity": "moderate",
  "timing": "comes_and_goes",
  "reported_by": "individual",
  "note": null,
  "created_at": "2026-11-23T10:05:00Z"
}
```

---

### `GET /api/pain?profile_id=<id>` 🔒

Fetch all pain entries for a profile, newest first.

**Response `200`**
```json
[ { ...PainEntry }, { ...PainEntry } ]
```

---

## AI Endpoints

All AI endpoints are protected and call the Gemini API server-side.

---

### `POST /api/ai/phrase-up` 🔒

Translate a pain entry into language suitable for a caregiver or clinician.

**Request**
```json
{ "pain_entry": { ...PainEntry } }
```

**Response `200`**
```json
{
  "caregiver_text": "She's experiencing moderate cramping in her lower abdomen that comes and goes.",
  "clinical_text": "Patient reports intermittent, moderate-intensity cramping localised to the lower abdomen."
}
```

---

### `POST /api/ai/phrase-down` 🔒

Simplify a clinical or complex question for a user with a lower comprehension level.

**Request**
```json
{ "question": "Do you experience dysmenorrhea?", "reading_level": "simple" }
```

**Response `200`**
```json
{
  "simple_question": "Does your tummy hurt when you have your period?",
  "pictograph_hints": ["tummy", "calendar", "sad-face"]
}
```

---

### `POST /api/ai/story` 🔒

Generate a personalized coping story for a profile.

**Request**
```json
{ "profile": { ...Profile }, "topic": "breathing through the pain" }
```

**Response `200`**
```json
{
  "title": "Maya and the Calm Cloud",
  "pages": [
    { "text": "Maya felt a tight squeeze in her tummy.", "image_hint": "girl holding stomach" },
    { "text": "She took a big breath and imagined a soft cloud.", "image_hint": "child breathing, fluffy cloud" }
  ]
}
```

---

### `POST /api/ai/summarise` 🔒

Summarise a list of pain entries and surface patterns.

**Request**
```json
{ "entries": [ { ...PainEntry }, { ...PainEntry } ] }
```

**Response `200`**
```json
{
  "summary": "Over the past 7 days, pain was most frequently reported in the lower abdomen with cramping quality.",
  "patterns": ["pain peaks mid-cycle", "intensity higher in the morning", "mostly comes and goes"]
}
```

---

## Error Format

All errors follow the same shape:

```json
{ "error": "Human-readable message", "code": "MACHINE_READABLE_CODE" }
```

| HTTP status | Meaning |
|-------------|---------|
| `400` | Validation error / bad request body |
| `401` | Missing or invalid token |
| `403` | Authenticated but not authorised for this resource |
| `404` | Resource not found |
| `500` | Server / AI error |
