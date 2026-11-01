import json, sys

sys.stdout.reconfigure(encoding='utf-8')
full_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript_full.jsonl"

with open(full_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index")
        for tc in data.get("tool_calls", []):
            if tc.get("name") in ["write_file", "edit_file"]:
                path = tc["args"].get("Path", "")
                if "index.html" in path and idx < 469:
                    print(f"Step {idx} wrote index.html directly! Length: {len(tc['args'].get('Content', ''))}")
                elif "generate_site.py" in path and idx < 469:
                    print(f"Step {idx} wrote generate_site.py! Length: {len(tc['args'].get('Content', ''))}")
