import importlib
import pkgutil

all_patterns = {}

for _loader, module_name, _is_pkg in pkgutil.iter_modules(__path__):
    full_module_name = f"{__name__}.{module_name}"
    module = importlib.import_module(full_module_name)
    all_patterns[module_name] = module
