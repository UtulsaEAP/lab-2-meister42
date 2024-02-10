"""
Name: Henry Holman
Lab Time: Thursday @ 2pm
"""

def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    first = str(phone_number//10000000)
    second = str(int(phone_number%10000000)//10000)
    third = str(phone_number % 10000)

    print("(" + first + ")" + " " + second + "-" + third)


if __name__ == "__main__":
    telephone()