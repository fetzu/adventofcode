# AoC 2023, Day 3: Neighborhood Mechanic // Part 1

f = open("03_data.txt","r")
input = f.read()

def is_adjacent_to_symbol(grid, row, col, num_length):
    rows = len(grid)
    cols = len(grid[0])
    
    # Define the directions to check (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Check all positions around the number
    for i in range(num_length):
        for dr, dc in directions:
            r, c = row + dr, col + dc + i
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] not in '0123456789.':
                    return True
    return False

def find_adjacent_numbers(input_str):
    grid = input_str.strip().split('\n')
    adjacent_numbers = []
    
    for row in range(len(grid)):
        col = 0
        while col < len(grid[row]):
            if grid[row][col].isdigit():
                # Find the full number
                num_start = col
                while col < len(grid[row]) and grid[row][col].isdigit():
                    col += 1
                num_length = col - num_start
                number = int(grid[row][num_start:col])
                
                # Check if the number is adjacent to a symbol
                if is_adjacent_to_symbol(grid, row, num_start, num_length):
                    adjacent_numbers.append(number)
            else:
                col += 1
    
    return adjacent_numbers

numbers = find_adjacent_numbers(input)
result = sum(numbers)
print(result)