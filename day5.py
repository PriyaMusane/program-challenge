def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Reverse to maintain original order
    return leaders[::-1]


# Example usage
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))
