import os, json, sys, re

sys.stdout.reconfigure(encoding='utf-8')
transcript_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript.jsonl"

found_steps = []
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        content = json.dumps(data, ensure_ascii=False)
        if "ekran_goruntusu" in content or "oabt-ekran" in content or "mebags_1" in content or "01_Namaz" in content:
            found_steps.append((data.get("step_index"), data.get("type")))

print("Steps with screenshot mentions:", found_steps)
