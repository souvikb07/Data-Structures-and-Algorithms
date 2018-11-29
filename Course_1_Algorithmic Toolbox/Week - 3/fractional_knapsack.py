# Uses python3
import sys

def arrange(val,wt,vlwt,n):
    for i in range(n):
        for j in range(i+1,n):
            if(vlwt[i]<vlwt[j]):
                temp=vlwt[i]
                vlwt[i]=vlwt[j]
                vlwt[j]=temp
                temp=wt[i]
                wt[i]=wt[j]
                wt[j]=temp
                temp=val[i]
                val[i]=val[j]
                val[j]=temp

def get_optimal_value(capacity, weights, values):
    value=0;
    n=len(values)
    vlwt=[0 for x in range(n)]
    for i in range(n):
        vlwt[i]=values[i]/weights[i]
    arrange(values,weights,vlwt,n)
    for i in range(n):
        if(capacity==0):
            return value
        elif(weights[i]<=capacity):
            value=value+values[i]
            capacity=capacity-weights[i]
        else:
            value=value+(values[i]*(capacity/weights[i]))
            capacity=0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))