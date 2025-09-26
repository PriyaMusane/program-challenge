def find_zero_sum_subarrays(arr):
    sum_map = {}   # Maps cumulative sum to list of indices
    result = []
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        # Case 1: Subarray from 0 to i sums to zero
        if curr_sum == 0:
            result.append((0, i))

        # Case 2: curr_sum seen before
        if curr_sum in sum_map:
            for start_index in sum_map[curr_sum]:
                result.append((start_index + 1, i))

        # Add current index to the map of the current sum
        sum_map.setdefault(curr_sum, []).append(i)

    return result
