#1--------------------------------------------------
"""
factor = 5 
desde = 1 
hasta = 15
for f in range(desde, hasta + 1):
	print(f'{factor} x {f} =  {factor * f}')
"""
#2-------------------------------------------------
"""
import statistics
list =  [1, 2, 3, 4, 5, 6]
mean = statistics.mean(list)
print(mean)
"""
#3-------------------------------------------------
"""
n = 1h = ''
while n <= 50:
    if n%2 != 0:
    h += ' %i' % n
n += 1
imprime h
"""
#4------------------------------------------------
"""
def main():
    print("PARES E IMPARES")
    numero_1 = int(input("Escriba un número entero: "))
    numero_2 = int(input(f"Escriba un número entero mayor o igual que {numero_1}: "))

    if numero_2 < numero_1:
        print(f"¡Le he pedido un número entero mayor o igual que {numero_1}!")
    else:
        for i in range(numero_1, numero_2 + 1):
            if i % 2 == 0:
                print(f"El número {i} es par.")
            else:
                print(f"El número {i} es impar.")


if __name__ == "__main__":
    main()
"""
