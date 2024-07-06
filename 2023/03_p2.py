# AoC 2023, Day 3: Claude, the friently Neighborhood Mechanic // Part 1

f = open("03_data.txt","r")
input = f.read()

def find_gear_ratios(input_str):
    grid = input_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    gear_ratios = []

    def get_full_number(r, c):
        # Find the start of the number
        while c > 0 and grid[r][c-1].isdigit():
            c -= 1
        # Extract the full number
        num = ''
        while c < cols and grid[r][c].isdigit():
            num += grid[r][c]
            c += 1
        return int(num) if num else None

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '*':
                adjacent_numbers = []
                # Check all adjacent positions
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        r, c = row + dr, col + dc
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c].isdigit():
                            num = get_full_number(r, c)
                            if num and num not in adjacent_numbers:
                                adjacent_numbers.append(num)
                
                # If exactly two numbers are adjacent, calculate and store the gear ratio
                if len(adjacent_numbers) == 2:
                    gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])

    return gear_ratios

result = find_gear_ratios(input)
print("Gear ratios:", result)
print("Sum of gear ratios:", sum(result))