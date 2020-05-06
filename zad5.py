početnaVrijednost = int(input('Upiši pozitivan broj: '))
brojač = 0

if početnaVrijednost < 1:
    print('Pogreška')
else:
    while početnaVrijednost > 1:
        if početnaVrijednost % 2 == 0:
            broj = početnaVrijednost / 2
            brojač += 1
        else:
            broj = početnaVrijednost * 3 + 1
            brojač += 1
        print(f'{brojač}.Sljedeca vrijednost:{int(broj)}')
        početnaVrijednost = broj
    print(f'Krajnja vrijednost: {int(početnaVrijednost)}, broj koraka: {int(brojač)}')
