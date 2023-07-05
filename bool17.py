def main(L,R):
    """
    Check that given L is the length of a circle of radius R.
    Args:
        L: float
        R: float
    Returns:
        bool
    """
    # Write your code here
    return type(L,R)==type(1.0) and 3.14==L/(2*R) 
print(main(12.56,2))