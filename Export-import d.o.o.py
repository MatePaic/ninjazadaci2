plaća = int(input('Trenutna plaća: '))
broj_godina_staža = int(input('Broj godina staža: '))

if broj_godina_staža < 10:
    print('Nisu ispunjeni uvjeti')
else:
    plaća = plaća / (1 - broj_godina_staža * 0.01 )
    print(f'Nakon {broj_godina_staža} godina plaća je {plaća}')
    

