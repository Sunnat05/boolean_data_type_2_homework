def main(a):
    type(a)==type(1) and a%4==0  and a**2>10000 and a%1==0
    """
    Check if a given year is a leap year and the square of the year is greater than 10000.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return type(a)==type(1) and a%4==0  and a**2>10000
print(main(400))