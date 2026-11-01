import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')
full_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript_full.jsonl"

with open(full_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") == 166:
            content = data["tool_calls"][0]["args"]["Content"]
            matches = re.findall(r'(\.[a-zA-Z0-9_-]*(?:phone|screenshot|carousel|screen|mockup)[^{]*\{[^}]*\})', content)
            for m in matches:
                print(m)
                print("---")
