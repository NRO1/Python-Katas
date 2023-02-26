
def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    single_mat = []

    if (rows != None):
        rows +=1

    for lst in mat[0:rows]:
        for num in lst[0:]:
            single_mat.append(num)
            print(single_mat)
        
    avg = sum(single_mat) / len(single_mat)
    return avg


mat = [[1,2,3],[1,2,3],[4,5,6]]
x = matrix_avg(mat)
print(x)

        