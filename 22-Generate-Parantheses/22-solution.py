class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(bracket, opening, ending):
            if len(bracket) == 2*n and opening == 0 and ending == 0:
                result.append("".join(bracket))
                return
            
            if opening > 0:
                bracket.append("(")
                opening -= 1
                generate(bracket, opening, ending)
                bracket.pop()
                opening += 1
            if ending > 0 and ending > opening:
                bracket.append(")")
                ending -= 1
                generate(bracket, opening, ending)
                bracket.pop()
                ending += 1
                
        result = []
        generate([], n, n)
        return result