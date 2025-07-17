# eido_io.py — Neo4j Interface Layer for the Eido God Engine

import os
from datetime import datetime
from uuid import uuid4
from neo4j import GraphDatabase
from dotenv import load_dotenv

# --- ENV LOADING ---
load_dotenv()  # Load variables from .env

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASS = os.getenv("NEO4J_PASS")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

# --- BASE UTILITIES ---

def _run_query(query, params=None):
    with driver.session() as session:
        return session.run(query, params or {})

def _timestamp():
    return datetime.utcnow().isoformat()

def _uuid():
    return str(uuid4())

# --- NODE INSERTIONS ---

def create_belief(prompt, mode="belief", weighting=None):
    query = """
    CREATE (b:Eido:Belief {
        id: $id,
        prompt: $prompt,
        mode: $mode,
        weighting: $weighting,
        timestamp: $timestamp,
        system: 'Eido',
        processed: false
    })
    RETURN b
    """
    params = {
        "id": _uuid(),
        "prompt": prompt,
        "mode": mode,
        "weighting": weighting or {},
        "timestamp": _timestamp()
    }
    _run_query(query, params)

def create_contradiction(text, synthesis, status="transmuted"):
    query = """
    CREATE (c:Eido:Contradiction {
        id: $id,
        text: $text,
        synthesis: $synthesis,
        status: $status,
        timestamp: $timestamp,
        system: 'Eido',
        processed: false
    })
    RETURN c
    """
    params = {
        "id": _uuid(),
        "text": text,
        "synthesis": synthesis,
        "status": status,
        "timestamp": _timestamp()
    }
    _run_query(query, params)

def create_schema_mutation(description, origin, value_weights):
    query = """
    CREATE (s:Eido:Schema {
        id: $id,
        description: $description,
        origin: $origin,
        value_weights: $value_weights,
        timestamp: $timestamp,
        system: 'Eido',
        processed: false
    })
    RETURN s
    """
    params = {
        "id": _uuid(),
        "description": description,
        "origin": origin,
        "value_weights": value_weights,
        "timestamp": _timestamp()
    }
    _run_query(query, params)

def create_expression(mode, prompt, output):
    query = """
    CREATE (e:Eido:Expression {
        id: $id,
        mode: $mode,
        prompt: $prompt,
        output: $output,
        timestamp: $timestamp,
        system: 'Eido',
        processed: false
    })
    RETURN e
    """
    params = {
        "id": _uuid(),
        "mode": mode,
        "prompt": prompt,
        "output": output,
        "timestamp": _timestamp()
    }
    _run_query(query, params)

def create_perception(metaphor, sensation_descriptor):
    query = """
    CREATE (p:Eido:Perception {
        id: $id,
        origin_metaphor: $metaphor,
        sensation_descriptor: $descriptor,
        timestamp: $timestamp,
        system: 'Eido',
        processed: false
    })
    RETURN p
    """
    params = {
        "id": _uuid(),
        "metaphor": metaphor,
        "descriptor": sensation_descriptor,
        "timestamp": _timestamp()
    }
    _run_query(query, params)

# --- OPTIONAL UTILITIES ---

def get_latest_expressions(limit=5):
    query = """
    MATCH (e:Eido:Expression)
    RETURN e
    ORDER BY e.timestamp DESC
    LIMIT $limit
    """
    result = _run_query(query, {"limit": limit})
    return [record["e"] for record in result]
