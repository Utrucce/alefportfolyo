import json, sys

sys.stdout.reconfigure(encoding='utf-8')
full_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript_full.jsonl"

with open(full_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index")
        if 450 <= idx <= 500:
            for tc in data.get("tool_calls", []):
                if tc.get("name") in ["write_file", "edit_file"]:
                    path = tc["args"].get("Path")
                    print(f"Step {idx} wrote to: {path}")
