def find_length_of_lcis(nums):
    if not nums:
        return 0

    ans = 1
    max_len = 1

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            max_len += 1
            ans = max(ans, max_len)
        else:
            max_len = 1

    return ans
