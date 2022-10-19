class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        first = second = third = 0
        while third < n:
            while chars[second] == chars[third]:
                third += 1
                if third >= n:
                    break
            
            chars[first] = chars[second]
            first += 1
            ls = list(str(third-second))
            if third - second > 1:
                for i in ls:
                    chars[first] = i
                    first += 1
                
            second = third
        return first