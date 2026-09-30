class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in seen:
                seen[s].append(i)
            else: seen[s] = [i]
        return list(seen.values())