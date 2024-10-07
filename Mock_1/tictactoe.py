def get_cell(row, col):
    if row < 0 or row >= grid_size or col < 0 or col >= grid_size:
        return '.'
    return game_grid[row][col]

def detect_winner(player_index, player_symbol):
    for direction in range(4):
        for row in range(grid_size):
            for col in range(grid_size):
                if get_cell(row - row_directions[direction], col - col_directions[direction]) != player_symbol:
                    line_length = 0
                    while get_cell(row + line_length * row_directions[direction], col + line_length * col_directions[direction]) == player_symbol:
                        line_length += 1
                    
                    if line_length >= min_length:
                        winning_lines[player_index] += 1
                        for i in range(line_length):
                            if i < min_length and min_length + i >= line_length:
                                winning_positions[player_index][row + i * row_directions[direction]][col + i * col_directions[direction]] += 1

grid_size, min_length = map(int, input().split())
game_grid = [list(input().strip()) for _ in range(grid_size)]

marked_count = [0, 0]
last_player = 0
is_full = True
winning_lines = [0, 0]
winning_positions = [[[0] * 1000 for _ in range(1000)] for _ in range(2)]
row_directions = [1, 1, 0, -1]
col_directions = [0, 1, 1, 1]

for i in range(grid_size):
    for j in range(grid_size):
        if game_grid[i][j] == 'X':
            marked_count[0] += 1
        elif game_grid[i][j] == 'O':
            marked_count[1] += 1
        else:
            is_full = False

if marked_count[0] == marked_count[1]:
    last_player = 1
elif marked_count[0] == marked_count[1] + 1:
    last_player = 0
else:
    print("ERROR")
    exit()

for player_index in range(2):
    detect_winner(player_index, "XO"[player_index])

if winning_lines[1 - last_player] != 0:
    print("ERROR")
    exit()

if winning_lines[last_player] == 0:
    if is_full:
        print("DRAW")
    else:
        print("IN PROGRESS")
    exit()

is_valid = False
for i in range(grid_size):
    for j in range(grid_size):
        if winning_positions[last_player][i][j] == winning_lines[last_player]:
            is_valid = True

if not is_valid:
    print("ERROR")
else:
    print(f"{'XO'[last_player]} WINS")
