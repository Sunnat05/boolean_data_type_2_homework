def main(b):
    number=((b%3==0 and not b%5==0) or (not b%3==0 and b%5==0))
    """
    Check if the given number is divisible by only one of 3 or 5.
    Args:
        b: int
    Returns:
        bool
    """
    # Write your code here
    return number
print(main(36))