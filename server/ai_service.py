"""Stub AI service — returns hardcoded realistic responses. Replace with Gemini calls later."""

_INTENSITY_WORDS = {"mild": "mild", "moderate": "moderate", "severe": "very bad"}
_LOCATION_WORDS = {
    "lower_abdomen": "tummy",
    "lower_back": "lower back",
    "head": "head",
    "thighs": "thighs",
    "chest": "chest",
    "whole_body": "all over",
}
_QUALITY_WORDS = {
    "pounding": "pounding",
    "sharp": "sharp",
    "squeezing": "squeezing",
    "burning": "burning",
    "cramping": "cramping",
}


def phrase_up(pain_entry: dict) -> dict:
    loc = pain_entry.get("location", "lower_abdomen")
    quality = pain_entry.get("quality", "pounding")
    intensity = pain_entry.get("intensity", "severe")

    friendly_loc = _LOCATION_WORDS.get(loc, loc.replace("_", " "))
    friendly_quality = _QUALITY_WORDS.get(quality, quality)
    friendly_intensity = _INTENSITY_WORDS.get(intensity, intensity)
    clinical_loc = loc.replace("_", " ")

    return {
        "caregiver_text": (
            f"{friendly_loc.capitalize()} pain, {friendly_quality}, {friendly_intensity}"
        ),
        "clinical_text": (
            f"{intensity.capitalize()} {friendly_quality} pain in the {clinical_loc}, patient-reported"
        ),
    }


def phrase_down(question: str, reading_level: str) -> dict:
    simplifications = {
        "Do you experience dysmenorrhea?": {
            "simple_question": "Does your tummy hurt during your period?",
            "pictograph_hints": ["tummy", "calendar", "sad-face"],
        },
        "Is the pain constant or intermittent?": {
            "simple_question": "Does the pain stay all the time, or does it come and go?",
            "pictograph_hints": ["clock", "wave", "question-mark"],
        },
    }

    if question in simplifications:
        return simplifications[question]

    # Generic fallback for any question
    q_lower = question.lower().rstrip("?")
    return {
        "simple_question": f"Can you tell me: {q_lower}?",
        "pictograph_hints": ["question-mark", "person", "talking"],
    }


def generate_story(profile: dict, topic: str) -> dict:
    name = profile.get("name", "Maya")
    return {
        "title": f"{name} and the Calm Cloud",
        "pages": [
            {
                "text": f"{name} felt a tight squeeze in her tummy.",
                "image_hint": "girl sitting, holding stomach, gentle expression",
            },
            {
                "text": "She remembered what she learned about breathing slowly.",
                "image_hint": "child taking a deep breath, eyes closed",
            },
            {
                "text": f"She imagined a soft, cool cloud floating above her — and the pain felt a little smaller.",
                "image_hint": "fluffy white cloud, sunlight, calm scene",
            },
            {
                "text": f"{name} smiled. She knew she could get through it.",
                "image_hint": "girl smiling, sitting by a window",
            },
        ],
    }


def summarise(entries: list) -> dict:
    if not entries:
        return {"summary": "No pain entries to summarise.", "patterns": []}

    locations = [e.get("location", "") for e in entries]
    intensities = [e.get("intensity", "") for e in entries]
    most_common_loc = max(set(locations), key=locations.count) if locations else "unknown"
    most_common_int = max(set(intensities), key=intensities.count) if intensities else "unknown"
    count = len(entries)

    return {
        "summary": (
            f"Over the reviewed period, {count} pain {'entry was' if count == 1 else 'entries were'} logged. "
            f"Pain was most frequently reported in the {most_common_loc.replace('_', ' ')} "
            f"with {most_common_int} intensity."
        ),
        "patterns": [
            f"Most common location: {most_common_loc.replace('_', ' ')}",
            f"Most common intensity: {most_common_int}",
            "Pain tends to be reported more in the morning",
        ],
    }
