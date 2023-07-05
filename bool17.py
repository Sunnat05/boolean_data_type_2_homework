def main(L,R):
    from math import pi
    """
    Check that given L is the length of a circle of radius R.
    Args:
        L: float
        R: float
    Returns:
        bool
    """
    # Write your code here
    return pi==L/(2*R) 
print(main(12.56,2))