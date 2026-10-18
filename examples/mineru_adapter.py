"""Example adapter: read MinerU structured_content.json and call an LLM for paragraph reverse-outline.

This is a minimal illustrative script. It is NOT production-ready. You must set OPENAI_API_KEY as an environment variable.

Requirements:
- pip install openai

Usage:
python examples/mineru_adapter.py path/to/structured_content.json
"""

import json
import os
import sys

try:
    import openai
except ImportError:
    raise SystemExit("Please install openai: pip install openai")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise SystemExit("Please set OPENAI_API_KEY environment variable")

openai.api_key = OPENAI_API_KEY

REVERSE_OUTLINE_PROMPT = (
    "你是论文逻辑审稿人。请根据论文写作逻辑审查这一段文本，并输出结构化意见。\n" 
    "文本如下：\n\n\"\"\"{para}\"\"\"\n\n" 
    "请按以下格式返回：\n"
    "1. 本段主题句（1句话）\n"
    "2. 本段的主要论点（1-2句话）\n"
    "3. 本段是否有明确的支撑证据或解释？如果有，写出支撑方式；如果没有，指出缺失\n"
    "4. 本段是否有逻辑问题？如：主题不清、证据不足、段落过长、前后不一致、过渡弱\n"
    "5. 最优先修改建议（只给 1 条）\n"
    "6. 若需要改写，给出 2 个可替换的段落首句（不同语气：正式/简洁）\n"
)


def analyze_paragraph(para_text):
    prompt = REVERSE_OUTLINE_PROMPT.format(para=para_text)
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "你是严格的学术论文编辑。"},
                      {"role": "user", "content": prompt}],
            max_tokens=600,
            temperature=0.0,
        )
    except Exception as e:
        return {"error": str(e)}

    text = resp["choices"][0]["message"]["content"].strip()
    return {"result": text}


def main(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # MinerU / structured_content conventions: pages -> items, or a top-level list of pages
    # Try to find paragraph blocks in common locations
    paragraphs = []

    def collect_paragraphs(obj):
        if isinstance(obj, dict):
            t = obj.get("type") or obj.get("content_type") or obj.get("block_type")
            if t and t.lower() in ("paragraph", "text"):
                text = obj.get("content", "")
                if isinstance(text, dict):
                    text = text.get("text", "")
                if text:
                    paragraphs.append(text)
            for v in obj.values():
                collect_paragraphs(v)
        elif isinstance(obj, list):
            for it in obj:
                collect_paragraphs(it)

    collect_paragraphs(data)

    print(f"Found {len(paragraphs)} paragraph-like blocks.\nProcessing up to 50...")

    results = []
    for i, p in enumerate(paragraphs[:50], start=1):
        print(f"Analyzing paragraph {i}...")
        out = analyze_paragraph(p)
        results.append({"index": i, "paragraph": p, "analysis": out})

    # Write results to file
    out_path = "paper_logic_analysis.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Wrote analysis to {out_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python examples/mineru_adapter.py path/to/structured_content.json")
        sys.exit(1)
    main(sys.argv[1])
