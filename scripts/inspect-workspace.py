#!/usr/bin/env python3
"""Read-only structural inspection of a RoModular workspace."""
from pathlib import Path
import subprocess, sys

REPOS = ("RoModular", "RoModularAgents", "RoModularBuild", "CPSTL", "Foundation", "DspCore", "MCC", "MIDILAR")

def run(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], text=True,
        capture_output=True, check=False).stdout.strip()

def main():
    root = Path(sys.argv[1] if len(sys.argv) == 2 else ".").resolve()
    failed = False
    for name in REPOS:
        repo = root / name
        if not (repo / ".git").exists():
            print(f"error: missing repository {name}"); failed = True; continue
        status = run(repo, "status", "--porcelain")
        branch = run(repo, "branch", "--show-current")
        required = ["README.md", "LICENSE", "AGENTS.md"]
        missing = [item for item in required if not (repo / item).is_file()]
        print(f"{name}: branch={branch or 'detached'} clean={'yes' if not status else 'no'}"
              f" required={'ok' if not missing else 'missing:' + ','.join(missing)}")
        failed |= bool(status or missing)
    return int(failed)

if __name__ == "__main__":
    raise SystemExit(main())
