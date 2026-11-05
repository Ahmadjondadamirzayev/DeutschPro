"""
Interaktiv Test va Xatolarni To'g'rilash Sessiyasi Boshqaruvchisi
Duden mavzulari, Goethe-Institut (A1-C2) va Lug'at (Vocabulary) testlarini qo'llab-quvvatlaydi.
"""
import random
from typing import Dict, List, Optional, Tuple
from data.manager import get_topic_by_id, ALL_TOPICS
from data.goethe import get_goethe_tests_by_level, GOETHE_TESTS
from data.vocabulary import generate_vocab_quiz, get_words_by_level

USER_SESSIONS: Dict[int, dict] = {}


def prepare_question(quiz_data: dict) -> dict:
    options = list(quiz_data["options"])
    correct_idx = quiz_data["correct_index"]
    correct_text = options[correct_idx]
    wrong_explanations = quiz_data.get("wrong_explanations", {})

    items = []
    for i, opt in enumerate(options):
        items.append({
            "text": opt,
            "is_correct": (i == correct_idx),
            "wrong_reason": wrong_explanations.get(i, "❌ Tanlangan variant ushbu qoidaga to'g'ri kelmaydi.")
        })

    random.shuffle(items)

    new_options = [it["text"] for it in items]
    new_correct_idx = next(i for i, it in enumerate(items) if it["is_correct"])
    new_wrong_explanations = {
        i: it["wrong_reason"] for i, it in enumerate(items) if not it["is_correct"]
    }

    return {
        "id": quiz_data.get("id"),
        "question": quiz_data["question"],
        "options": new_options,
        "correct_index": new_correct_idx,
        "proof": quiz_data["proof"],
        "wrong_explanations": new_wrong_explanations,
        "original_quiz": quiz_data,
        "exam_name": quiz_data.get("exam_name"),
        "part": quiz_data.get("part")
    }


def start_topic_quiz(user_id: int, topic_id: str, count: int = 3) -> Optional[dict]:
    topic = get_topic_by_id(topic_id)
    if not topic:
        return None

    raw_quizzes = list(topic.get("quizzes", []))
    if not raw_quizzes:
        return None

    random.shuffle(raw_quizzes)
    selected_quizzes = raw_quizzes[:min(count, len(raw_quizzes))]
    prepared_questions = [prepare_question(q) for q in selected_quizzes]

    session = {
        "mode": "topic",
        "topic_id": topic_id,
        "topic_title": topic["title"],
        "level": topic["level"],
        "questions": prepared_questions,
        "current_idx": 0,
        "correct_count": 0,
        "mistakes": [],
        "answers_history": [],
        "is_fixing_mistakes": False
    }

    USER_SESSIONS[user_id] = session
    return session


def start_random_quiz(user_id: int, count: int = 5) -> Optional[dict]:
    all_raw = []
    for t in ALL_TOPICS:
        for q in t.get("quizzes", []):
            all_raw.append((t, q))

    if not all_raw:
        return None

    random.shuffle(all_raw)
    selected = all_raw[:min(count, len(all_raw))]

    prepared_questions = []
    for t, q in selected:
        pq = prepare_question(q)
        pq["topic_title"] = t["title"]
        prepared_questions.append(pq)

    session = {
        "mode": "random",
        "topic_id": "random",
        "topic_title": "Aralash Test (A1-C1)",
        "level": "Mix",
        "questions": prepared_questions,
        "current_idx": 0,
        "correct_count": 0,
        "mistakes": [],
        "answers_history": [],
        "is_fixing_mistakes": False
    }

    USER_SESSIONS[user_id] = session
    return session


def start_goethe_quiz(user_id: int, level: str, count: int = 4) -> Optional[dict]:
    level_clean = level.upper()
    raw_quizzes = list(get_goethe_tests_by_level(level_clean))
    if not raw_quizzes:
        return None

    random.shuffle(raw_quizzes)
    selected = raw_quizzes[:min(count, len(raw_quizzes))]
    prepared = [prepare_question(q) for q in selected]

    session = {
        "mode": "goethe",
        "topic_id": f"goethe_{level_clean}",
        "topic_title": f"Goethe-Zertifikat {level_clean} Imtihon Testi",
        "level": level_clean,
        "questions": prepared,
        "current_idx": 0,
        "correct_count": 0,
        "mistakes": [],
        "answers_history": [],
        "is_fixing_mistakes": False
    }

    USER_SESSIONS[user_id] = session
    return session


def start_goethe_einstufung(user_id: int) -> Optional[dict]:
    selected = []
    for lvl in ["A1", "A2", "B1", "B2", "C1", "C2"]:
        tests = get_goethe_tests_by_level(lvl)
        if tests:
            t = random.choice(tests)
            selected.append(t)

    prepared = [prepare_question(q) for q in selected]
    session = {
        "mode": "goethe_einstufung",
        "topic_id": "goethe_einstufung",
        "topic_title": "Goethe Daraja Aniqlovchi Imtihon (A1 - C2)",
        "level": "A1-C2",
        "questions": prepared,
        "current_idx": 0,
        "correct_count": 0,
        "mistakes": [],
        "answers_history": [],
        "is_fixing_mistakes": False
    }

    USER_SESSIONS[user_id] = session
    return session


def start_vocab_quiz(user_id: int, level: str = "A1", count: int = 5) -> Optional[dict]:
    """So'z boyligi bo'yicha interaktiv test sessiyasi"""
    level_clean = level.upper()
    quizzes = []
    for _ in range(count):
        q = generate_vocab_quiz(level_clean)
        quizzes.append(prepare_question(q))

    session = {
        "mode": "vocab",
        "topic_id": f"vocab_{level_clean}",
        "topic_title": f"{level_clean} Lug'at & So'z Boyligi Testi",
        "level": level_clean,
        "questions": quizzes,
        "current_idx": 0,
        "correct_count": 0,
        "mistakes": [],
        "answers_history": [],
        "is_fixing_mistakes": False
    }
    USER_SESSIONS[user_id] = session
    return session


def start_fixing_mistakes(user_id: int) -> Optional[dict]:
    session = USER_SESSIONS.get(user_id)
    if not session or not session.get("mistakes"):
        return None

    old_mistakes = session["mistakes"]
    prepared_mistakes = [prepare_question(m["original_quiz"]) for m in old_mistakes]

    fix_session = {
        "mode": session.get("mode", "topic"),
        "topic_id": session.get("topic_id", ""),
        "topic_title": session.get("topic_title", ""),
        "level": session.get("level", "A1"),
        "questions": prepared_mistakes,
        "current_idx": 0,
        "correct_count": 0,
        "mistakes": [],
        "answers_history": [],
        "is_fixing_mistakes": True,
        "initial_mistakes_count": len(prepared_mistakes)
    }

    USER_SESSIONS[user_id] = fix_session
    return fix_session


def get_current_session(user_id: int) -> Optional[dict]:
    return USER_SESSIONS.get(user_id)


def record_answer(user_id: int, chosen_opt: int) -> Optional[dict]:
    session = USER_SESSIONS.get(user_id)
    if not session:
        return None

    idx = session["current_idx"]
    questions = session["questions"]
    if idx >= len(questions):
        return None

    q = questions[idx]
    is_correct = (chosen_opt == q["correct_index"])

    if is_correct:
        session["correct_count"] += 1
    else:
        session["mistakes"].append(q)

    session["answers_history"].append({
        "question": q["question"],
        "chosen_opt": chosen_opt,
        "is_correct": is_correct
    })

    wrong_reason = ""
    if not is_correct:
        wrong_reason = q.get("wrong_explanations", {}).get(
            chosen_opt,
            "❌ Siz tanlagan javob to'g'ri emas."
        )

    is_last = (idx + 1 >= len(questions))

    return {
        "is_correct": is_correct,
        "question_text": q["question"],
        "proof": q["proof"],
        "wrong_reason": wrong_reason,
        "current_idx": idx,
        "total": len(questions),
        "is_last": is_last,
        "is_fixing_mistakes": session.get("is_fixing_mistakes", False)
    }


def advance_question(user_id: int) -> bool:
    session = USER_SESSIONS.get(user_id)
    if not session:
        return False
    session["current_idx"] += 1
    return session["current_idx"] < len(session["questions"])
