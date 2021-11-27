def rotate_90_clock(mat):
    #step1 transpose the matrix
    row_size = len(mat)
    col_size = len(mat[0])

    for i in range(row_size):
        #once you swap you dont want to iterate that element again and swap it back. Therefore, loop from i to end
        for j in range(i,col_size):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


    #step2 Flip Horizontally/columns

    for i in range(row_size):
        #you want flip each column with its last columns ex: flip 1 with 4, 2 with 3 in case 4x4
        for j in range(int(col_size/2)):
            #right side columns can be indexed like usual but on the left side it starts from the end and then loops backwards like N-1-j
            mat[i][j], mat[i][row_size-1-j] = mat[i][row_size-1-j],mat[i][j]

    return mat

    


def rotate_90_anti(mat):
    #step1 transpose the matrix
    row_size = len(mat)
    col_size = len(mat[0])

    for i in range(row_size):
        #once you swap you dont want to iterate that element again and swap it back. Therefore, loop from i to end
        for j in range(i,col_size):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    print("transposed mat = ", mat)

    #step2 flip verticallt/rows

    for i in range(int(row_size/2)):
        for j in range(col_size):
            mat[i][j],mat[row_size-1-i][j] = mat[row_size-1-i][j], mat[i][j]

    return mat

def transpose(matrix):
    # Transpose O(N*N)
    size = len(matrix)
    for i in range(size):
        for j in range(i+1, size):
            matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
    return matrix




if __name__ == "__main__":
    #test1 rotateby90clock 3x3
    matrix_test = [[1,2,3], [4,5,6], [7,8,9]]
    matrix_rotated = rotate_90_clock(matrix_test)

    #test2 roateby90clock 4x4
    matrix_test2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    matrix_rotated2 = rotate_90_clock(matrix_test2)

    #test3 rotatebyanticlock 3x3
    matrix_test3 = [[1,2,3], [4,5,6], [7,8,9]]
    matrix_rotated_anti = rotate_90_anti(matrix_test3)
