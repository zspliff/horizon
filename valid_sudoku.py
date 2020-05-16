import numpy


def check_rows(arr):

    for i in range(9):
        if not is_unique_list(arr[i]):
            return False
    
    return True

def check_cols(arr):
    for i in range(9):
        if not is_unique_list(arr[:, i]):
            return False
    return True

def check_blocks(arr):
    for i in range(0, 9, 3):
        for j in range (0, 9, 3):
            if not check_rows(arr[i:i+3, j:j+3]) and \
                not check_cols(arr[i:i+3, j:j+3]):

                return False
    return True

        
    

def is_unique_list(num_list):
     unique_set = set()
     
     [unique_set.add(i) for i in num_list]
     
     return len(unique_set) == len(num_list)

    
def is_valid(arr):
     if (check_rows(arr)): #and check_cols(arr) and check_blocks(arr)):
        return True
     else:
        return False




if __name__ == "__main__":
    sudoku_board = numpy.array(([1, 2, 3, 9, 6, 7, 6, 5, 4],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [8, 5, 1, 4, 5, 8, 7, 8, 9],
    [5, 8, 9, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]))


    if is_valid(sudoku_board):
        print ("This board is valid")
    else:
        print ("This board is invalid")
