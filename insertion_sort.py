def insertion_sort(vector):
    for i in range(len(vector),1,-1):
        temp=vector[i-1]
        j=i-2
        while j>=0 and temp>vector[j]:
            vector[j-1]=vector[j]
            j-=1
        vector[j-1]=temp
    return vector

lista=[3,5,8,1]

insertion_sort(lista) #no funciona

print(lista)