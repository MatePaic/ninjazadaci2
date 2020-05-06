iznos = int(input('Unesite iznos: '))

broj_novčanica_od_50_kn = int(iznos / 50)
broj_novčanica_od_20_kn = int(iznos % 50 / 20)
broj_novčanica_od_5_kn = int(iznos % 50 % 20 / 5)
broj_novčanica_od_2_kn = int(iznos % 50 % 20 % 5 / 2)
broj_novčanica_od_1_kn = int(iznos % 50 % 20 % 5 % 2)

print(f'''Broj novčanica od 50 kn: {broj_novčanica_od_50_kn}
      Broj novčanica od 20 kn: {broj_novčanica_od_20_kn}
      Broj novčanica od 5 kn: {broj_novčanica_od_5_kn}
      Broj novčanica od 2 kn: {broj_novčanica_od_2_kn}
      Broj novčanica od 1 kn: {broj_novčanica_od_1_kn}''')

