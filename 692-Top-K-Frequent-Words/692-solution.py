class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        w = []
        for item in freq.keys():
            w.append(item)
        heap = []
        answer = []
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
        
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer