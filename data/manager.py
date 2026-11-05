"""
Ma'lumotlar boshqaruvchisi (Data Manager)
A1 dan C1 gacha bo'lgan barcha Duden grammatika mavzularini birlashtiradi va qidiruvni ta'minlaydi.
"""
import random
from typing import List, Dict, Optional
from data.a1 import A1_TOPICS
from data.a2 import A2_TOPICS
from data.b1 import B1_TOPICS
from data.b2 import B2_TOPICS
from data.c1 import C1_TOPICS

ALL_TOPICS = A1_TOPICS + A2_TOPICS + B1_TOPICS + B2_TOPICS + C1_TOPICS
TOPICS_BY_ID = {t["id"]: t for t in ALL_TOPICS}


def get_topics_by_level(level: str) -> List[Dict]:
    """Berilgan darajadagi (A1, A2, B1, B2, C1) barcha mavzularni qaytaradi."""
    level = level.upper()
    return [t for t in ALL_TOPICS if t.get("level") == level]


def get_topic_by_id(topic_id: str) -> Optional[Dict]:
    """ID bo'yicha mavzuni topib beradi."""
    return TOPICS_BY_ID.get(topic_id)


def search_topics(query: str) -> List[Dict]:
    """
    Foydalanuvchi yozgan so'z bo'yicha (masalan 'akkusativ', 'perfekt', 'weil', 'artikl')
    tegishli mavzularni topadi.
    """
    q = query.lower().strip()
    if not q:
        return []

    matched = []
    for topic in ALL_TOPICS:
        score = 0
        title_lower = topic["title"].lower()
        keywords_lower = [k.lower() for k in topic.get("keywords", [])]

        # Aniq keyword mosligi
        for kw in keywords_lower:
            if q == kw:
                score += 15
            elif q in kw or kw in q:
                score += 8

        # Sarlavhada qidirish
        if q in title_lower:
            score += 10

        # Kontentda qidirish
        if q in topic.get("content", "").lower():
            score += 3

        if score > 0:
            matched.append((score, topic))

    # Eng mos kelganlarini tartiblaymiz
    matched.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in matched[:8]]


def get_random_quiz() -> Optional[Dict]:
    """Tasodifiy bitta mavzudan test savolini tanlab beradi."""
    all_quizzes = []
    for topic in ALL_TOPICS:
        for q in topic.get("quizzes", []):
            all_quizzes.append({
                "topic_id": topic["id"],
                "topic_title": topic["title"],
                "quiz": q
            })
    if not all_quizzes:
        return None
    return random.choice(all_quizzes)
