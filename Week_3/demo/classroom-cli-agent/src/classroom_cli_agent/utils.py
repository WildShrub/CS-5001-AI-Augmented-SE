from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, Tuple


def clamp(s: str, max_chars: int = 14000) -> str:
    if len(s) <= max_chars:
        return s
    return s[:max_chars] + "\n\n[TRUNCATED]"


def ensure_repo_path(repo: str) -> Path:
    p = Path(repo).resolve()
    if not p.exists() or not p.is_dir():
        raise SystemExit(f"Invalid repo path: {repo}")
    return p


def ensure_ollama_available() -> None:
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, text=True, check=True)
    except Exception:
        raise SystemExit("Ollama CLI not found. Install Ollama and ensure `ollama` is on PATH.")


def ensure_model_available(model: str) -> None:
    try:
        out = subprocess.check_output(["ollama", "list"], text=True)
    except Exception:
        raise SystemExit("Unable to run `ollama list`. Ensure Ollama is installed and running.")
    if model not in out:
        raise SystemExit(f"Ollama model '{model}' not found locally. Run: ollama pull {model}")


def parse_coverage_total(json_path: Path) -> Tuple[float, Dict[str, Any]]:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    total = float(data["totals"]["percent_covered"])
    return total, data


def strip_code_fences(text: str) -> str:
    """
    Remove Markdown code fences and language tags from LLM output.
    Also trims common wrappers like '[CODE]' or leading prose lines.
    """
    if not text:
        return ""

    s = text.strip()

    # Remove simple wrappers often seen in model outputs
    s = re.sub(r"^\s*\[CODE\]\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^\s*Here is the code:\s*", "", s, flags=re.IGNORECASE)

    lines = s.splitlines()

    # Drop opening fence: ``` or ```python
    if lines and lines[0].lstrip().startswith("```"):
        lines = lines[1:]

    # Drop closing fence
    if lines and lines[-1].lstrip().startswith("```"):
        lines = lines[:-1]

    return "\n".join(lines).strip()
