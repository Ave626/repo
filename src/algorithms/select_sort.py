def min_value(arr):
    value = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] <= value:
            value = arr[i]
            smallest_index = i
    return smallest_index

def Select_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = min_value(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == "__main__":
    print("Введите количество элементов")
    n = int(input())
    arr = []
    for i in range(n):
        print(f"Введите элемент #{i+1}")
        item = int(input())
        arr.append(item)
    new = Select_sort(arr)
    print(new)