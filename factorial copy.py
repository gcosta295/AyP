n=int(input("factorial de que"))
result=1
for i in range(n,1,-1):
    result*=i #multiplica lo que esta en result por i y lo pone en result
    print("result en", i, "es", result)
print("y finalmente el factorial de", n, "es...",result)