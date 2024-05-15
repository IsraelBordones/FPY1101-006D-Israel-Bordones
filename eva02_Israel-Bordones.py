import os
productos = {"escoba": 5, "huevo": 25, "leche": 10}
menup = ["Ver Stock de productos", "Añadir Nuevo Producto",
         "Ajustar Stock", "Eliminar Producto", "Salir"]
print ("*"*50)
print ("*"*21,"STOCK","*"*22)
print ("*"*50)

while True:
    for ind in range(len(menup)):
        print(f"{ind+1}. {menup[ind]}")
    ans = input("Escoge una opción:\n")
    if ans == "1":
        os.system("cls")
        print(productos)
        print()
    elif ans == "2":
        os.system("cls")
        ans4 = input ("Escribe el nuevo producto:\n")
        if ans4 in productos:
            print("Error: El producto ya esta.")
            print()
        else:
            productos({ans4}) : 0
#se me olvido el como se hacia para añadir algo a un diccionario :,v
    elif ans == "3":
        os.sytem("cls")
        ans2 = input("Escoge el producto al que vas a ajustar: " )
        if ans2 in productos:
            ans3 = int(input("Escribe cual es el valor actual"))
#no me dio el tiempo xd 
        else:
            print()
            print("ERROR: El elemento que seleccionaste no esta en los productos")
            print()
    elif ans == "4":
        while True:
            ans1 = input("Escriba el producto a eliminar:\n")
            if ans1 in productos:
                productos.pop(ans1)
            os.system("cls")
            print("Producto eliminado exitosamente")
            break
    elif ans == "5":
        os.system("cls")
        exit("Gracias por usar nuestro programa. Adios")
    else:
        os.system("cls")
        print("ERROR: Escoge una opción valida")
