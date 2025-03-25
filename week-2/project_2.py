#importing the required library
import numpy as np

#asking the user to input the required values
print('this program handles three different types of equations.')
eqn_list = ['quadratic', 'cubic', 'quartic']
for i in range(1, 4):
    print(str(i) + '. ' + eqn_list[i - 1])
eqn = int(input("Choose the type of equation you want to find the roots of: "))
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))


#finding the roots of the quadratic equation
def quadratic(a, b, c):
    disc = b ** 2 - (4 * a * c)
    if disc < 0:
        print('this equation has no real roots')
    else: 
        root1 = ((0 - b) + (disc ** 0.5)) / (2 * a)
        root2 = ((0 - b) - (disc ** 0.5)) / (2 * a)
    print(f'the roots of the equation are {root1} and {root2}')

#finding the roots of the cubic equation
def cubic(a, b, c, d):
    cubic_list = [a, b, c, d]
    roots = np.roots(cubic_list)
    print("Roots of the cubic equation:", roots)

#finding the roots of the quartic equation
def quartic(a, b, c, d, e):
    quartic_list = [a, b, c, d, e]
    roots = np.roots(quartic_list)
    print("Roots of the quartic equation:", roots)

#performing the calculations
if eqn == 1:
    quadratic(a, b, c)
elif eqn == 2:
    d = float(input('Enter the value of d: '))
    cubic(a, b, c, d)
elif eqn == 3:
    d = float(input('Enter the value of d: '))
    e = float(input('Enter the value of e: '))
    quartic(a, b, c, d, e)
