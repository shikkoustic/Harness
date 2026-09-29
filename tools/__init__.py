import importlib
import pkgutil

_tool_modules = {}

for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    if hasattr(module, "SCHEMA") and hasattr(module, "run"):
        _tool_modules[module.SCHEMA["function"]["name"]] = module


def get_schemas():
    return [module.SCHEMA for module in _tool_modules.values()]


def call_tool(name: str, arguments: dict) -> str:
    if name not in _tool_modules:
        return f"Error: unknown tool '{name}'"
    return _tool_modules[name].run(**arguments)
