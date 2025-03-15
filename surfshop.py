import datetime

class TooManyBoardsError(Exception):
    def __str__(self):
        return 'Cart cannot have more than 4 surfboards in it!'

class CheckoutDateError(Exception):
    def __str__(self):
        return 'Check out date cannot be past or present!'

class ShoppingCart:
    def __init__(self):
        self._num_surfboards = 0
        self._checkout_date = None
        self._locals_discount = False

    def add_surfboards(self, quantity=1):
        if self._num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self._num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    @property
    def checkout_date(self):
        return self._checkout_date

    @checkout_date.setter
    def checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        self._checkout_date = date

    def apply_locals_discount(self):
        self._locals_discount = True
