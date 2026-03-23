def merge_sort(arr):
    if len(arr) <= 1;
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    print("Введите количество элементов")
    n = int(input())
    arr = []
    for i in range(n):
        print(f"Введите элемент #{i+1}")
        item = int(input())
        arr.append(item)
    new = merge_sort(arr)
    print(new)