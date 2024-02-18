def bit_is_even(n):
    return n & 1 == 0


def bit_is_odd(n):
    return n & 1 == 1


def bit_is_odd1(n):
    return not bit_is_even(n)

