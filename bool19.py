def main(a):
    a%4==0 and (a%400==0 or not a%100==0) and a**2>10000
    """
    Check if a given year is a leap year and the square of the year is greater than 10000.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a%4==0 and a**2>10000
print(main(400))