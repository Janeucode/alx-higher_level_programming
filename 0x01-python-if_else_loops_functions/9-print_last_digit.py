#!/usr/bin/python3
def lastd(n):
    n = str(n)
    if n:
        last_d = n[-1]
        print('{}'.format(last_d))
    else:
        print('the input is empty')
