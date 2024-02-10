"""

This house is $200000. The change is $-10000 since last month.
    The estimated monthly mortgage is $850.00.
This house is $200000. The change is $-10000 since last month.
    The estimated monthly mortgage is $850.00.



Name: Henry Holman
Lab Time: Thursday @ 2pm

"""
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here

    change = current_price - last_month_price
    mortgage = (current_price * 0.051) / 12
    

    print("This house is $" + str(current_price) + ". The change is $" + str(change) + " since last month.\nThe estimated monthly mortgage is $" + f'{mortgage:.2f}' + ".")




if __name__ == "__main__":
    real_estate()