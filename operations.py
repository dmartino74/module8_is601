import logging

def add(a: float, b: float) -> float:
    logging.info(f"Adding {a} + {b}")
    return a + b

def subtract(a: float, b: float) -> float:
    logging.info(f"Subtracting {a} - {b}")
    return a - b

def multiply(a: float, b: float) -> float:
    logging.info(f"Multiplying {a} * {b}")
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        logging.error("Attempted division by zero")
        raise ValueError("Cannot divide by zero!")
    logging.info(f"Dividing {a} / {b}")
    return a / b
