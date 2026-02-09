# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return (abs(left_height - right_height) <= 1) and is_tree_balanced(root.left) and is_tree_balanced(root.right)
```

- Maintained all function signatures and variable names
- Improved readability by using more descriptive variable names (left_height, right_height)
- Simplified the return statement in is_tree_balanced by removing redundant "is True" checks
- Preserved all edge case behavior (None root, balanced/unbalanced trees)
- Kept the same return types for all functions
- Maintained the original logic and structure of the height calculation
- Ensured the balance check still performs both height comparison and recursive balance checks
- No changes to the Node class structure or initialization
- All test cases should pass as the behavior is identical to the original implementation
