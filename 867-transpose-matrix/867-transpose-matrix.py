class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        result = []
        for i in range(0,column):
            new_row = []
            for j in range(0,row):
                new_row.append(matrix[j][i])
            result.append(new_row)
        
        return result