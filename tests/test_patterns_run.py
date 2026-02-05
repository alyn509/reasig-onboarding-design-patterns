import pytest

from design_patterns_example_runner.patterns import all_patterns


@pytest.mark.parametrize("name,module", all_patterns.items())
def test_pattern_runs(name, module):
    """
    Smoke test: ensure every pattern's main() runs without crashing.
    """
    assert hasattr(module, "main"), f"{name} has no main()"
    module.main()