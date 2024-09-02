class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        frequency = len(set(candyType))

        canEatCandies = len(candyType) // 2

        return min(frequency, canEatCandies)
