from random import randint


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot: int = array[0]

    updated_array: list = array[1:]
    less: list = [item for item in updated_array if item <= pivot]
    greater: list = [item for item in updated_array if item > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    array: list = [randint(0, 50) for i in range(10)]
    result: list = quick_sort(array)
    print(f"Input array: {array}")
    print(f"Sorted array: {result}")
