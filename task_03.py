from decimal import Decimal
from numpy import arange

# I'm not sure if using non-built-in modules is allowed,
# so I've written two versions of that function.


def get_decimals_using_arange(start=2, stop=6, step=0.5):
    return [Decimal(x) for x in arange(start, stop, step)]


def get_decimals(start=2, stop=6, step=0.5):
    result = []
    curr = start
    while curr < stop:
        result.append(Decimal(curr))
        curr += step
    return result


print(get_decimals())
