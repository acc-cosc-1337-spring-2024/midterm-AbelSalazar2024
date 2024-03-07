#add import
#Q1

from question_a import get_fahrenheit

print('Celsius\t Fahrenheit')

C = 0

while C <= 20:
    F = get_fahrenheit(C)
    print(f'{C}\t{F:.2f}')
    C += 1



