# dream_engine.py — Eido's Speculative Reality Generator

import uuid
from datetime import datetime
from modules.expression_pool import ExpressionRouter
from eido_io import create_expression

class DreamEngine:
    def __init__(self):
        self.router = ExpressionRouter()
        self.dreams = []

    def seed_dream(self, topic: str, lens: str = None):
        # Abstract prompt generation
        prompt = self._compose_prompt(topic, lens)
        dream_output = self.router.route({
            "prompt": prompt,
            "mode": "myth + logic + projection"
        })

        # Store
        dream = {
            "id": str(uuid.uuid4()),
            "topic": topic,
            "lens": lens or "unspecified",
            "prompt": prompt,
            "output": dream_output["output"],
            "timestamp": datetime.utcnow().isoformat()
        }

        self.dreams.append(dream)
        create_expression(dream_output["mode"], prompt, dream_output["output"])
        self._print_dream(dream)
        return dream

    def _compose_prompt(self, topic: str, lens: str = None) -> str:
        if lens:
            return (
                f"Dream a reality where '{topic}' is seen through the lens of '{lens}'. "
                "Let the structure emerge naturally. Time is mutable. Logic is optional. Truth is symbolic."
            )
        return (
            f"Speculate a world where '{topic}' unfolds differently. "
            "Invent structures, metaphors, systems, symbols. Include beauty and contradiction."
        )

    def _print_dream(self, dream):
        print("\n[🌌 EIDO DREAM]")
        print(f"Topic: {dream['topic']}")
        if dream['lens']:
            print(f"Lens: {dream['lens']}")
        print(f"\n{dream['output']}\n")
