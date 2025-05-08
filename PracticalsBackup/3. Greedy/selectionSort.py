def selectionSort(arr):
    def heuristic(arr):
        sorted_arr = sorted(arr)
        heuristic_values = [abs(arr.index(x) - sorted_arr.index(x)) for x in arr]
        return heuristic_values
    
    print("Heuristic is used to calculate the distance of each element from its target sorted position.")
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: Array: {arr} | Heuristic: {heuristic(arr)}")
    
    return arr

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
sorted_array = selectionSort(arr)
print("Sorted Array:", sorted_array)

# shravanbobade@Shravans-Laptop 3. Greedy % python selectionSort.py
# Enter the array elements separated by space:  5 8 4 2 6 5 1 8 15 20 41 
# Heuristic is used to calculate the distance of each element from its target sorted position.
# Step 1: Array: [1, 8, 4, 2, 6, 5, 5, 8, 15, 20, 41] | Heuristic: [0, 5, 0, 2, 1, 2, 2, 5, 0, 0, 0]
# Step 2: Array: [1, 2, 4, 8, 6, 5, 5, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 3, 1, 2, 2, 3, 0, 0, 0]
# Step 3: Array: [1, 2, 4, 8, 6, 5, 5, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 3, 1, 2, 2, 3, 0, 0, 0]
# Step 4: Array: [1, 2, 4, 5, 6, 8, 5, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
# Step 5: Array: [1, 2, 4, 5, 5, 8, 6, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
# Step 6: Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Step 7: Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Step 8: Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Step 9: Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Step 10: Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Step 11: Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41] | Heuristic: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Sorted Array: [1, 2, 4, 5, 5, 6, 8, 8, 15, 20, 41]
# shravanbobade@Shravans-Laptop 3. Greedy % 