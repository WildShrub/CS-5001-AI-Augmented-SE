# Classroom CLI Agent (cca) - Ollama-only

Default model: devstral-small-2:24b-cloud
Override:
- --model <name>
- OLLAMA_MODEL environment variable

## Install
pip install -e .

## Start Ollama and pull model
ollama serve
ollama pull devstral-small-2:24b-cloud

## Example repo (make sure it is a git repo)
cd demo_repo
git init
git add -A
git commit -m "init demo repo"
cd ..

## Create a program
cca --repo demo_repo create --desc "prime number checker" --module src/program.py

## Generate tests and iterate until target coverage (natural language)
cca --repo demo_repo test --desc "prime number checker" --module src/program.py --tests tests/test_program.py --coverage "one hundred percent" --max-iters 6

## Commit and push
cca --repo demo_repo commit --message "Agent: add program + tests" --push

## End-to-end
cca --repo demo_repo full --desc "prime number checker" --module src/program.py --tests tests/test_program.py --coverage "at least ninety five percent" --message "Agent: program + tests" --push
