import json, sys

sys.stdout.reconfigure(encoding='utf-8')
transcript_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index", 0)
        if 130 <= idx <= 180 and data.get("type") in ["PLANNER_RESPONSE", "USER_INPUT"]:
            content = data.get("content", "")
            if content:
                print(f"Step {idx}: {content[:300]}...\n")
