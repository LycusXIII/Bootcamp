'''
Generates a random grid of 5x5 containing either - or # each slot.
To represent a grid, like in minesweeper. After the generated grid,
another grid is made that shows the number of adjacent mines at each
safe spot represented by a '-' in the generated grid.
'''


def show_grid(s_grid):
    '''
    Takes in the generated grid from make_grid() and counts the mines
    and shows the number of adjacent mines indicated for each safe spot.
    Args:
        grid(2d list): The generated 2d list from make_grid() function.
    Returns:
        A new list with the same dimensions as the one from make_grid()
        function each slot is either the number of adjacent mines or the
        mine represented by the '#'
    '''
    # Gets the length of rows and columns from s_grid (2d list)
    s_rows, s_cols = len(s_grid), len(s_grid[0])

    # Makes a new grid to store the updated information.
    new_grid = []
    for _ in range(s_rows):
        s_row = ['X'] * s_cols
        new_grid.append(s_row)

    # Checks each row, slot by slot if its '#' or not
    for row_index, s_row in enumerate(s_grid):
        for col_index, slot in enumerate(s_row):
            if slot == '#':
                new_grid[row_index][col_index] = '#'
            else:
                mines = mine_counter(s_grid, row_index, col_index)
                new_grid[row_index][col_index] = mines
    return new_grid


def mine_counter(m_grid, m_row, m_col):
    '''
    Counts the adjacent mines surrounding the current slot in the grid.
    Args:
        m_grid: a 2d list containing either '-' or '#' at each slot
        m_row: the row index of the current slot
        m_col: the column index of the current slot
    Returns:
        The number of adjacent mines to the current slot
    '''
    m_rows, m_cols = len(m_grid), len(m_grid[0])
    mine_count = 0
    # NW position   N position   NE position
    #  W position        X        E position
    # SW position   S position   SE position
    # X = the current position
    # Iterates through all surrounding slots
    # https://shorturl.at/T8gnt
    # https://shorturl.at/nUyio
    for row_offset, col_offset in enumerate([(-1, -1), (-1, 0), (-1, 1),
                                             (0, -1),           (0, 1),
                                             (1, -1),  (1, 0),  (1, 1)]):
        # Unpacks the offset tuple
        row_offset, col_offset = col_offset
        new_row = m_row + row_offset
        new_col = m_col + col_offset
        # Checks if its still within boundaries and not the current slot
        if 0 <= new_row < m_rows and 0 <= new_col < m_cols:
            if m_grid[new_row][new_col] == '#':
                mine_count += 1
    return mine_count


grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]
print("Example input:")
# Prints the example grid in a more readable format.
for row in grid:
    for col in row:
        print(col, end=" ")
    print()
# Prints the changed grid in a more readable format.
print("Output:")
updated_grid = show_grid(grid)
for u_row in updated_grid:
    for u_col in u_row:
        print(u_col, end=' ')
    print()
