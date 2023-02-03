test_matrix_true = [[5,5,5],[5,5,5],[5,5,5]]
test_matrix_false = [[3,3,3],[3,3,3],[3,3,3]]

def create_matrix(ask_standard):
    if ask_standard == "y":
        n_rows = 3
        n_cols = 3
    else:
        n_rows = int(input("Enter number of rows: "))
        n_cols = int(input("Enter number of columns: "))
# initialise matrix
    matrix = []

    # create matrix
    for i in range(n_rows):
        matrix.append([])
        for j in range(n_cols):
            matrix[i].append(int(input("Enter element" + "["+str(i+1)+","+str(j+1)+"]" + ": ")))
    return matrix

def ask_to_enter_matrices(ask_standard):
    matrices = []
    add_another = True
    while add_another:
        matrices.append(create_matrix(ask_standard))
        add_another = input("Do you want to create another matrix? (y/n) ")
        if add_another == 'y':
            add_another = True
        else:
            add_another = False
    return matrices

def check_if_rows_add_to_15(matrix):
    for row in matrix:
        if sum(row) != 15:
            return False
    return True


def check_if_columns_add_to_15(matrix):
    for i in range(len(matrix)):
        column_sum = 0
        for row in matrix:
            column_sum += row[i]
        if column_sum != 15:
            return False
    return True

def check_if_T(matrix):
    return check_if_rows_add_to_15(matrix) and check_if_columns_add_to_15(matrix)

def stringify(matrix):
    string = ""
    for row in matrix:
        string += str(row) + "\n"
    return string

def app():
    ask_standard = input("Do you want to use the standard matrix 3x3? (y/n) ")
    matrices = ask_to_enter_matrices(ask_standard)
    for i in range(len(matrices)):
        name = "Matrix " + str(i+1) + "\n"
        if check_if_T(matrices[i]):
            print(name + stringify(matrices[i]), "is a T matrix\n")
        else:
            print(name + stringify(matrices[i]), "is NOT a T matrix\n")


app()