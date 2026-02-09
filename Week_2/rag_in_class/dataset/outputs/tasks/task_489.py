def frequency_Of_Largest(n, arr):
    if n == 0:
        return 0

    max_val = arr[0]
    frequency = 1

    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            frequency = 1
        elif arr[i] == max_val:
            frequency += 1

    return frequency
