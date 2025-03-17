import datetime
from typing import Optional

class TooManyBoardsError(Exception):
    def __str__(self) -> str:
        return 'Cart cannot have more than 4 surfboards in it!'

class CheckoutDateError(Exception):
    def __str__(self) -> str:
        return 'Check out date cannot be past or present!'

class ShoppingCart:
    def __init__(self) -> None :
        self._num_surfboards: int = 0
        self._checkout_date: Optional[datetime.datetime] = None
        self._locals_discount: bool = False

    def add_surfboards(self, quantity: int = 1) -> str:
        if self._num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self._num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    @property
    def checkout_date(self) -> Optional[datetime.datetime]:
        return self._checkout_date

    @checkout_date.setter
    def checkout_date(self, date:datetime.datetime) -> None:
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        self._checkout_date = date

    @property
    def locals_discount(self) -> bool:
        return self._locals_discount

    @locals_discount.setter
    def locals_discount(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError('Should input True or False')
        self._locals_discount = value

    def apply_locals_discount(self) -> bool:
        self.locals_discount = True
        return self._locals_discount
