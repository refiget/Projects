def is_anagram(s, t):
    """
    LeetCode 242. Valid Anagram
    给定两个字符串 s 和 t，编写一个函数来判断 t 是否是 s 的字母异位词（字符种类和数量完全相同，顺序不同）。

    仅包含「测试失败场景」的用例（代码逻辑有误时会触发失败）：
    >>> is_anagram("anagram", "nagaram")  # 基础：字母全匹配（顺序不同）→ 预期 True，错返 False 失败
    True
    >>> is_anagram("rat", "car")          # 基础：字母种类不同 → 预期 False，错返 True 失败
    False
    >>> is_anagram("a", "ab")             # 边界：长度不同 → 预期 False，错返 True 失败
    False
    >>> is_anagram("", "")                # 边界：空字符串 → 预期 True，错返 False 失败
    True
    >>> is_anagram("aacc", "ccac")        # 易错：字母数量不匹配（a 多1个）→ 预期 False，错返 True 失败
    False
    >>> is_anagram("abc", "cba")          # 基础：全不同顺序 → 预期 True，错返 False 失败
    True
    >>> is_anagram("xyz", "xyza")         # 边界：长度差1（多1个字符）→ 预期 False，错返 True 失败
    False
    >>> is_anagram("abba", "baab")        # 易错：重复字母不同顺序 → 预期 True，错返 False 失败
    True
    >>> is_anagram("test", "tset")        # 基础：普通字符串 → 预期 True，错返 False 失败
    True
    >>> is_anagram("hello", "llleo")      # 易错：字母数量匹配（l 2个）→ 预期 True，错返 False 失败
    False
    """

    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for j in t:
        if j in count:
            count[j] -= 1
            if count[j] < 0:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
