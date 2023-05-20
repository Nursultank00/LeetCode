# Делаем словарь, сортим его элементы, потом DFS

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path, d = [], {}
        for i, j in tickets:
            if i not in d:
                d[i] = [j]
            else:
                d[i].append(j)
        
        for key in d:
            d[key].sort()

        def dfs(departure):
            while d[departure]:
                dfs(d[departure].pop(0))
            path.append(departure)
        
        dfs("JFK")
        return path[::-1]