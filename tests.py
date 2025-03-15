import surfshop
import unittest
from datetime import datetime, timedelta

class SurfShopSystemTest(unittest.TestCase):

#Create a fresh ShoppingCart instance before each test
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    #Test adding 1 surfboards
    def test_add_surfboard(self):
        result = self.cart.add_surfboards(1)
        self.assertEqual(
            result,
            'Successfully added 1 surfboard to cart!',
            msg=f"Expected successful message for adding 1 surfboard, but got {result}")

    # Test adding exactlly 4 surfboards, the max limit
    def test_add_four_surfboards(self):
        result = self.cart.add_surfboards(4)
        self.assertEqual(
            result,
            'Successfully added 4 surfboards to cart!',
            msg=f'Expected successful message for adding 4 surfboards, but got {result}'
        )

    #Test that adding 2-5 surfboards
    def test_add_more_surfboards(self):
        for num in range(2,5):
            with self.subTest(num):
                self.cart = surfshop.ShoppingCart()
                expect_result = f'Successfully added {num} surfboards to cart!'
                self.assertEqual(
                    self.cart.add_surfboards(num),
                    expect_result,
                    f'Adding {num} surfboards failed.')

    # Test that adding more than 4 surfboards raises an error
    def test_add_too_many_surfboards(self):
        with self.assertRaises(surfshop.TooManyBoardsError, msg='Should raise TooManyBoardsErrors when adding more than 4 surfboards'):
            self.cart.add_surfboards(5)

    #Test adding surfboards multiple times and more than 4 in total
    def test_add_surfboards_sequentially(self):
        self.cart.add_surfboards(2)
        self.cart.add_surfboards(2)
        with self.assertRaises(surfshop.TooManyBoardsError, msg='Should Raise TooManyBoardsError when adding more than 4 surfboards multiple times'):
            self.cart.add_surfboards(3)

    # Test setting a valid future check out date
    def test_set_valid_checkout_date(self):
        future_time = datetime.now() + timedelta(days=3)
        self.cart.checkout_date = future_time
        self.assertEqual(
            self.cart.checkout_date,
            future_time,
            msg=f'Should set checkout date successfully, but got {self.cart.checkout_date}')

    # Test setting a past date raises CheckoutDateError
    def test_check_out_invalid_date(self):
        past_time = datetime.now() - timedelta(days=5)
        with self.assertRaises(surfshop.CheckoutDateError, msg='Should raise CheckoutDateError when setting a past date'):
            self.cart.checkout_date = past_time

    # Test setting a present date raises CheckoutDateError
    def test_check_out_now_date(self):
        now_time = datetime.now()
        with self.assertRaises(surfshop.CheckoutDateError, msg='Should raise CheckoutDateError when setting a present date'):
            self.cart.checkout_date = now_time

    def test_apply_local_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(
            self.cart._locals_discount,
            "Local discount should be set to True after applying the discount")

unittest.main()
