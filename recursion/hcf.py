def gcd(n1,n2):
 assert n1>=0 and int(n1)== n1 and  n2>=0 and int(n2)== n2,"number should be a positive  integer "
 if n2==0 :
    return n1
 else:
    return gcd(n2,n1 % n2)
print(gcd(48,18))