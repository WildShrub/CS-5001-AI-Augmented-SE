# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    res = [0, 1]
    for i in range(2, n + 1):
        res.append(max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]))
    return res[n]
```

- Preserved the original function signature and return type
- Simplified the loop structure using a for loop instead of while
- Removed redundant list initialization with append(0) and append(1)
- Used integer division operator // for clarity
- Maintained the same edge case behavior for n=0 and n=1
- Kept the same calculation logic for the max sum
- Improved readability by removing unnecessary parentheses and line breaks
- Maintained the exact same behavior as validated by the tests
