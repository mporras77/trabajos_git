#1----------------------------------------------------------------
"""
edad = int(input("ingrese su edad"))
edadFutura = int(input("ingrese numero"))
total = (edad + edadFutura)
print(total)

"""
#2----------------------------------------------------------------
"""
lado = int(input("ingrese diametros"))
total = lado **3
print(total)

"""
#3----------------------------------------------------------------
"""
producto = int(input("ingrese producto"))
total = producto + producto * 0.10
print (f"(prodcuto) - con 10% {total}")

"""
#4----------------------------------------------------------------

"""
producto = (input("ingrese producto"))
if producto == "arroz" or producto == "huevos":
    print("no hay iva")
    
elif producto == "carne" or producto == "salMarina":
    print("puede tener iva")
else:
    print ("no es valido")
    
"""
#5--------------------------------------------------------------

""""

x=0
while x<100:
    print(x)
    x=x+100

"""

#6--------------------------------------------------------------

""""

def imprimir_tabla(numero):
    # Se supone que las tablas llegan hasta el 10
    LIMITE = 10
    # Comenzar en 1
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        # Incrementar contador para no caer en ciclo infinito
        contador = contador + 1

# Probar función
imprimir_tabla(5)

"""
#7---------------------------------------------------------------

"""

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

"""

#8----------------------------------------------------------

"""
print("- Matriz creada con una lista de listas:")
lista_de_listas=[ [1  ,-4], 
                  [12 , 3], 
                  [7.2, 5]]
matriz = np.array(lista_de_listas)
print(matriz)


print("- Matriz creada con np.zeros:")
dimensiones=(2,3)
matriz_ceros = np.zeros(dimensiones)
print(matriz_ceros)


print("- Matriz creada con np.ones:")
dimensiones=(3,2)
matriz_unos = np.ones(dimensiones)
print(matriz_unos)

#también podemos usar np.copy para copiar una matriz 
print("- Copia de la matriz creada con np.ones:")
matriz_unos_copia=np.copy(matriz_unos)
print(matriz_unos_copia)

"""

#9----------------------------------------------------------------

""""

loanAmount = input("Cuánto quieres pedir prestado? \n")
interestRate = input("Cuál es la tasa de interés? \n")
repaymentLength = input("Cuántos años durará el préstamo? \n")


loanAmount = float(loanAmount)
interestRate = float(interestRate)
repaymentLength = float(repaymentLength)


interestCalculation = interestRate / 100 / 12


numberOfPayments = repaymentLength*12

#Formula
#M = L * ((I * ((1+I) ** n) / (1+I) ** n - 1))

#   * M = Pago mensual
#   * L = Monto préstamo
#   * I = Tasa de interés
#   * N = Número de pagos

monthlyRepaymentCost = loanAmount * (interestCalculation * (1+interestCalculation) * numberOfPayments) / ((1+interestCalculation) ** (numberOfPayments - 1))


totalCharge = (monthlyRepaymentCost ** numberOfPayments) - loanAmount


print("Quieres pedir prestado $" + str(loanAmount) + " por " + str(repaymentLength) + " años, con una tasa de interés de " + str(interestRate) + "%!")

print("Tu pago mensual es de $" + str(monthlyRepaymentCost))

print("El costo de este préstamo es de " + totalCharge)

if interestCalculation == 4.5:
    print("la tasa de interes es igual a la inflacion")

"""

#10---------------------------------------------------------------------------------------------------

"""

PORCENTAJE_IVA = 16

conteo_productos = 1  # Saber en cuál producto vamos
precio_total = 0  # Acumulador del total de productos
# Mientras que el conteo del productos sea menor o igual a 5
while conteo_productos <= 5:
    mensaje = "Ingresa el precio del producto número {}: ".format(
        conteo_productos)
    precio_como_cadena = input(mensaje)
    # Convertir a flotante
    precio = float(precio_como_cadena)
    # Agregarlo al precio total
    precio_total = precio_total + precio
    # Ya leímos un producto, le sumamos al conteo
    conteo_productos = conteo_productos + 1
# Cuando el ciclo termine calculamos el IVA
aumento = precio_total * (PORCENTAJE_IVA / 100)  # Dividir entre 100 porque es un porcentaje
# Sumar el aumento
precio_con_iva = precio_total + aumento
# Imprimir totales
print("Total: ${}".format(precio_total))
print("IVA: ${}".format(aumento))
print("Total con IVA: ${}".format(precio_con_iva))

"""