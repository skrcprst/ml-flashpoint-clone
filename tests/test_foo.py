from ml_flashpoint import important_func


def test_very_good_coverage():
    assert important_func() == 42
    with open('python-code-coverage-results.md', 'w') as out:
        print("hello from test_very_good_coverage!", file=out)