# Sliding window, boundary - 3000 ms

class RecentCounter:

    def __init__(self):
        self.pings = []
    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[0] + 3000 < self.pings[-1]:
            self.pings.pop(0)
        return len(self.pings)