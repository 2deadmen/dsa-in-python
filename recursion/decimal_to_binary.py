def bin(n):
    assert int(n)== n,"number should be a positive  integer "

    if n == 0:
        return 0
    else:
        return n%2 + 10 * bin(int(n/2))
print(bin(10))