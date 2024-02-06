# estudiantes=[1,2,3,4,5,6]
# estudiantes[len(estudiantes)] #dice en numeros cuantos elementos hay en la lista pero no la posicion

# # estudiantes[len(estudiantes)-1] 

# # vec = range(-4,5,2) #el tercer numero es lo que le suma
# # list(vec) #transforma el rango en una lista
# # [x for x in vec] #hace una lista con los elementos de vec llamada x

# # s=input("fruta: ")
# # s.strip() #quita los espacios sobrantes a la palabra 

# matriz=[["A","B","C","D", "E"], ["F","G","H","I","J"]]
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j]) #primero pasa por la primera lista con i, y depsues con j pasa por 
#         #cada elemento de cada lista dentro dde la lista principal

# x=int(input("numero"))

# for i in range(1,x+1):
#     #tratar de hacer eso para primo

products={
    "mobiles":{
        "Apple":[
            {"id":"1",
             "name":"Iphone7",
             "price":"300"},

             {"id":"2",
              "name":"iphone8",
              "price":"200"}
        ]
        }
    }


for K,V in products.items(): #la k hace referencia a mobiles, y la V a lops valores de cada key del diccionario
    for k1,v1 in V.items():
        for i in range(len(v1)): #aca usamos x porque ya estamos dentro de una lista
            for k2,v2 in v1[i]:
                print(k2)


