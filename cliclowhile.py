controlador=100

print("******EMPANADAS EL MACHETE******")
print("1: Agregar un sabor de empanadas ")
print("2: Ver sabor de empanada ")
print("3: Salir ")


while controlador!=3:
    controlador=int(input("Digita un opcion: "))
    if controlador==1:
        sabor=input("¿Que sabor de empanada deseas?")
    elif controlador==2:
        print(f"El sabor de empanada que elegiste:{sabor}")  
    elif controlador==3:
        print("!Un gusto atenderte")
    else:
        print("La opcion que elegiste no es valida")