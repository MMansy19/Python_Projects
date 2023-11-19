import requests

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://api.apilayer.com/fixer/convert?to={api_key}&from={from_currency}&to={to_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.json().get('rate')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = '8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9'

    # Get user input
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                print("The amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a numeric amount.")

    # Get exchange rate
    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)

    if exchange_rate is not None:
        # Perform currency conversion
        converted_amount = convert_currency(amount, exchange_rate)

        # Display the result
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
