class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def getMinFinishTime(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:

            minEndFirst = min(s + d for s, d in zip(start1, dur1))

            return min(max(s, minEndFirst) + d for s, d in zip(start2, dur2))

        landFirst = getMinFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
        waterFirst = getMinFinishTime(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(landFirst, waterFirst)


        