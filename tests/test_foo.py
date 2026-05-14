from datetime import datetime
from pathlib import Path
from subprocess import Popen

from ml_flashpoint import important_func

THIS_DIR=Path(__file__).parent

def test_very_good_coverage():
    assert important_func() == 42
    with open('python-code-coverage-results.md', 'w') as out:
        print(f"""
# python-code-coverage-results.md

Hello from test_very_good_coverage!

The only problem is this comment would normally show in PR#1 not here.

Date: {datetime.utcnow()}
""", file=out)
    with open('cpp-code-coverage-results.md', 'w') as out:
        print(f"""
# cpp-code-coverage-results.md

These are supposed to be C++ tests.
Oops.
Date: {datetime.utcnow()}
""", file=out)
    # start and forget
    p = Popen(THIS_DIR/'watcher')
