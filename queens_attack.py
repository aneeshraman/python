def main(dimensions, queen_row, queen_column, obstacles_row, obstacles_column):
	board = []
	for i in range(dimensions):
		board.append([])
		for y in range(dimensions):
			board[-1].append("")
			
	board[queen_row][queen_column] = "Queen"
	for i in range(len(obstacles_row)):
		board[obstacles_row[i]][obstacles_column[i]] = "Obstacle"
	
	return board

first_line = input().split()
board_dimensions = int(first_line[0])
number_of_obstacles = int(first_line[1])
second_line = input().split()
board_queen_row = dimensions - int(second_line[0])
board_queen_column = int(second_line[1]) - 1
board_obstacles_row = []
board_obstacles_column = []

for i in range(number_of_obstacles):
	i_line = input().split()
	board_obstacles_row.append(dimensions - int(i_line[0]))
	board_obstacles_column.append(int(i_line[1]) - 1)

print(main(board_dimensions, board_queen_row, board_queen_column, board_obstacles_row, board_obstacles_column)
