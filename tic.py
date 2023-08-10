# Game board
board = [[' ', ' ', ' '], 
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Print the game board
def print_board(board):
  for row in board:
    print('| ' + ' | '.join(row) + ' |')

# Handle player's move with input validation  
def player_move(board, player):
  
  while True:
    print(f"\n{player}'s turn!")
    row = input("Enter row (0, 1, or 2): ")
    col = input("Enter column (0, 1, or 2): ")
    
    if row.isdigit() and col.isdigit():
      row = int(row)
      col = int(col)
      
      if row >= 0 and row < 3 and col >= 0 and col < 3:
        if board[row][col] == ' ':
          board[row][col] = player
          break
        else:
          print("That space is already occupied!") 
      else:
        print("Invalid input. Please enter a value between 0 and 2.")
    else:
      print("Invalid input. Please enter a valid number.")
      
# Check for winner  
def check_win(board, player):
  # Check rows
  for row in board:
    if len(set(row)) == 1 and row[0] == player:
      return True

  # Check columns
  for i in range(len(board)):
    col = [row[i] for row in board]
    if len(set(col)) == 1 and col[0] == player:
      return True

  # Check diagonals
  diag1 = [board[i][i] for i in range(len(board))]
  diag2 = [board[i][len(board)-1-i] for i in range(len(board))]
  if len(set(diag1)) == 1 and diag1[0] == player:
    return True
  if len(set(diag2)) == 1 and diag2[0] == player:
    return True

  return False

# Check for tie
def check_tie(board):
  for row in board:
    if ' ' in row:
      return False
  
  return True

# Main game loop  
player = 'X'
while True:

  print_board(board)
  
  player_move(board, player)
  
  if check_win(board, player):
    print(f"\n{player} wins!")
    break
  
  if check_tie(board):
    print("\nIt's a tie!")
    break
    
  # Switch player
  if player == 'X':
    player = 'O'
  else:
    player = 'X'
