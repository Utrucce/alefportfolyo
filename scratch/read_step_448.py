import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')
transcript_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index", 0)
        if 440 <= idx <= 460:
            content = data.get("content", "")
            print(f"Step {idx} [{data.get('type')}]: {content[:200]}...")
