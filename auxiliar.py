def assign_if_none(value, default_value):
    return value if value is not None else default_value


def bind_generic(target_objects, condition, additional_code, trigger_method_name):
    for card in target_objects:
        if condition(card):

            def decorator(original_method):
                def wrapper():
                    original_method()
                    additional_code()
                return wrapper

            setattr(card, trigger_method_name, decorator(getattr(card, trigger_method_name)))
