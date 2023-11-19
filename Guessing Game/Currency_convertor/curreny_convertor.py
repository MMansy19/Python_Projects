import requests

def make_currency_conversion_request(currency_in, currency_out, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={currency_out}&from={currency_in}&amount={amount}"
    headers = {"apikey": "8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making currency conversion request: {e}")
        return None

def get_user_input():
    currency_in = input("Enter your currency code: ").upper()
    currency_out = input("Enter target currency code: ").upper()

    while True:
        try:
            amount = float(input("Enter the amount you need to convert: "))
            if amount <= 0:
                print("The amount must be greater than 0.")
            else:
                return currency_in, currency_out, amount
        except ValueError:
            print("Please enter a numeric amount.")

def display_result(amount, currency_in, result, currency_out):
    converted_amount = result.get('result')
    print(f"{amount} {currency_in} = {converted_amount} {currency_out}")

#The main
print("Welcome to the Currency Converter!")
currency_in, currency_out, amount = get_user_input()
result = make_currency_conversion_request(currency_in, currency_out, amount)
if result is not None:
    display_result(amount, currency_in, result, currency_out)



