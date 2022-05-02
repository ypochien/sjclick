import sys
from .applications import SjClick as SjClick

def main():
    sjclick = SjClick()
    sjclick.run()


if __name__ == "__main__":
    sys.exit(main())