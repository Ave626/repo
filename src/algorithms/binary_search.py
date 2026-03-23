def binary_search(massiv,item):
    start = 0
    end = len(massiv) - 1
    while start <= end:
        mid = (end + start) // 2
        guess = massiv[mid]
        if guess == item:
            return mid
        if guess > item:
            end = mid - 1
        elif guess < item:
            start = mid + 1
    return None


if __name__ == "__main__":
    print("Введите количество чисел")
    n = int(input())
    massive = []
    for i in range(n):
        print(f"Введите число №{i+1}")
        massive.append(int(input()))
    massive.sort()
    print("Введите число для поиска")
    item = int(input())
    print(f"Отсортированный массив чисел {massive}")
    result = binary_search(massive,item)
    if result is not None:
        print(f"Элемент найден на позиции {result}")
    else:
        print("Элемента нет в массиве")
    print("О(log(n))")