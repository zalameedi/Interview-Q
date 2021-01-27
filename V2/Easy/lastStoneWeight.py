class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x = max(stones)
            stones.remove(max(stones))
            y = max(stones)
            stones.remove(max(stones))
            if x == y:
                pass
            elif x != y:
                stones.append(x-y)
        if len(stones) > 0:
            return stones[0]
        return 0