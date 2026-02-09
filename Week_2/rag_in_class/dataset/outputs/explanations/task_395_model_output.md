# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None
```

- Maintained the original function signature and variable names
- Preserved the exact logic for tracking character counts and order
- Kept the same return type (returns a character or None)
- Ensured edge cases (empty string, all repeating characters) behave identically
- No changes to the algorithm's time or space complexity
- Code formatting remains consistent with original
- All test cases should pass without modification
