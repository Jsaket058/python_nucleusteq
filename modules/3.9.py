# 9. Use `importlib` to dynamically import a module and invoke a function.

import importlib

def dynamic_import_and_call(module_name, func_name, *args):
    """
    Dynamically import a module and call a function from it.

    Args:
        module_name (str): Name of the module to import.
        func_name (str): Name of the function to invoke.
        *args: Positional arguments to pass to the function.

    Returns:
        The result returned by the function.
    """
    module = importlib.import_module(module_name)
    
    func = getattr(module, func_name)
    
    return func(*args)


result = dynamic_import_and_call("mymodule", "greet", "Saket")
print(result)
