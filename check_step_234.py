import json, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript_full.jsonl"
with open(p, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") in [230, 231, 232, 233, 234]:
            for tc in data.get("tool_calls", []):
                print(f"Step {data.get('step_index')}: {tc.get('name')} -> {tc.get('args')}")
