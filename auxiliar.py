import inspect

def assign_if_none(value, default_value):
    return value if value is not None else default_value


def bind_generic(target_objects, condition, additional_code, trigger_method_name):
    for anObject in target_objects:
        if condition(anObject):

            def decorator(original_method):
                def wrapper():
                    original_method()
                    if len(inspect.signature(additional_code).parameters) == 1:  ### HORIBLE!!! CULPA DE Hiker.
                        additional_code(anObject)
                    else:    
                        additional_code()
                return wrapper

            setattr(anObject, trigger_method_name, decorator(getattr(anObject, trigger_method_name)))
