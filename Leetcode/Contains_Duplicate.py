def contains_duplicate1(nums):   #Use Two loops 
    """
    LeetCode 217. Contains Duplicate
    给你一个整数数组 nums，如果任一值在数组中出现至少两次，返回 true；如果数组中每个元素互不相同，返回 false。
    
    仅包含「测试失败场景」的用例（即你的代码若逻辑有误，会触发这些用例失败）：
    >>> contains_duplicate1([1, 2, 3, 1])  # 存在重复（末尾与开头重复）→ 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # 多处重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate1([2, 14, 18, 22, 22])  # 末尾两个重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate1([-1, -2, -3, -1])  # 负数重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate1([0, 0])  # 两个 0 重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate1([1, 2, 3, 4])  # 无重复 → 预期 False，若返回 True 则失败
    False
    >>> contains_duplicate1([1])  # 单个元素（无重复）→ 预期 False，若返回 True 则失败
    False
    >>> contains_duplicate1([-1, 2, -1, 4])  # 负数与正数混合重复 → 预期 True，若返回 False 则失败
    True
    """

    if len(nums) <= 1:
        return False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate2(nums):  # Use hash_set
    """
    LeetCode 217. Contains Duplicate
    给你一个整数数组 nums，如果任一值在数组中出现至少两次，返回 true；如果数组中每个元素互不相同，返回 false。
    
    仅包含「测试失败场景」的用例（即你的代码若逻辑有误，会触发这些用例失败）：
    >>> contains_duplicate2([1, 2, 3, 1])  # 存在重复（末尾与开头重复）→ 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # 多处重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate2([2, 14, 18, 22, 22])  # 末尾两个重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate2([-1, -2, -3, -1])  # 负数重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate2([0, 0])  # 两个 0 重复 → 预期 True，若返回 False 则失败
    True
    >>> contains_duplicate2([1, 2, 3, 4])  # 无重复 → 预期 False，若返回 True 则失败
    False
    >>> contains_duplicate2([1])  # 单个元素（无重复）→ 预期 False，若返回 True 则失败
    False
    >>> contains_duplicate2([-1, 2, -1, 4])  # 负数与正数混合重复 → 预期 True，若返回 False 则失败
    True
    """    
    hash_set = set()
    for num in nums:
        if num in hash_set:
            return True
        hash_set.add(num)

    return False
        

