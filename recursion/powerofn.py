def power(base,n):
 assert int(n)== n,"number should be a positive  integer "
 if n<1:
   return 1
 elif n<0:
   return 1/base * power(base,n+1)
   
 else:
    return base  * power(base,n-1)

print(power(2,-2))