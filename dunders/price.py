EXCHANGE_RATES = {
    "USD": 1,
    "UAH": 0.036,
    "GBP": 1.39,
}


class Price:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency.upper()

    def __add__(self, other: "Price") -> "Price":
        if self.currency != other.currency:
            amount_in_usd = self._convert_to_usd(
                self.amount, self.currency
            ) + self._convert_to_usd(other.amount, other.currency)
            amount = self._convert_from_usd(amount_in_usd, self.currency)
        else:
            amount = self.amount + other.amount
        return Price(amount, self.currency)

    def __sub__(self, other: "Price") -> "Price":
        if self.currency != other.currency:
            amount_in_usd = self._convert_to_usd(
                self.amount, self.currency
            ) - self._convert_to_usd(other.amount, other.currency)
            amount = self._convert_from_usd(amount_in_usd, self.currency)
        else:
            amount = self.amount - other.amount
        return Price(amount, self.currency)

    def _convert_to_usd(self, amount: float, currency: str) -> float:
        if currency == "USD":
            return amount
        else:
            return amount / self.EXCHANGE_RATES.get(currency)

    def _convert_from_usd(self, amount_in_usd: float, currency: str) -> float:
        if currency == "USD":
            return amount_in_usd
        else:
            return amount_in_usd * self.EXCHANGE_RATES.get(currency)

    def __repr__(self) -> str:
        return f"{round(self.amount, 2)} '{self.currency}'"


def main():
    price1 = Price(100, "USD")
    price2 = Price(200, "GBP")

    result = price1 + price2
    print(result)

    result = price1 - price2
    print(result)


if __name__ == "__main__":
    main()
