def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements from lst1 and lst2."""
    return [a + b for a, b in zip(lst1, lst2)]
