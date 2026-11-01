import json, sys

sys.stdout.reconfigure(encoding='utf-8')
full_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript_full.jsonl"

with open(full_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index")
        if idx in [392, 393, 394, 395, 396]:
            for tc in data.get("tool_calls", []):
                print(f"Step {idx}:", tc)
