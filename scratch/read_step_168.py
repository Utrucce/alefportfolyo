import json, sys

sys.stdout.reconfigure(encoding='utf-8')
full_path = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\.system_generated\logs\transcript_full.jsonl"

with open(full_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index")
        if idx in [165, 166, 167, 168, 169, 170, 187]:
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                print(f"Step {idx} tool: {tc.get('name')}")
                if tc.get("name") in ["write_file", "edit_file"]:
                    args = tc.get("args", {})
                    path = args.get("Path", "")
                    content = args.get("Content", "") or args.get("Replacement", "")
                    print(f"  Target: {path}, length: {len(content)}")
                    if "index.html" in path:
                        # find section goruntuler
                        import re
                        m = re.search(r'<section[^>]*id="goruntuler"[\s\S]*?</section>', content)
                        if m:
                            print("  Found #goruntuler in Step", idx, ":\n", m.group(0)[:500])
