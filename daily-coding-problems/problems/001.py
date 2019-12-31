def two_sum(l, k):
    l = sorted(l)

    i, j = 0, len(l) - 1
    while i < j:
        if l[i] + l[j] < k:
            i += 1
        elif l[i] + l[j] > k:
            j -= 1
        else:
            return True

    return False


if __name__ == "__main__":
    l = [10, 15, 3, 7]
    assert two_sum(l, 17), str(l)
