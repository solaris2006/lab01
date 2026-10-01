"""Tiny module used by the GitHub Actions examples."""


def greet(name: str = "world") -> str:
    """Return a greeting for ``name``."""
    return f"hello, {name}"


def farewell(name: str = "world") -> str:
    """Return a farewell for ``name``."""
    return f"bye, {name}"


if __name__ == "__main__":
    import sys

    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(who))
    print(farewell(who))
