import json

p = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript.jsonl"
with open(p, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        c = json.dumps(data, ensure_ascii=False)
        for w in ['banana', 'nano', 'arka plan']:
            if w in c.lower():
                print(f"Step {data.get('step_index')}: found {w} -> {c[:120]}")
