# Classroom CLI Agent (cca) - Ollama-only

This package assumes you will always use Ollama.

Default model: `devstral-small-2:24b-cloud`
Override:
- `--model <name>` or
- `OLLAMA_MODEL` environment variable

## Install (editable)
pip install -e .

## Commands
Create program:
cca create --repo <repo> --desc "..." --module src/program.py

Generate tests and iterate to 100% coverage (or max iterations):
cca test --repo <repo> --desc "..." --module src/program.py --tests tests/test_program.py --max-iters 6

Commit and optionally push:
cca commit --repo <repo> --message "..." --push

All-in-one:
cca full --repo <repo> --desc "..." --module src/program.py --tests tests/test_program.py --message "..." --push
