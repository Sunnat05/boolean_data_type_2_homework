def main(a):
    a%4==0 and (a%400==0 or not a%100==0)
    """
    Check if a given year is a leap year. Leap year is  is divisible by 4 and 400 but not by 100.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a%4==0 and (a%400==0 or not a%100==0)
print(main(1704))