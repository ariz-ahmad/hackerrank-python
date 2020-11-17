# hackkerrank_print_function
# input: n: 4
# output: 1234
# * operator on range unpacks the array
# https://www.hackerrank.com/challenges/python-print/tutorial

if __name__ == '__main__':
    n = int(input())
    print(*range(1, n+1), sep='')