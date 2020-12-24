def solution(nums):
    get_num = len(nums) // 2
    nums = set(nums)

    if get_num > len(nums):
        return len(nums)
    return get_num