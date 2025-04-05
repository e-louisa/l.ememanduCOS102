#data for the girls
names = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna', 'Waje', 'Tola','Aisha', 'Latifa']
age = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
height = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

#creating the table for the girls
table_girls = list(zip(names, age, height, scores))
table_girls.insert(0, ["Name", "Age", "Height", "Score"])
for row in table_girls:
    print("{:<10} {:<5} {:<11} {:<15}".format(*row))

print('\n \n')

#data for the boys
names = ['Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola', 'Kunle', 'George', 'Thomas', 'Wesley']
age = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
height = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

#creating the table for the boys
table_boys = list(zip(names, age, height, scores))
table_boys.insert(0, ["Name", "Age", "Height", "Score"])
for row in table_boys:
    print("{:<10} {:<5} {:<11} {:<15}".format(*row))
