# Uses python3
def calc_fib(n):
    num=[]
    num.append(0)
    num.append(1)
    for i in range(2,n+1):
        num.append(num[i-1] + num[i-2])
    return num[n]


n = int(input())
print(calc_fib(n))