def findSingleNumberBS(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                left = mid + 2
            else:
                right = mid
        else:
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid

    return arr[left]
