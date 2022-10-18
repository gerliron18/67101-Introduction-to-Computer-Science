from ex11_sudoku import board_list

def check_no_dups(nineGrouping):
    uniqueDigits = set()
    for num in nineGrouping:
        if num != 0:
            if num in uniqueDigits:
                return False
        uniqueDigits.add(num)
    return True


def check_row(grid, row):
    nineGrouping = []
    for cell in grid[row]:
        nineGrouping.append(cell)
    return check_no_dups(nineGrouping)


def check_column(grid, column):
    nineGrouping = []
    for row in grid:
        nineGrouping.append(row[column])
    return check_no_dups(nineGrouping)


def check_subgrid(grid, row, column):
    nineGrouping = []
    for i in range(row, row + 3):
        for j in range(column, column + 3):
            nineGrouping.append(grid[i][j])
    return check_no_dups(nineGrouping)


def check_sudoku(grid):
    for i in range(0, 9):
        if not check_row(grid, i):
            return False
        if not check_column(grid, i):
            return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not check_subgrid(grid, i, j):
                return False
    return True

print(check_sudoku(board_list))