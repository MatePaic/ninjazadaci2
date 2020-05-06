unosBrojeva = 0
brojac_1 = 0
brojac_2 = 0
brojac_3 = 0
while unosBrojeva % 3 == 0 or unosBrojeva % 5 == 0:
    unosBrojeva = int(input('Unesi brojeve: '))
    if unosBrojeva % 5 == 0 and unosBrojeva % 3 == 0:
        brojac_1 += 1
    elif unosBrojeva % 3 == 0:
        brojac_2 += 1
    elif unosBrojeva % 5 == 0:
        brojac_3 += 1
    else:
        break
print(f'Unesena su {brojac_1} broja dijeljiva sa 3 i 5')
print(f'Unesena su {brojac_2} broja dijeljiva sa 3')
print(f'Unesena su {brojac_3} broja dijeljiva sa 5')




