def merge(arr1, arr2, n, m):
    # Function to calculate next gap
    def nextGap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = n + m
    while gap > 0:
        gap = nextGap(gap)

        # Compare elements in first array
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare elements in both arrays
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare elements in second array
        if j < m:
            k = j
            while k + gap < m:
                if arr2[k] > arr2[k + gap]:
                    arr2[k], arr2[k + gap] = arr2[k + gap], arr2[k]
                k += 1


# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2, len(arr1), len(arr2))

print("arr1 =", arr1)
print("arr2 =", arr2)
