# myproject29/lib.py

def try_me(x):
    """
    return x Time 29 when x is a positive integer.
    """
    if (type(x) == int) and (x > 0):
        return x * 29
    return 0


if __name__ == "__main__":
    val = try_me(-3)
    print(val)
