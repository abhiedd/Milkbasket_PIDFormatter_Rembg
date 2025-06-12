import os
import ast

import pytest

# Utility to load the clean_sheet_name function from hero_code_plus.py without
# executing the rest of the Streamlit application.

def load_clean_sheet_name():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             "Hero_Function_Seperated", "hero_code_plus.py")
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    module = ast.parse(source)
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == "clean_sheet_name":
            code = compile(ast.Module(body=[node], type_ignores=[]), file_path, "exec")
            ns = {}
            # Provide required imports like 're' when executing the function
            exec(code, {"re": __import__("re")}, ns)
            return ns["clean_sheet_name"]
    raise RuntimeError("clean_sheet_name not found")

clean_sheet_name = load_clean_sheet_name()


def test_remove_invalid_characters():
    result = clean_sheet_name("Na[me]:with*invalid?/chars\\")
    assert result == "Namewithinvalidchars"


def test_trim_and_cap_length():
    long_name = "  " + "x" * 40 + "  "
    result = clean_sheet_name(long_name)
    assert result == "x" * 31
    assert not result.startswith(" ") and not result.endswith(" ")
