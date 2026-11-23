from flask import Blueprint, jsonify, request

import ai_service

ai_bp = Blueprint("ai", __name__, url_prefix="/api/ai")


@ai_bp.route("/phrase-up", methods=["POST"])
def phrase_up():
    body = request.get_json(force=True)
    pain_entry = body.get("pain_entry", {})
    return jsonify(ai_service.phrase_up(pain_entry))


@ai_bp.route("/phrase-down", methods=["POST"])
def phrase_down():
    body = request.get_json(force=True)
    question = body.get("question", "")
    reading_level = body.get("reading_level", "simple")
    return jsonify(ai_service.phrase_down(question, reading_level))


@ai_bp.route("/story", methods=["POST"])
def story():
    body = request.get_json(force=True)
    profile = body.get("profile", {})
    topic = body.get("topic", "")
    return jsonify(ai_service.generate_story(profile, topic))


@ai_bp.route("/summarise", methods=["POST"])
def summarise():
    body = request.get_json(force=True)
    entries = body.get("entries", [])
    return jsonify(ai_service.summarise(entries))
