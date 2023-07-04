def main(a):
    a<10000 and a%1==0 and (1000<=a<10000 and (a%10+a//1000+(a//100%10)+(a//10%10))%2==1) or (100<=a<1000 and (a%10+a//100+a//10%10)%2==1) or ((10<=a<100 and (a//10+a%10)%2==1)) or ((0<=a<10 and a%2==1))
    """
    Given integer is less of 10000 . Check if the sum of digits is odd .
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a<10000 and a%1==0 and (1000<=a<10000 and (a%10+a//1000+(a//100%10)+(a//10%10))%2==1) or (100<=a<1000 and (a%10+a//100+a//10%10)%2==1) or ((10<=a<100 and (a//10+a%10)%2==1)) or ((0<=a<10 and a%2==1))
print(main(7))