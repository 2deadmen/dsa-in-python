def sum(n):
    assert n>=0 and int(n)== n,"number should be a positive  integer "
    if n<10:
        return n
    else:
        return n%10 + sum(n//10)
    
print(sum(233))