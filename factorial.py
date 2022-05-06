def factorial(number: int) -> int:
    if number <= 0:
        raise Exception("Number must be positive")
    if number == 1:
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    number: int = 5
    result: int = factorial(number)
    print(f"Factorial of {number} is {result}")  # Factorial of 5 is 120
