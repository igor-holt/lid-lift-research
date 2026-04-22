import requests
import json
import os
import sys

# --- 1. ACCESS CONFIGURATION ---
ACCESS_TOKEN = os.environ.get('ZENODO_TOKEN')

# --- 2. FILE NAME CONFIGURATION (CRITICAL: MATCH YOUR LOCAL FILES) ---
# Check your folder. Ensure these match your actual filenames exactly.
FILE_1_NAME = "Beyond Retry_ A Metacognitive Dynamics Framework for Autonomous Agent Failure Recovery.md"
FILE_2_NAME = "The Landauer Context_ A Physics-Grounded Energy Basis for Large Language Model Orchestration.md"
FILE_3_NAME = "Dissonance-Weighted Eviction_ A Hybrid LRU Protocol for Long-Horizon Agent Memory.md"
FILE_4_NAME = "mcp-tool-dissonance-v1.0.0-podman.zip"

# --- 3. IDENTITY & DOI CONFIGURATION ---
AUTHOR_NAME = "Holt, Igor"
AUTHOR_ORCID = "0009-0008-8389-1297"

PAPER_1_ID = "17784144"
PAPER_2_ID = "17784836"
PAPER_3_ID = "17784838"

# --- SYSTEM CONFIGURATION ---
BASE_URL = "https://zenodo.org/api"
HEADERS = {"Content-Type": "application/json"}
PARAMS = {'access_token': ACCESS_TOKEN}

# METADATA DEFINITIONS
papers = [
    {
        "id": PAPER_1_ID,
        "file": FILE_1_NAME,
        "metadata": {
            "title": "Beyond Retry: A Metacognitive Dynamics Framework for Autonomous Agent Failure Recovery",
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": "<b>System:</b> LID-LIFT Orchestrator v1.4<br><b>Series:</b> Part 1 of the LID-LIFT Technical Suite<br><br><b>Abstract:</b><br>Autonomous agents frequently encounter 'cognitive deadlocks'—states where iterative retries fail to resolve a task due to strict constraints, missing tools, or context overflow. Traditional error handling (try/catch loops) exacerbates token waste in these scenarios. This paper introduces the LID-LIFT Protocol, a metacognitive failure-recovery framework. Unlike standard error correction, LID-LIFT triggers a four-stage dynamic: (1) Objective Abstraction, (2) Tool Broadening, (3) Solution Diversification, and (4) Context Re-packing. We demonstrate that this method statistically improves success rates in 'impossible' scenarios by shifting the agent’s operating plane rather than forcing execution on a blocked path.<br><br>TECHNICAL KEYWORDS:<br>Agentic AI, Large Language Models (LLM), Metacognition, Control Theory, Failure Recovery, Autonomous Orchestration, System Architecture.",
            "creators": [{
                "name": AUTHOR_NAME,
                "affiliation": "Independent Researcher",
                "orcid": AUTHOR_ORCID
            }],
            "keywords": ["Agentic AI", "Metacognition", "LID-LIFT"]
        }
    },
    {
        "id": PAPER_2_ID,
        "file": FILE_2_NAME,
        "metadata": {
            "title": "The Landauer Context: A Physics-Grounded Energy Basis for Large Language Model Orchestration",
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": "<b>System:</b> LID-LIFT Orchestrator v1.4<br><b>Series:</b> Part 2 of the LID-LIFT Technical Suite<br><br><b>Abstract:</b><br>As Large Language Model (LLM) agents approach autonomy, their energy consumption becomes a critical limiting factor. Current 'Green AI' metrics rely on fluctuating estimates of kilowatt-hours (kWh) or carbon intensity, which fail to provide a stable baseline for algorithmic efficiency. This paper proposes the Landauer Context, a reporting framework that normalizes agentic energy expenditure against the theoretical Landauer limit (kT ln 2). We introduce the Thermodynamic Efficiency Ratio (eta_therm) as a standardized metric for the LID-LIFT Orchestrator, allowing for precise arbitration between high-accuracy/high-energy models and heuristic approximations based on fundamental physical limits.<br><br>TECHNICAL KEYWORDS:<br>Green AI, Sustainable Computing, Landauer Limit, Thermodynamics, LLM Efficiency, Energy Metrics, Super Learner Arbitration.",
            "creators": [{
                "name": AUTHOR_NAME,
                "affiliation": "Independent Researcher",
                "orcid": AUTHOR_ORCID
            }],
            "keywords": ["Green AI", "Landauer Limit", "Thermodynamics"],
            "related_identifiers": [
                {
                    "relation": "cites",
                    "identifier": f"10.5281/zenodo.{PAPER_1_ID}",
                    "resource_type": "publication-workingpaper",
                    "scheme": "doi"
                }
            ]
        }
    },
    {
        "id": PAPER_3_ID,
        "file": FILE_4_NAME,
        "metadata": {
            "title": "MCP Tool Dissonance: Podman Container Implementation",
            "upload_type": "software",
            "description": "<b>System:</b> LID-LIFT Orchestrator v1.4<br><b>Series:</b> Part 3 of the LID-LIFT Technical Suite<br><br><b>Package:</b> mcp-tool-dissonance-v1.0.0-podman<br><b>Platform:</b> Podman (OCI-compatible)<br><br><b>Abstract:</b><br>Production-ready container implementation of the Dissonance-Weighted Eviction (DWE) algorithm. This package provides a Podman-native deployment of the MCP (Model Context Protocol) tool for long-horizon agent memory management. Features include: distroless container base, non-root execution (UID 65532), Quadlet systemd integration, and 4 deployment methods.<br><br><b>Security Features:</b><br>- Rootless operation (UID 65532)<br>- NoNewPrivileges enforced<br>- All capabilities dropped<br>- Distroless base (no shell)<br>- Auto-update compatible<br><br><b>Files:</b> 15<br><b>Go Lines:</b> 750<br><br>TECHNICAL KEYWORDS:<br>MCP, Podman, Container Security, DWE Algorithm, Agent Memory, OCI, Quadlet, Distroless.",
            "creators": [{
                "name": AUTHOR_NAME,
                "affiliation": "Independent Researcher",
                "orcid": AUTHOR_ORCID
            }],
            "keywords": ["MCP", "Podman", "Container Security", "DWE Algorithm", "Agent Memory"],
            "version": "1.0.0",
            "language": "eng",
            "related_identifiers": [
                {
                    "relation": "isPartOf",
                    "identifier": f"10.5281/zenodo.{PAPER_1_ID}",
                    "resource_type": "publication-workingpaper",
                    "scheme": "doi"
                },
                {
                    "relation": "references",
                    "identifier": "arXiv:2604.11322",
                    "scheme": "arxiv"
                },
                {
                    "relation": "references",
                    "identifier": "arXiv:2604.11288",
                    "scheme": "arxiv"
                }
            ]
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
        # Diagnostic Error Message
        print(f"\n❌ CRITICAL ERROR: Could not find file: '{file_path}'")
        print(f"   Current Directory: {os.getcwd()}")
        print("   Files actually present in this folder:")
        try:
            for f in os.listdir():
                if f.endswith(".md"):
                    print(f"    - {f}")
        except:
            print("    (Could not list directory)")
        return 404

def update_deposit(dep_id, metadata):
    if not dep_id or dep_id.startswith("REPLACE"):
        print(f"⚠️ Skipping update for {metadata['title']}: No valid ID provided.")
        return 0

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
        sys.exit(1)

    print("--- LID-LIFT Publication Pipeline ---")
    print(f"Author: {AUTHOR_NAME} ({AUTHOR_ORCID})")

    for p in papers:
        dep_id = p.get('id')

        # 1. Update Draft Metadata
        if dep_id:
            update_deposit(dep_id, p['metadata'])
        else:
             print(f"⚠️ Skipping '{p['metadata']['title']}' due to missing ID.")
             continue

        # 2. Upload File
        if p['file']:
            status = upload_file(dep_id, p['file'])
            if status == 404:
                print("   -> Tip: Update the FILE_X_NAME variables at the top of the script to match your actual files.")
                continue

        # 3. Output Link
        print(f"✅ Draft Ready: {BASE_URL.replace('/api', '')}/deposit/{dep_id}")

    print("\nNOTE: Ensure 'ORCID Auto-Update' is enabled in DataCite Profiles.")

if __name__ == "__main__":
    main()