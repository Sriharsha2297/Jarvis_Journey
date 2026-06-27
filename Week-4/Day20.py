# Type Hints & Docstrings
# n def greet(name: str) -> str:
# n list[str], dict[str, int]
# n Optional[str] from typing
# n Triple-quoted docstrings
# n Add type hints to all previous code
# n pip install mypy && mypy your_file.py

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

list_of_names: list[str] = input("Enter names separated by commas: ").split(",")
name_to_age: dict[str, int] = dict(input("Enter name-age pairs (name:age) separated by commas: ").split(","))
from typing import Optional
def find_age(name: str) -> Optional[int]:
    """Return the age of the person with the given name, or None if not found."""
    return name_to_age.get(name)

triple_quoted_docstring = """This is a triple-quoted docstring.
It can span multiple lines and is often used for documentation."""

hinted_variable: int = 42
