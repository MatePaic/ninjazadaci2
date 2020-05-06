prvi_broj = int(input('Prvi jednoznamenkasti broj: '))
drugi_broj = int(input('Drugi jednoznamenkasti broj: '))

if prvi_broj % 2 == 0 and drugi_broj %  2 == 0:
    parni_broj = str(prvi_broj) + str(drugi_broj)
    parni_broj_2 = str(drugi_broj) + str(prvi_broj)
    print(f'Parni brojevi stvoreni od znamenaka {prvi_broj} i {drugi_broj} su: {parni_broj} i {parni_broj_2}')

elif prvi_broj % 2 == 0 and drugi_broj % 2 == 1:
    parni_broj = str(drugi_broj) + str(prvi_broj)
    print(f'Parni brojevi stvoreni od znamenaka {prvi_broj} i {drugi_broj} su: {parni_broj}')
elif prvi_broj % 2 == 1 and drugi_broj % 2 == 0:
    parni_broj = str(prvi_broj) + str(drugi_broj)
    print(f'Parni brojevi stvoreni od znamenaka {prvi_broj} i {drugi_broj} su: {parni_broj}')
else:
    print('Nema parnih brojeva')

