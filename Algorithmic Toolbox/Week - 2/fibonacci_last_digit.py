# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    num=[]
    num.append(0)
    num.append(1)
    for i in range(2,n+1):
        num.append((num[i-1] + num[i-2])%10)
    return num[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))