from __future__ import print_function, division
from math import sqrt
 
def cell(n, x, y, start=1):
    d, y, x = 0, y - n//2, x - (n - 1)//2
    l = 2*max(abs(x), abs(y))
    d = (l*3 + x + y) if y >= x else (l - x - y)
    return (l - 1)**2 + d + start - 1
 
def show_spiral(n, found_symbol='* ', not_found_symbol=None):
    start = 1
    top = start + n*n + 1
    is_prime = [False,False,True] + [True,False]*(top//2)
    for x in range(3, 1 + int(sqrt(top))):
        if not is_prime[x]: continue
        for i in range(x*x, top, x*2):
            is_prime[i] = False
 
    cell_str = lambda x: f(x) if is_prime[x] else not_found_symbol
    f = lambda _: found_symbol 
 
    if not_found_symbol == None: not_found_symbol = ' '*len(found_symbol)
 
    for y in range(n):
        print(''.join(cell_str(v) for v in [cell(n, x, y, start) for x in range(n)]))
    print()

n = int(input("Enter N :"))
found_symbol = str(input("What symbol you want to use? :"))
not_found_symbol = str(input("What symbol you want to use if the number is not prime? :"))

show_spiral(n,found_symbol,not_found_symbol)
