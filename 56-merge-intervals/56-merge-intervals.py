class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        
        if len(intervals)==1:
            return intervals
        
        res = []
        
        for i in range(1, len(intervals)):
            if len(res)==0:
                if intervals[i-1][1]>=intervals[i][0]:
                    nn = [min(intervals[i-1][0],intervals[i][0]), max(intervals[i-1][1],intervals[i][1])]
                    res.append(nn)
                else:
                    res.append(intervals[i-1])
                    res.append(intervals[i])
            else:
                if res[-1][1]>=intervals[i][0]:
                    nn = [min(res[-1][0],intervals[i][0]), max(res[-1][1],intervals[i][1])]
                    res.pop()
                    res.append(nn)
                else:
                    res.append(intervals[i])
            
        return res