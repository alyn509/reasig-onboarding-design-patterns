import sys


def main():
    if len(sys.argv) < 2:
        print("Choose a design pattern example to run:")
        return


    cmd = sys.argv[1]

    print(f"Pattern '{cmd}' not found")