def maxSubArray(arr):
    if not arr:
        return 0, []

    max_so_far = arr[0]
    current_max = arr[0]
    start_index = 0
    end_index = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            temp_start = i
        else:
            current_max += arr[i]

        if current_max > max_so_far:
            max_so_far = current_max
            start_index = temp_start
            end_index = i

    subarray = []
    for i in range(start_index, end_index + 1):
        subarray.append(arr[i])
        
    print("The sub array is:", subarray)
    return max_so_far
