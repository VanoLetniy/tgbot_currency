import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:  # Ошибка ConvertionException
    @staticmethod
    def get_price(quote: str, base: str, amount: str) -> object:
        if quote == base:  # Если валюты одинаковы
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:  # Если исходной валюты нет в списке keys
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:  # Если итоговой валюты нет в списке keys
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:  # Если количество не является числом
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        # Get запрос API cryptocompare.com, где quote_ticker - исходная валюта указанная пользователем
        # base_ticker - итоговая валюта указанная пользователем
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
