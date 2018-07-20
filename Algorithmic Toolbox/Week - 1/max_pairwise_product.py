# python3


def max_pairwise_product(numbers):
    numbers.sort()
    n = len(numbers)
    return numbers[n-1]*numbers[n-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
