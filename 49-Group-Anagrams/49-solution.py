class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for item in strs:
            item_sorted = "".join(sorted(item))
            if item_sorted in dic:
                dic[item_sorted].append(item)
            else:
                dic[item_sorted] = [item]
        return dic.values()