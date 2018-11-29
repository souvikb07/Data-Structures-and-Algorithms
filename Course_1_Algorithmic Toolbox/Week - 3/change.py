# Uses python3
import sys

def get_change(m):
    #write your code here
    if m >= 10:
        ten_coin = m // 10
        coin_remaining = m % 10
        if coin_remaining >= 5:
            five_coin = coin_remaining // 5
            coin_remaining = coin_remaining % 5
            if coin_remaining >= 0:
                one_coin = coin_remaining // 1
        elif coin_remaining >=0:
            five_coin = 0
            one_coin = coin_remaining//1
        return ten_coin + five_coin + one_coin
    elif m >= 5 and m < 10:
        five_coin = m // 5
        coin_remaining = m % 5
        if coin_remaining >= 0:
            one_coin = coin_remaining // 1
        return five_coin + one_coin
    elif m >= 2 and m < 5:
        one_coin = m//1
        return one_coin
    else:
        return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))