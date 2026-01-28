def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b


while True:
    print("Menu calculadora")

    print("1. Suma")
    print("2. Resta")
    print("3. Multi")
    print("4. Division")
    print("5. Salir")

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

            print(f"La resta de {n1} - {n2} es = {suma(n1,n2)}")

        case "3":
            print("Multi")
            n1 = int(input("Inserte el primer numero: "))
            n2 = int(input("Inserte el segundo numero: "))

            print(f"La resta de {n1} * {n2} es = {multi(n1,n2)}")

        case "4":
            print("Division")
            n1 = int(input("Inserte el primer numero: "))
            n2 = int(input("Inserte el segundo numero: "))

            if n2 == 0:
                print("No se puede dividir entre 0")
            else:
                print(f"La resta de {n1} * {n2} es = {multi(n1,n2)}")

        case "5":
            print("Adios")
            break

        case _:
            print("Esa opcion no existe")
