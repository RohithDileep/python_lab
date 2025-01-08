def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
bubble_sort(arr)
print("Sorted list:", arr)
