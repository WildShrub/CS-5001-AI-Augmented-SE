def parallel_lines(line1, line2):
    """Check if two lines are parallel by comparing their slopes.

    Args:
        line1: A tuple or list representing the first line in (m, b) form.
        line2: A tuple or list representing the second line in (m, b) form.

    Returns:
        bool: True if the lines are parallel, False otherwise.
    """
    return line1[0] / line1[1] == line2[0] / line2[1]
