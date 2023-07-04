def main(a):
    ans=(a%7==0 and not a%3==0)
    """
    Check if a given number is divisible by 7 but not by 3.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return ans
print(main(21))
