def count(arr):
    total = 0
    if len(arr) < 2:
        return 0
    else:
        i = 1  # during the first execution, the previous is 0
        while i < len(arr):
            prev = arr[i - 1]
            # if the value of the previous index is greater the current one
            # look for possible inlet after the current index
            if arr[i] < prev:
                i_max = next_big_at(arr, i)
                if i_max != -1:
                    total = total + estimate(arr, i - 1, i_max)
                    # since there's always an increment of i at the end,
                    # Placing i equal to i_max will make the next iteration to ignore
                    # the interval just considered
                    i = i_max
            # if the value of the current index is greater the one
            # of the previous value, look for possible inlet before the current index
            elif arr[i] > prev:
                # where's the
                i_max = prev_max_at(arr, i)
                if i_max != -1:
                    total = total + estimate(arr, i, i_max)
                    # No skipping to any other index
            i = i + 1
    return total


def prev_max_at(arr, i):
    ind = -1
    maximum = arr[i - 1]
    found = False
    x = i - 2
    while not found:
        if x < 0:
            found = True
        else:
            if arr[x] > maximum:
                maximum = arr[x]
                ind = x
                found = True
            x = x - 1
    return ind


def next_big_at(arr, i):
    ind = -1
    maximum = arr[i - 1]
    found = False
    x = i + 1
    while not found:
        if x > len(arr) - 1:
            found = True
        else:
            if arr[x] >= maximum:
                maximum = arr[x]
                ind = x
                found = True
            x = x + 1
    return ind


def estimate(arr, i, i_max):
    tot = 0
    lim_sup = min(arr[i], arr[i_max])
    if i < i_max:
        interval = range(i, i_max)
    else:
        interval = range(i_max + 1, i)
    for x in interval:
        tot = tot + (lim_sup - arr[x])
    return tot