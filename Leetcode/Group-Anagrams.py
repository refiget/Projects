# Given an array of strings strs, group the anagrams together.
# You may return the answer in any order
def group_anagrams(strs):
    """
    将变位词分组

    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    >>> group_anagrams(["", "a", "", "a"])
    [['', ''], ['a', 'a']]
    >>> group_anagrams(["hello"])
    [['hello']]
    >>> group_anagrams(["abc", "def", "ghi"])
    [['abc'], ['def'], ['ghi']]
    >>> group_anagrams(["aab", "aba", "baa", "aab"])
    [['aab', 'aba', 'baa', 'aab']]
    """
    group_dict = {}
    for str in strs:
        key = "".join(sorted(str))
        group_dict.setdefault(key, []).append(str)
    return list(group_dict.values())


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
