import math


def binary_search(array: list, item: int) -> int:
    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        mid: int = math.floor((low + high) / 2)
        guess: int = array[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    arr: list = list(range(1, 11))
    index: int | None = binary_search(arr, 6)
    print(f"Your item index: {index}")  # Your item index: 5
