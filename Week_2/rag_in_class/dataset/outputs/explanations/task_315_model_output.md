# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1

    while i < n:
        if str[i] == ' ':
            if currlen % 2 == 0 and currlen > maxlen:
                maxlen = currlen
                st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1

    if currlen % 2 == 0 and currlen > maxlen:
        maxlen = currlen
        st = i - currlen

    return str[st:st + maxlen] if st != -1 else "-1"
```

- Combined conditions for maxlen update to improve readability
- Simplified the final return statement using a ternary operator
- Maintained all original variable names and function signature
- Preserved exact behavior including edge cases (e.g., returning "-1" when no valid substring found)
- Kept the same logic flow and loop structure
- No changes to the return type or function parameters
- Improved code formatting and indentation for better readability
- All test cases should pass as the core logic remains unchanged
