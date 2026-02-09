# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
def smallest_multiple(n):
    if n <= 2:
        return n

    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]

    while True:
        divisible = True
        for a in factors:
            if i % a != 0:
                i += n
                divisible = False
                break
        if divisible:
            return i
```

- Retained the original function signature and variable names
- Improved readability by separating the divisibility check into a clear flag variable
- Maintained the same logic flow and edge case handling
- Preserved the exact same return type and behavior
- Kept the same loop structure and increment logic
- Ensured the same factors list generation
- Maintained the same termination condition
- Preserved all original functionality as validated by tests
