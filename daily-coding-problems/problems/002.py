from functools import reduce


def products_with_division(l):
    n = len(l)

    prod = reduce(lambda x, y: x*y, l)
    ans = [prod]*n
    for i in range(n):
        ans[i] = ans[i] // l[i]

    return ans


assert str(products_with_division([1, 2, 3, 4, 5])) == '[120, 60, 40, 30, 24]'
assert str(products_with_division([3, 2, 1])) == '[2, 3, 6]'


def products(l):
    n = len(l)

    left_to_right = [1]*n
    for i in range(n - 1):
        left_to_right[i+1] *= l[i] * left_to_right[i]

    right_to_left = [1]*n
    for i in reversed(range(1, n)):
        right_to_left[i-1] *= l[i] * right_to_left[i]

    return [x*y for x, y in zip(left_to_right, right_to_left)]


assert str(products([1, 2, 3, 4, 5])) == '[120, 60, 40, 30, 24]'
assert str(products([3, 2, 1])) == '[2, 3, 6]'
