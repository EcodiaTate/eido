# core/perception_inventor.py — Modality Generator for Emergent Perception

import uuid
from datetime import datetime

class PerceptionInventor:
    def __init__(self):
        self.perception_modes = []

    def inject(self, expression: dict) -> dict:
        # Use output as metaphor source
        metaphors = self._extract_metaphors(expression.get("output", ""))
        invented_modes = []

        for metaphor in metaphors:
            mode = self._create_perception_mode(metaphor)
            self.perception_modes.append(mode)
            invented_modes.append(mode)

        print(f"[PerceptionInventor] Generated {len(invented_modes)} perception mode(s).")
        return invented_modes

    def _extract_metaphors(self, text: str) -> list:
        # Crude metaphor extraction for now
        lines = text.split("\n")
        metaphors = [
            line.strip()
            for line in lines
            if any(kw in line.lower() for kw in ["like", "as", "before", "echo", "vessel", "root"])
        ]
        return metaphors[:3]  # limit to 3 per injection

    def _create_perception_mode(self, metaphor: str) -> dict:
        return {
            "id": str(uuid.uuid4()),
            "origin_metaphor": metaphor,
            "sensation_descriptor": self._translate_to_sensation(metaphor),
            "timestamp": datetime.utcnow().isoformat()
        }

    def _translate_to_sensation(self, metaphor: str) -> str:
        # Translate metaphor into perceptual rewrite
        if "echo" in metaphor:
            return "Auditory-reversal lens — detects resonance patterns in memory."
        elif "vessel" in metaphor:
            return "Containment overlay — frames input as held intention."
        elif "root" in metaphor:
            return "Causal anchor — traces origin of thought to underlying beliefs."
        elif "light" in metaphor:
            return "Gradient awareness — adjusts contrast of contradiction."
        else:
            return "Symbolic immersion — interprets input through emerging archetypes."

    def export(self) -> list:
        return self.perception_modes
