import sys

from .patterns import all_patterns


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.design_patterns_example_runner <pattern>")
        print_available_patterns(all_patterns.keys())
        return

    cmd = sys.argv[1]

    if cmd in all_patterns:
        all_patterns[cmd].main()
    else:
        print(f"Unknown pattern: {cmd}")
        print_available_patterns(all_patterns.keys())


def print_available_patterns(patterns):
    print("Available patterns:")
    for pattern in patterns:
        print("-", pattern)
