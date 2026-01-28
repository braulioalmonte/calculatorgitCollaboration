def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

#Multipication va aqui

#Division va aqui

while True:
    print("Menu calculadora")

    print("1. Suma")
    print("2. Resta")
    #Multiplicacion va aqui

    #Division va aqui
    print("3. Salir")

    usuario = input("")

    match usuario:
        case "1":
            print("Suma")
            n1 = int(input("Inserte el primer numero: "))
            n2 = int(input("Inserte el segundo numero: "))

            print(f"La suma de {n1} + {n2} es = {suma(n1,n2)}")

        case "2":
            print("Resta")
            n1 = int(input("Inserte el primer numero: "))
            n2 = int(input("Inserte el segundo numero: "))

            print(f"La resta de {n1} + {n2} es = {suma(n1,n2)}")

        case "3":
            print("Adios")
            break

        case _:
            print("Esa opcion no existe")
