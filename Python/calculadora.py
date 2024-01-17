print("bienvenido a tu calculadora de sumas, por favor, dame dos números para sumarlos.")
def sumas():
    número_1=int(input("¿Cual será tu primer número? "))
    número_2=int(input("¿Cual será tu segundo número? "))
    print(número_1+número_2)
sumas()
Final=input("¿quieres seguir usando el programa? (Y/N) ")
while Final == "Y":
    sumas()
    Final=input("¿quieres seguir usando el programa? (Y/N) ")
    if Final == "N":
        exit
        
