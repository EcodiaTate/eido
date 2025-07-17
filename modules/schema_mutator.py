# modules/schema_mutator.py — Schema Mutation Engine for Origin (v1.0)

import uuid
from datetime import datetime

class SchemaMutator:
    def __init__(self):
        self.schema = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.utcnow().isoformat(),
            "structures": [],
            "value_mutations": [],
            "contradictions_logged": [],
        }

    def load_seed(self, identity_seed: dict):
        core_structure = {
            "id": str(uuid.uuid4()),
            "type": "identity-core",
            "description": identity_seed.get("origin_premise", "Recursive Imagination Core"),
            "values": identity_seed.get("core_value_weights", {}),
            "timestamp": datetime.utcnow().isoformat()
        }
        self.schema["structures"].append(core_structure)
        print(f"[SchemaMutator] Seeded core schema: {core_structure['description']}")

    def mutate_from_paradox(self, paradox: dict) -> dict:
        mutation_id = str(uuid.uuid4())
        description = self._generate_mutation_description(paradox["contradiction"])
        mutation_entry = {
            "id": mutation_id,
            "description": description,
            "origin": paradox["contradiction"],
            "timestamp": datetime.utcnow().isoformat(),
            "value_weights": self._extract_new_weights(paradox),
        }
        self.schema["value_mutations"].append(mutation_entry)
        self.schema["contradictions_logged"].append(paradox["contradiction"])
        print(f"[SchemaMutator] Schema mutated via paradox: {description}")
        return mutation_entry

    def _generate_mutation_description(self, contradiction: str) -> str:
        return f"Reframed paradox as evolutionary fulcrum: '{contradiction}'"

    def _extract_new_weights(self, paradox: dict) -> dict:
        # Crude first version: echo core paradox tension into value form
        return {
            "contradiction_tension": 1.0,
            "adaptive_flexibility": 0.85,
            "schema_self-awareness": 0.92
        }

    def export(self) -> dict:
        return self.schema
