import inspect
from typing import get_type_hints

def generate_docstring(func):
    """
    Generate a docstring template from a function's type annotations.
   
    Args:
        func (callable): The function to inspect.
   
    Returns:
        str: A formatted docstring template.
    """
    # Get type hints (includes return type if present)
    hints = get_type_hints(func)
    sig = inspect.signature(func)

    doc_lines = ['"""', f"{func.__name__} function.", "", "Args:"]
   
    # Parameters
    for name, param in sig.parameters.items():
        type_hint = hints.get(name, "Any")
        doc_lines.append(f"    {name} ({type_hint.__name__ if hasattr(type_hint, '__name__') else type_hint}): Description.")
   
    # Return type
    return_type = hints.get('return', None)
    if return_type and return_type is not inspect.Signature.empty:
        doc_lines.append("")
        doc_lines.append("Returns:")
        doc_lines.append(f"    {return_type.__name__ if hasattr(return_type, '__name__') else return_type}: Description.")
   
    doc_lines.append('"""')
    return "\n".join(doc_lines)

# Example usage
def add_numbers(a: int, b: int) -> int:
    return a + b

print(generate_docstring(add_numbers))