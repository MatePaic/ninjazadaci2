list1 = []
number = int(input('Enter list length: '))
print('Enter numbers: ')
for i in range (number):
    data = int(input())
    list1.append(data)
print(list1)
list2 = list1[::-1]
print(list2)

brojac = 0
squared_numbers = []
for number in list2:
    brojac += 1
    squared_numbers.append(number ** 2)
print(squared_numbers,f'Broj znamenki je {brojac}')
