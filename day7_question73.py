class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        flag = False

        for row in range(rows):
            if matrix[row][0] == 0 :
                flag = True

            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0


        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        #here if [0,0] == 0 then set the row[0] = 0 and col[0] = 0

        if matrix[0][0] ==0:
            for col in range(cols):
                matrix[0][col] = 0

        if flag == True:
            for i in range(rows):
                matrix[row][0] = 0
        
