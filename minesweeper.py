def mine_sweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [['0'] * cols for _ in range(rows)]  # Initialize the result grid with '0's

    # Iterate over each cell in the grid using enumerate to get the row index (i) and element (row)
    for i, row in enumerate(grid):
        # Iterate over each element in the row using enumerate to get the column index (j) and cell value (cell)
        for j, cell in enumerate(row):
            if cell == '-':  # Check if the cell is a mine
                count = 0  # Initialize the count of neighboring mines to 0

                # Iterate over the neighboring cells (including the current cell itself)
                for ni in range(max(0, i - 1), min(rows, i + 2)):
                    for nj in range(max(0, j - 1), min(cols, j + 2)):
                        if grid[ni][nj] == '#':  # Check if the neighboring cell is a mine
                            count += 1  # Increment the count of neighboring mines

                result[i][j] = str(count)  # Update the result grid with the count of neighboring mines as a string

    return result

grid = [
    ['#', '#', '#', '#', '#'],
    ['#', '#', '-', '-', '-'],
    ['#', '-', '#', '-', '-'],
    ['#', '-', '-', '#', '-'],
    ['#', '-', '-', '-', '#']
]

result = mine_sweeper(grid)

# Format and print the result grid with line breaks and indentation
formatted_result = '\n'.join([' '.join(row) for row in result])
print(formatted_result)