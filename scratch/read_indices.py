import json, sys

sys.stdout.reconfigure(encoding='utf-8')
transcript_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        if i < 5:
            print("Line", i, data.get("step_index"), data.get("type"))
        idx = data.get("step_index")
        if idx in [129, 130, 131, 132, 133, 134, 135, 187, 188, 189]:
            print(f"Step {idx} [{data.get('type')}]: {str(data.get('content'))[:150]}")
