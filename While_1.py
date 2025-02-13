#input

n = int(input("Dijite un numero: "))

#processing
s = 0
i = 1

while i <= n:
    s = s + i
    i = i + 1

#ouput

print(f"La suma de los {n} primeros numeros es: {s}")