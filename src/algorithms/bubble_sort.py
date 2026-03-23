def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j + 1],arr[j]
    return arr


if __name__ == "__main__":
    print("Введите количество элементов")
    n = int(input())
    arr = []
    for i in range(n):
        print(f"Введите элемент #{i+1}")
        item = int(input())
        arr.append(item)
    new = bubble_sort(arr)
    print(new)