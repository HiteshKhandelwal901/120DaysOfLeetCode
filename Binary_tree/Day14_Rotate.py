def rotate_90_clock(mat):
    #step1 transpose the matrix
    row_size = len(mat)
    col_size = len(mat[0])

    for i in range(row_size):
        #once you swap you dont want to iterate that element again and swap it back. Therefore, loop from i to end
        for j in range(i,col_size):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


    #step2 Flip Horizontally

    for i in range(row_size):
        #you want flip each column with its last columns ex: flip 1 with 4, 2 with 3 in case 4x4
        for j in range(int(col_size/2)):
            #right side columns can be indexed like usual but on the left side it starts from the end and then loops backwards like N-1-j
            mat[i][j], mat[i][row_size-1-j] = mat[i][row_size-1-j],mat[i][j]

    return mat




if __name__ == "__main__":
    matrix_test = [[1,2,3], [4,5,6], [7,8,9]]
    matrix_rotated = rotate_90_clock(matrix_test)
    #print(matrix_rotated)

    matrix_test2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    matrix_rotated2 = rotate_90_clock(matrix_test2)
    print("rotated matrix = ", matrix_rotated2)
