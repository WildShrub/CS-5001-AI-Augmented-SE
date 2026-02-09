# Model output for task_853

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sum_of_odd_Factors(n):
    res = 1
    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors starting from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum

    # If remaining n is a prime number greater than 2
    if n > 2:
        res *= (1 + n)

    return res
```

- Retained the original function signature and variable names
- Improved loop efficiency by skipping even numbers in the factor checking loop
- Added comments to clarify the purpose of each code block
- Maintained the exact same logic for handling factors and their sums
- Preserved the edge case behavior for when n is a prime number
- Kept the same return type and value calculation
- Ensured the mathematical operations remain identical to the original
- Maintained the same variable initialization and update patterns
