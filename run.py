import subprocess
import sys
from pathlib import Path

SCRIPTS_ROOT = Path("scripts/python")


def run(script: str) -> None:
    print(f"Running {script}...")
    subprocess.run([sys.executable, SCRIPTS_ROOT / script], check=True)


def main():
    run("extract_data.py")
    run("clean_data.py")
    run("init_db.py")
    run("load_data.py")


if __name__ == "__main__":
    main()
