import numpy as np
import matplotlib.pyplot as plt


def count(arr, plotting=False):
    if control_input(arr):
        return count_water(arr, plotting)
    else:
        return None


def count_water(arr, plotting):
    total = 0
    found = np.zeros(len(arr))
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
                if i_max != -1 :
                    total_t, found_t = estimate(arr, i - 1, i_max, plotting)
                    found = np.add(found, found_t)
                    total = total_t + total
                    # since there's always an increment of i at the end,
                    # Placing i equal to i_max will make the next iteration to ignore
                    # the interval just considered
                    i = i_max
            # if the value of the current index is greater the one
            # of the previous value, look for possible inlet before the current index
            elif arr[i] > prev:
                # where's the
                i_max = prev_max_at(arr, i)
                if i_max != -1 :
                    total_t, found_t = estimate(arr, i, i_max, plotting)
                    found = np.add(found, found_t)
                    total = total_t + total
                    # No skipping to any other index
            i = i + 1
    if plotting:
        plot_res(arr, found)
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
    max_t = 0
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
            elif arr[x] > arr[i]:
                if arr[x] > max_t:
                    max_t = arr[x]
                    ind = x
            x = x + 1
    return ind


def estimate(arr, i, i_max, plotting):
    # baseline for plotting
    base = np.zeros(len(arr))
    tot = 0
    lim_sup = min(arr[i], arr[i_max])
    if i < i_max:
        interval = range(i + 1, i_max)
    else:
        interval = range(i_max + 1, i)
    for x in interval:
        tot = tot + (lim_sup - arr[x])
        if plotting:
            base[x] = (lim_sup - arr[x])
    return tot, base


def plot_res(arr, base):
    xaxe = np.arange(len(arr))
    fig, (x1, x2) = plt.subplots(2)
    x1.bar(xaxe, arr)
    x1.axis([-1, len(arr), 0, max(arr) + 2])
    x1.bar(xaxe, base, bottom=arr, color="red")
    x2.bar(xaxe, arr)
    x2.axis([-1, len(arr), 0, max(arr) + 2])
    plt.show()


def control_input(arr):
    controlled = False
    if arr is None:
        print("None Array passed")
    else:
        if any(x < 0 for x in arr):
            make_every_positive(arr)
        controlled = True
    return controlled


def make_every_positive(arr):
    min_value = min(arr)
    for i in range(0, len(arr)):
        arr[i] = arr[i] + (-min_value)
