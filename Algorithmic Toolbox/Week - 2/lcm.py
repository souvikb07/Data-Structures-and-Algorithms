# Uses python3
import sys
"""
The most efficient way to find LCM is by dividing the product of 2 numbers with the gcd of a and b.
"""
def gcd(a, b):
    """
    (int,int) -> int
    Return Great common divissior
    >> gcd(357,234)
    3
    >> gcd(2341537,8746812)
    1
    """
    if b == 0:
        return a
    a_ = a % b
    return gcd(b, a_)

def lcm_efficient(a, b):
    """
    (int,int) -> int
    Return Great common divissior
    >> lcm_efficient(357,234)
    3
    >> lcm_efficient(2341537,8746812)
    1
    """
    g = gcd(a, b)
    lcm = a*b//g
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))