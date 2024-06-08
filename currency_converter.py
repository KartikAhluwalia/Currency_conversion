
import requests
from termcolor import colored, cprint
from pyfiglet import Figlet

# Get user input
from_currency = input("Enter the original currency: ").upper()
to_currency = input("Enter the currency you would like to convert to: ").upper()
amount = float(input("Enter the amount of money: "))

# Define color print functions
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
print_yellow = lambda x: cprint(x, 'yellow')
print_blue = lambda x: cprint(x, 'blue')
print_magenta = lambda x: cprint(x, 'magenta')
print_cyan = lambda x: cprint(x, 'cyan')
print_white = lambda x: cprint(x, 'white')

# Request exchange rate data
response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    converted_amount = data['rates'][to_currency]

    # Print the result using Figlet and colors
    f = Figlet(font='banner3-D', width=200)
    f1 = Figlet(font='standard', width=200)
    f2 = Figlet(font='slant', width=200)

    

    print_yellow(f"{amount} {from_currency}")
    print_green(f"is")
    print_blue(f"{converted_amount} {to_currency}")
else:
    print_red("Failed to retrieve data. Please check your input and try again.")
