class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)

        for x in strs:
            alphabet = [0]*26
            for c in x:
                alphabet[ord(c)-ord('a')] += 1

            lists[tuple(alphabet)].append(x)

        return list(lists.values())

