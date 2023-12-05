def definir(l1, l2, l3):
    cant1 = cant1 + cant1
    cant2 = cant2 + cant2
    cant3 = cant3 + cant3
    if l1==l2 and l1==l3:
        cant1=cant1+1
    else:
        if l1==l2 or l1==l3 or l2==l3:
            cant2=cant2+1
        else:
            cant3=cant3+1
    print("Equilatero:",cant1)
    print("Isoseles:",cant2)
    print("Escaleno",cant3)

def ingreso_datos():
    n = int(input("Ingrese cantidad a procesar:"))
    for x in range(n):
        lado1=int(input("Ingrese lado 1:"))
        lado2=int(input("Ingrese lado 2:"))
        lado3=int(input("Ingrese lado 3:"))
        definir(lado1, lado2, lado3)

ingreso_datos()

