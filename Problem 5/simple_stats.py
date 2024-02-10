"""
Name: Henry Holman
Lab Time: Thursday @ 2pm
"""


def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''

    avg1 = (num1 + num2 + num3 + num4)/4
    prod1 = num1 * num2 * num3 * num4
    avg2 = (num1 + num2 + num3 + num4)/4
    prod2 = num1 * num2 * num3 * num4

    #Output each rounded integer using the following:
    print(f'{prod1:.0f}' + " " + f'{avg1:.0f}')

    #Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
    print(f'{prod2:.3f}' + " " + f'{avg2:.3f}')
if __name__ == "__main__":
    simple_stats()