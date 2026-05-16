from datetime import datetime
from pathlib import Path
from subprocess import Popen

THIS_DIR = Path(__file__).parent


def test_very_good_coverage():
    with open("python-code-coverage-results.md", "w") as out, (THIS_DIR / "fake-py.md").open() as inp:
        print(inp.read() + f"\nDate: {datetime.utcnow()}", file=out)

    with open("cpp-code-coverage-results.md", "w") as out, (THIS_DIR / "fake-cpp.md").open() as inp:
        print(inp.read() + f"\nDate: {datetime.utcnow()}", file=out)

    # start and forget to force pr_number.txt to have "2" and not "1"
    p = Popen(THIS_DIR / "watcher")
