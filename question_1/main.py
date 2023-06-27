# Determine the integer of the sum of two floats.
# The returned value is the truncated float, i.e. everything after the decimal point is removed.
#
# Constraints
#  0.1 > a , b< 10^6
#  a and b have at most 8 places after the decimal point.

def truncated_float_sum(a, b):
    if a <= 0.1 or b >= 10 ** 6:
        return "Invalid input"
    return int(a + b)


if __name__ == "__main__":

    # Usage examples
    a = 0.05
    b = 50000000
    result = truncated_float_sum(a, b)
    print(result)  # Output: Invalid input

    c = 3.14159
    d = 2.71828
    result = truncated_float_sum(c, d)
    print(result)  # Output: 5
