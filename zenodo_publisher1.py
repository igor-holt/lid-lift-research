import requests
import json
import os
import sys

# CONFIGURATION
# Best Practice: Load from environment variable to keep your token safe.
ACCESS_TOKEN = os.environ.get('ZENODO_TOKEN')

# URL SELECTION
# Use 'sandbox.zenodo.org' for testing, 'zenodo.org' for production.
BASE_URL = "https://zenodo.org/api"
HEADERS = {"Content-Type": "application/json"}
PARAMS = {'access_token': ACCESS_TOKEN}

# YOUR IDENTITY
# This format triggers the DataCite -> ORCID auto-sync
AUTHOR_NAME = "Holt, Igor"
AUTHOR_ORCID = "0009-0008-8389-1297"

# PAPER 1 DOI ID (Reserved ID)
PAPER_1_ID = "17784144"

# METADATA DEFINITIONS
papers = [
    {
        "id": PAPER_1_ID,
        "file": "Beyond Retry_ A Metacognitive Dynamics Framework for Autonomous Agent Failure Recovery.md",
        "metadata": {
            "title": "Beyond Retry: A Metacognitive Dynamics Framework for Autonomous Agent Failure Recovery",
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": "[LID-LIFT Technical Series: Paper 1 of 3]<br><br>ABSTRACT:<br>Autonomous agents frequently encounter 'cognitive deadlocks'—states where iterative retries fail to resolve a task due to strict constraints, missing tools, or context overflow. Traditional error handling (try/catch loops) exacerbates token waste in these scenarios. This paper introduces the LID-LIFT Protocol, a metacognitive failure-recovery framework. Unlike standard error correction, LID-LIFT triggers a four-stage dynamic: (1) Objective Abstraction, (2) Tool Broadening, (3) Solution Diversification, and (4) Context Re-packing. We demonstrate that this method statistically improves success rates in 'impossible' scenarios by shifting the agent’s operating plane rather than forcing execution on a blocked path.<br><br>TECHNICAL KEYWORDS:<br>Agentic AI, Large Language Models (LLM), Metacognition, Control Theory, Failure Recovery, Autonomous Orchestration, System Architecture.",
            "creators": [{
                "name": AUTHOR_NAME,
                "affiliation": "Independent Researcher",
                "orcid": AUTHOR_ORCID
            }],
            "keywords": ["Agentic AI", "Metacognition", "LID-LIFT"]
        }
    },
    {
        "id": None,
        "file": "The Landauer Context_ A Physics-Grounded Energy Basis for Large Language Model Orchestration.md",
        "metadata": {
            "title": "The Landauer Context: A Physics-Grounded Energy Basis for Large Language Model Orchestration",
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": "[LID-LIFT Technical Series: Paper 2 of 3]<br><br>ABSTRACT:<br>As Large Language Model (LLM) agents approach autonomy, their energy consumption becomes a critical limiting factor. Current 'Green AI' metrics rely on fluctuating estimates of kilowatt-hours (kWh) or carbon intensity, which fail to provide a stable baseline for algorithmic efficiency. This paper proposes the Landauer Context, a reporting framework that normalizes agentic energy expenditure against the theoretical Landauer limit (kT ln 2). We introduce the Thermodynamic Efficiency Ratio (eta_therm) as a standardized metric for the LID-LIFT Orchestrator, allowing for precise arbitration between high-accuracy/high-energy models and heuristic approximations based on fundamental physical limits.<br><br>TECHNICAL KEYWORDS:<br>Green AI, Sustainable Computing, Landauer Limit, Thermodynamics, LLM Efficiency, Energy Metrics, Super Learner Arbitration.",
            "creators": [{
                "name": AUTHOR_NAME,
                "affiliation": "Independent Researcher",
                "orcid": AUTHOR_ORCID
            }],
            "keywords": ["Green AI", "Landauer Limit", "Thermodynamics"]
        }
    },
    {
        "id": None,
        "file": "Dissonance-Weighted Eviction_ A Hybrid LRU Protocol for Long-Horizon Agent Memory.md",
        "metadata": {
            "title": "Dissonance-Weighted Eviction: A Hybrid LRU Protocol for Long-Horizon Agent Memory",
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": "[LID-LIFT Technical Series: Paper 3 of 3]<br><br>ABSTRACT:<br>Long-horizon autonomous agents suffer from 'context drift'—the accumulation of contradictory or obsolete information within the sliding context window. Traditional Least Recently Used (LRU) policies preserve data based on temporal recency, regardless of its semantic validity. This paper introduces Dissonance-Weighted Eviction (DWE), a core component of the HMIC-PPT Memory Model. By multiplying temporal decay with a 'Semantic Dissonance' coefficient (derived from entailment scoring against the active plan), DWE proactively purges conflicting data. We demonstrate that this hybrid policy significantly reduces 'agent schizophrenia' (the oscillating behavior between two contradictory instructions) in constraints-heavy environments.<br><br>TECHNICAL KEYWORDS:<br>RAG, Vector Databases, Context Window Management, Hallucination, Memory Hygiene, Semantic Search, LRU Algorithms.",
            "creators": [{
                "name": AUTHOR_NAME,
                "affiliation": "Independent Researcher",
                "orcid": AUTHOR_ORCID
            }],
            "keywords": ["RAG", "Vector Databases", "Memory Hygiene"]
        }
    }
]

def upload_file(deposition_id, file_path):
    print(f"Uploading {file_path} to {deposition_id}...")
    try:
        with open(file_path, 'rb') as fp:
            files = {'file': fp}
            r = requests.post(
                f'{BASE_URL}/deposit/depositions/{deposition_id}/files',
                params=PARAMS,
                files=files
            )
        return r.status_code
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found in current directory.")
        return 404

def create_deposit(metadata):
    print(f"Creating new deposit for: {metadata['title']}")
    data = {'metadata': metadata}
    r = requests.post(
        f'{BASE_URL}/deposit/depositions',
        params=PARAMS,
        json=data,
        headers=HEADERS
    )
    if r.status_code != 201:
        print(f"❌ Error creating deposit: {r.text}")
        return None
    return r.json()['id']

def update_deposit(dep_id, metadata):
    print(f"Updating deposit {dep_id}...")
    data = {'metadata': metadata}
    r = requests.put(
        f'{BASE_URL}/deposit/depositions/{dep_id}',
        params=PARAMS,
        json=data,
        headers=HEADERS
    )
    if r.status_code != 200:
         print(f"❌ Error updating deposit: {r.text}")
    return r.status_code

def main():
    if not ACCESS_TOKEN:
        print("❌ Error: ZENODO_TOKEN environment variable not set.")
        print("Run locally with: export ZENODO_TOKEN='your_token' && python zenodo_publisher.py")
        sys.exit(1)

    print("--- LID-LIFT Publication Pipeline ---")
    print(f"Author: {AUTHOR_NAME} ({AUTHOR_ORCID})")

    for p in papers:
        dep_id = p.get('id')

        # 1. Update or Create Draft
        if dep_id:
            update_deposit(dep_id, p['metadata'])
        else:
            dep_id = create_deposit(p['metadata'])
            if not dep_id: continue

        # 2. Upload File
        if os.path.exists(p['file']):
            upload_file(dep_id, p['file'])
        else:
            print(f"⚠️ File {p['file']} not found. Skipping upload.")
            continue

        # 3. Output Link
        print(f"✅ Draft Ready: {BASE_URL.replace('/api', '')}/deposit/{dep_id}")

    print("\nNOTE: Ensure 'ORCID Auto-Update' is enabled in DataCite Profiles.")

if __name__ == "__main__":
    main()