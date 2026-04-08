# Brute Force Approach
# Time Complexity: O(n*k) 

def BrutemaxSubarraySum(arr, k):
    n = len(arr)
    
    if n < k:
        return 0

    max_sum = 0

    # First loop → starting index
    for i in range(n - k + 1):
        current_sum = 0

        # Second loop → sum of k elements
        for j in range(i, i + k):
            current_sum += arr[j]

        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(BrutemaxSubarraySum(arr, k))  # Output: 9


# Optimized Approach (Sliding Window)
# Time Complexity: O(n)

def maxSubarraySum(arr, k):
    n = len(arr)
    if n < k:
        return 0

    max_sum = 0
    window_sum = 0
    low = 0

    # First window
    for high in range(k):
        window_sum += arr[high]

    max_sum = window_sum  # initialize max_sum properly

    # Sliding window
    while high < n - 1:
        high += 1
        window_sum += arr[high]   # add next element
        window_sum -= arr[low]    # remove previous element
        low += 1

        max_sum = max(max_sum, window_sum)

    return max_sum


# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
result = maxSubarraySum(arr, k)
print(result)  # Output: 9