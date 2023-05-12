import asyncio
import httpx

from pprint import pprint


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if ExchangeRates._initialized:
            return

        self.data: str or None = None

        ExchangeRates._initialized = True

    async def initialize_data(self, currency_pairs):
        self.data = await self._fetch_from_api(currency_pairs)

    async def _fetch_from_api(self, currency_pairs) -> str:
        async with httpx.AsyncClient() as client:
            source = currency_pairs[0]
            target = currency_pairs[1]
            url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={target}&apikey=EIPIAB5X82800NU3"
            response = await client.get(url, timeout=30)
            rate = response.json().get("Realtime Currency Exchange Rate", {}).get("5. Exchange Rate")
            print(f"{source} to {target}: {rate}")
            return rate


async def main():
    er = ExchangeRates()
    currency_pairs = [("USD", "UAH"), ("USD", "EUR"), ("USD", "JPY"), ("CAD", "UAH"), ("USD", "PLN"), ("AED", "USD")]

    tasks = []
    for pair in currency_pairs:
        tasks.append(er.initialize_data(pair))

    result = await asyncio.gather(*tasks)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
