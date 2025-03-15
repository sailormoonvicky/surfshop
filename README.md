# SurfShop Shopping Cart Unit Testing

## Overview
This project is designed to demonstrate unit testing practices in Python for a **surf shop's shopping cart** software. It includes various tests that check the behavior of the shopping cart system, focusing on **error handling**, **validation**, and **correctness**.

The **shopping cart** functionality includes:

- Adding surfboards to the cart (up to 4 boards).
- Setting a checkout date (which must be a future date).
- Applying a local discount to the cart.

The project exercises key concepts such as:

- Custom exception handling (`TooManyBoardsError`, `CheckoutDateError`).
Unit testing using the **unittest** module in Python.

## Files

- **`surfshop.py`**: Contains the implementation of the `ShoppingCart` class and custom error classes.
- **`tests.py`**: Contains unit tests for validating the shopping cart logic.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/sailormoonvicky/surfshop.git
    ```

2. Navigate into the project directory:
    ```bash
    cd surfshop
    ```


## Running the Tests

The project uses the built-in **unittest** framework in Python. To run the tests, use the following command:

```bash
python tests.py
```
