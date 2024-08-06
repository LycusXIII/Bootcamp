'''
Generates a random grid of 5x5 containing either - or # each slot.
To represent a grid, like in minesweeper. After the generated grid,
another grid is made that shows the number of adjacent mines at each
safe spot represented by a '-' in the generated grid.
'''
import random


def make_grid():
    '''
    Generates a randomized grid with predefined rows and columns
    Args:
        None
    Returns:
        generated_grid (list): a generated 2D list with 5 rows and 5
        columns with randomized data of '-' or '#'
    '''
    rows = 5
    cols = 5
    generated_grid = []

    # Generates a grid based on rows and cols with randomized values
    # for each slot
    for _ in range(rows):
        row_list = []
        for _ in range(cols):
            # Randomizes between '-' or '#' then appends it to the list
            slot = random.choice(["-", "#"])
            row_list.append(slot)
        generated_grid.append(row_list)
    return generated_grid


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
        row = ['X'] * s_cols
        new_grid.append(row)
    # Checks each row, slot by slot if its '#' or not
    for row_index, row in enumerate(s_grid):
        for col_index, slot in enumerate(row):
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
        if 0 <= new_row < m_rows and 0 <= new_col < m_cols and (
            new_row, new_col) != (m_row, m_col):
            if m_grid[new_row][new_col] == '#':
                mine_count += 1
    return mine_count


grid = make_grid()
print("Generated grid:")
for g_row in grid:
    for g_col in g_row:
        print(g_col, end=' ')
    print()

updated_grid = show_grid(grid)
print("Updated grid:")
for u_row in updated_grid:
    for u_col in u_row:
        print(u_col, end=' ')
    print()
