broj = input("Unesi broj: ")
lista = [int(znamenka) for znamenka in str(broj)]
brojač = 0
lista2 = lista[::-1]
print(lista)
print(lista2)

for znamenka in reversed(lista2):
    brojač += 1
    print(znamenka**2)
print(f"Broj znamenki: {brojač}")
