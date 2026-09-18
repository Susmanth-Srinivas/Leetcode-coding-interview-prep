class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # if merged is empty OR current interval doesn't overlap with last one
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # overlap: extend the end of the last merged interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged