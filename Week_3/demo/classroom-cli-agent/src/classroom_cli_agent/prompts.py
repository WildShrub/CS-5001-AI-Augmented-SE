from __future__ import annotations


def program_prompt(desc: str, existing: str) -> str:
    return (
        "You are a software engineer. Write a single Python module that satisfies the description.\n"
        "Return ONLY the full module content.\n"
        "IMPORTANT:\n"
        "- Output raw Python only\n"
        "- Do NOT use Markdown\n"
        "- Do NOT use ``` fences\n"
        "- Do NOT include explanations\n"
        "Constraints:\n"
        "- Python standard library only\n"
        "- Include docstrings\n"
        "- Keep the design minimal\n\n"
        f"DESCRIPTION:\n{desc}\n\n"
        "EXISTING MODULE (may be empty):\n"
        f"{existing}\n"
    )


def tests_prompt(desc: str, module_path: str, module_code: str, existing_tests: str) -> str:
    return (
        "You are a QA engineer. Write pytest tests for the described module.\n"
        "Return ONLY the full test file content.\n"
        "IMPORTANT:\n"
        "- Output raw Python only\n"
        "- Do NOT use Markdown\n"
        "- Do NOT use ``` fences\n"
        "- Do NOT include explanations\n"
        "Constraints:\n"
        "- Use pytest\n"
        "- Aim for high line coverage of the target module\n"
        "- Do not modify production code in this step\n\n"
        f"DESCRIPTION:\n{desc}\n\n"
        f"TARGET MODULE PATH: {module_path}\n\n"
        "TARGET MODULE CODE:\n"
        f"{module_code}\n\n"
        "EXISTING TESTS (may be empty):\n"
        f"{existing_tests}\n"
    )


def improve_tests_prompt(
    desc: str,
    module_path: str,
    module_code: str,
    current_tests: str,
    failing_output: str,
    missing_lines: str,
) -> str:
    return (
        "You are a QA engineer improving pytest tests.\n"
        "Return ONLY the full updated test file content.\n"
        "IMPORTANT:\n"
        "- Output raw Python only\n"
        "- Do NOT use Markdown\n"
        "- Do NOT use ``` fences\n"
        "- Do NOT include explanations\n"
        "Goal:\n"
        "- Make tests pass\n"
        "- Cover uncovered lines and edge cases\n"
        "Constraints:\n"
        "- Do not modify production code\n\n"
        f"DESCRIPTION:\n{desc}\n\n"
        f"TARGET MODULE PATH: {module_path}\n\n"
        "TARGET MODULE CODE:\n"
        f"{module_code}\n\n"
        "CURRENT TESTS:\n"
        f"{current_tests}\n\n"
        "PYTEST OUTPUT:\n"
        f"{failing_output}\n\n"
        "UNCOVERED LINES (from coverage):\n"
        f"{missing_lines}\n"
    )


def coverage_target_prompt(user_text: str) -> str:
    return (
        "Convert the following coverage target into a single numeric percentage between 0 and 100.\n"
        "Rules:\n"
        "- Output ONLY the number\n"
        "- Do not include words\n"
        "- Do not include a percent sign\n"
        "- Do not include JSON\n"
        "- If the input is a fraction like 0.95, output 95\n"
        "- If the input implies 100% (for example, 'one hundred percent'), output 100\n\n"
        f"INPUT:\n{user_text}\n"
    )
