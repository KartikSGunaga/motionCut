import requests
from datetime import datetime
import pytz

class CurrencyConverter:
    APIKEY = "https://v6.exchangerate-api.com/v6"
    def __init__(self, key, baseCurrency, targetCurrency):
        self.key = key
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency

    def convertTime(self, utcTime):

        input_datetime = datetime.strptime(utcTime, "%a, %d %b %Y %H:%M:%S %z")

        ist_timezone = pytz.timezone("Asia/Kolkata")
        ist_datetime = input_datetime.astimezone(ist_timezone)

        result_str = ist_datetime.strftime("%a, %d %b %Y %H:%M:%S %Z")

        return result_str

    def fetchCurrencyValue(self, amount):
        url = f"{self.APIKEY}/{self.key}/pair/{self.baseCurrency}/{self.targetCurrency}/{amount}"

        try:
            # print(url)
            response = requests.get(url)
            data = response.json()

            # print("Full JSON Response:", data)

            conversionResult = data["conversion_result"]
            utcTime = data["time_last_update_utc"]
            istTime = self.convertTime(utcTime)

            print(f"The amount {self.baseCurrency} {amount} = {self.targetCurrency} {conversionResult}.")
            print(f"The converted rate is fetched at: {istTime}.")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def main():
    print("\nWelcome to Currency converter!")

    key = "fface0495a0ebf7bf9a916e0"
    base = input("\nEnter the base currency in ISO 4217 code: ").upper()
    target = input("Enter the target currency in ISO 4217 code: ").upper()

    convert = CurrencyConverter(key, base, target)

    amount = float(input("\nEnter the amount to convert: "))
    convert.fetchCurrencyValue(amount)


if __name__ == '__main__':
    main()
