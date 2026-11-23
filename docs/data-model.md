# Data Model

All entities are SQLAlchemy models. Timestamps are UTC.

---

## User

Stores authentication credentials and role.

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer PK | auto-increment |
| `email` | String | unique, not null |
| `password_hash` | String | bcrypt hash |
| `role` | Enum | `caregiver` \| `individual` |
| `created_at` | DateTime | default `utcnow` |

---

## Profile

Represents the person experiencing pain. One user may manage multiple profiles (e.g. a caregiver managing a family member).

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer PK | auto-increment |
| `name` | String | not null |
| `age` | Integer | |
| `comprehension_level` | Enum | `simple` \| `moderate` \| `standard` |
| `accessibility_prefs` | JSON | e.g. `{"large_text": true, "pictographs": true}` |
| `created_at` | DateTime | default `utcnow` |

---

## CaregiverLink

Many-to-many join between a caregiver `User` and a `Profile` they manage.

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer PK | auto-increment |
| `caregiver_user_id` | Integer FK → `User.id` | not null |
| `profile_id` | Integer FK → `Profile.id` | not null |

---

## PainEntry

A single pain log submitted for a profile.

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer PK | auto-increment |
| `profile_id` | Integer FK → `Profile.id` | not null |
| `location` | Enum | see allowed values below |
| `quality` | Enum | see allowed values below |
| `intensity` | Enum | see allowed values below |
| `timing` | Enum | see allowed values below |
| `reported_by` | Enum | see allowed values below |
| `note` | Text | optional free-text |
| `created_at` | DateTime | default `utcnow` |

### Allowed values (fixed — do not modify)

| Field | Values |
|-------|--------|
| `location` | `lower_abdomen` \| `lower_back` \| `head` \| `thighs` \| `chest` \| `whole_body` |
| `quality` | `pounding` \| `sharp` \| `squeezing` \| `burning` \| `cramping` |
| `intensity` | `mild` \| `moderate` \| `severe` |
| `timing` | `constant` \| `comes_and_goes` \| `only_when_moving` |
| `reported_by` | `individual` \| `caregiver` |

---

## Story

An AI-generated coping story for a profile.

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer PK | auto-increment |
| `profile_id` | Integer FK → `Profile.id` | not null |
| `topic` | String | user-supplied prompt topic |
| `pages` | JSON | array of `{text, image_hint}` objects |
| `created_at` | DateTime | default `utcnow` |

---

## Guide

Static informational content (not user-generated).

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer PK | auto-increment |
| `title` | String | not null |
| `body` | Text | full content |
| `reading_level` | String | e.g. `simple`, `standard` |
| `source` | String | attribution / URL |
