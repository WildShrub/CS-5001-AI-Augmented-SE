from __future__ import annotations

def program_prompt(desc: str, existing: str) -> str:
    return (
        "You are a software engineer. Write a single Python module that satisfies the description.\n"
        "Return ONLY the full module content.\n"
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
        "Constraints:\n"
        "- Use pytest\n"
        "- Aim for 100% line coverage of the target module\n"
        "- Do not modify production code in this step\n\n"
        f"DESCRIPTION:\n{desc}\n\n"
        f"TARGET MODULE PATH: {module_path}\n\n"
        "TARGET MODULE CODE:\n"
        f"{module_code}\n\n"
        "EXISTING TESTS (may be empty):\n"
        f"{existing_tests}\n"
    )

def improve_tests_prompt(desc: str, module_path: str, module_code: str, current_tests: str, failing_output: str, missing_lines: str) -> str:
    return (
        "You are a QA engineer improving pytest tests.\n"
        "Return ONLY the full updated test file content.\n"
        "Goal: Make tests pass and reach 100% line coverage of the target module.\n"
        "Constraints:\n"
        "- Do not modify production code\n"
        "- Add tests for uncovered lines and edge cases\n\n"
        f"DESCRIPTION:\n{desc}\n\n"
        f"TARGET MODULE PATH: {module_path}\n\n"
        "TARGET MODULE CODE:\n"
        f"{module_code}\n\n"
        "CURRENT TESTS:\n"
        f"{current_tests}\n\n"
        "PYTEST OUTPUT (if failures):\n"
        f"{failing_output}\n\n"
        "UNCOVERED LINES (from coverage):\n"
        f"{missing_lines}\n"
    )
