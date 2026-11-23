def linear_search(collection, target):
    for i in range(len(collection)):
        if collection[i] == target:
            return i
    return -1


def binary_search(collection, target):
    left = 0
    right = len(collection) - 1

    while left <= right:
        mid = (left + right) // 2

        if collection[mid] == target:
            return mid
        elif collection[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def count_linear_search_steps(collection, target):
    steps = 0

    for i in range(len(collection)):
        steps += 1

        if collection[i] == target:
            return steps

    return steps


def count_binary_search_steps(collection, target):
    left = 0
    right = len(collection) - 1
    steps = 0

    while left <= right:
        mid = (left + right) // 2
        steps += 1

        if collection[mid] == target:
            return steps
        elif collection[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return steps


def main():
    print("TEST 1")
    data = [3, 7, 12, 18, 21, 25, 31, 40, 44, 52]
    target = 25

    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print()

    print("TEST 2")
    data = [1, 2, 3, 4, 5]
    target = 1

    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print()

    print("TEST 3")
    data = [1, 2, 3, 4, 5]
    target = 5

    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print()

    print("TEST 4")
    data = [1, 2, 3, 4, 5]
    target = 10

    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))

    print()

    print("TEST 5")
    data = []
    target = 5

    print(linear_search(data, target))
    print(binary_search(data, target))
    print(count_linear_search_steps(data, target))
    print(count_binary_search_steps(data, target))


if __name__ == "__main__":
    main()
