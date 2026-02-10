from __future__ import annotations
import argparse
import os
from .agent import Agent
from .types import AgentConfig
from .utils import ensure_repo_path, ensure_ollama_available, ensure_model_available

DEFAULT_MODEL = "devstral-small-2:24b-cloud"
DEFAULT_HOST = "http://localhost:11434"

def main() -> None:
    p = argparse.ArgumentParser(prog="cca", description="Classroom CLI agent (Ollama-only)")
    p.add_argument("--repo", required=True, help="Repository path")
    p.add_argument("--model", default=os.environ.get("OLLAMA_MODEL", DEFAULT_MODEL), help=f"Ollama model (default: {DEFAULT_MODEL})")
    p.add_argument("--host", default=os.environ.get("OLLAMA_HOST", DEFAULT_HOST), help=f"Ollama host (default: {DEFAULT_HOST})")
    p.add_argument("--temperature", type=float, default=float(os.environ.get("OLLAMA_TEMPERATURE", "0.0")))
    p.add_argument("--max-iters", type=int, default=6)
    p.add_argument("--verbose", action="store_true")

    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("create", help="Create/update a program module from a description")
    c.add_argument("--desc", required=True)
    c.add_argument("--module", required=True)

    t = sub.add_parser("test", help="Generate tests and iterate until 100% coverage or max iterations")
    t.add_argument("--desc", required=True)
    t.add_argument("--module", required=True)
    t.add_argument("--tests", required=True)

    cm = sub.add_parser("commit", help="Commit and optionally push changes")
    cm.add_argument("--message", required=True)
    cm.add_argument("--push", action="store_true")

    f = sub.add_parser("full", help="Create program, generate tests, reach 100% coverage, then commit/push")
    f.add_argument("--desc", required=True)
    f.add_argument("--module", required=True)
    f.add_argument("--tests", required=True)
    f.add_argument("--message", default="Agent: program and tests")
    f.add_argument("--push", action="store_true")

    args = p.parse_args()

    ensure_repo_path(args.repo)
    ensure_ollama_available()
    ensure_model_available(args.model)

    cfg = AgentConfig(
        repo=args.repo,
        model=args.model,
        host=args.host,
        temperature=args.temperature,
        max_iters=args.max_iters,
        verbose=args.verbose,
    )
    agent = Agent(cfg)

    if args.cmd == "create":
        r = agent.create_program(args.desc, args.module)
    elif args.cmd == "test":
        r0 = agent.create_tests(args.desc, args.module, args.tests)
        if not r0.ok:
            raise SystemExit(r0.details)
        r = agent.improve_tests_to_100(args.desc, args.module, args.tests, cfg.max_iters)
    elif args.cmd == "commit":
        r = agent.commit_and_push(args.message, args.push)
    else:
        r1 = agent.create_program(args.desc, args.module)
        if not r1.ok:
            raise SystemExit(r1.details)
        r2 = agent.create_tests(args.desc, args.module, args.tests)
        if not r2.ok:
            raise SystemExit(r2.details)
        r3 = agent.improve_tests_to_100(args.desc, args.module, args.tests, cfg.max_iters)
        if not r3.ok:
            raise SystemExit(r3.details)
        r = agent.commit_and_push(args.message, args.push)

    raise SystemExit(0 if r.ok else r.details)
