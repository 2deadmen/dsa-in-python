def fact(n):
    assert n>=0 and int(n)==n,"number should ben an integer"
    if n in [0,1]:
        return n
    else:
        return (n*fact(n-1))

print(fact(3))