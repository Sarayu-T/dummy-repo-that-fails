def buggy_function(denominator=1):
    try:
        result = 1 / denominator
    except ZeroDivisionError:
        result = 0
    return result

buggy_function()