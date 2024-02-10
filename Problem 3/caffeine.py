"""
Name: Henry Holman
Lab Time: Thursday @ 2pm
"""

def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''

    sixhrs = (caffeine_mg/2)
    twelvehrs = (caffeine_mg/4)
    twentyfourhrs = (caffeine_mg/16)

    print("After 6 hours: " + f'{sixhrs:.2f}'+ " mg")
    print("After 12 hours: " + f'{twelvehrs:.2f}' + " mg")
    print("After 24 hours: " + f'{twentyfourhrs:.2f}'  + " mg")


if __name__ == "__main__":
    caffeine()