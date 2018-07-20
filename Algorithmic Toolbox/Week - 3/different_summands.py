# Uses python3
import sys

def optimal_summands(n):
    summands = []
    
    k = n
    L = 1

    if k <= 2*L:
    	summands.append(k)
    	return summands

    while k > 2*L:
    	summands.append(L)
    	k = k - L
    	L = L + 1
    	if k <= 2*L:
	    	summands.append(k)

    return summands
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
