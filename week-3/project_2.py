print('Welcome to Izifin Technology\'s Annual Tax Revenue(ATR) System.')
years = int(input('How many years of experience do you have?'))
age = int(input('How old are you? '))

if years > 25 & age >= 55:
    print('Your ATR is N5,600,000.')
elif years > 20 & age >= 45:
    print('Your ATR is N4,480,000.')
elif years > 10 & age >= 35:
    print('Your ATR is N1,500,000')
else:
    print('Your ATR is N550,000.')