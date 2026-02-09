# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    x_coordinate = -b / (2 * a)
    y_coordinate = ((4 * a * c) - (b * b)) / (4 * a)
    vertex = (x_coordinate, y_coordinate)
    return vertex
```

- Retained the original function signature and variable names
- Improved readability by breaking down the calculation into separate steps
- Maintained the exact same return type and behavior
- Preserved all edge case behavior as validated by tests
- Used meaningful intermediate variable names
- Kept the same mathematical operations and order
- Ensured the function still returns a tuple with the same structure
- No changes to the core algorithm or logic
- Code is now more maintainable and easier to debug
- All test cases should pass without modification
