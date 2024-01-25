n=int(input("factorial de que"))
result=1
for i in range(1,n):
    result*=i #multiplica lo que esta en result por i y lo pone en result
    print("fact("+str(i)+")="+str(result))
print("y finalmente el factorial de", n, "es...",(result*n))