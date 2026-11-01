import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')
transcript_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index", 0)
        tool_calls = data.get("tool_calls", [])
        for tc in tool_calls:
            name = tc.get("name", "")
            args = tc.get("args", {})
            content = str(args)
            if "write_file" in name and ("index.html" in content or "generate_site.py" in content):
                # see what images were written in index.html
                imgs = re.findall(r'assets/[a-zA-Z0-9_\-\.]+\.(?:png|jpg|webp)', content)
                if imgs:
                    print(f"Step {idx} ({name}): {set(imgs)}")
