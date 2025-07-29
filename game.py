rows, cols = (3, 3)
import random
import time

game = 0

def generete_board():
    global board
    board = [[0 for col in range(cols)] for row in range(rows)]

def show_board():
    shown_board = [["" for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for column in range (cols):
            if board[row][column] == 1:
                shown_board[row][column] = "O"
            elif board[row][column] == -1:
                shown_board[row][column] = "X"
            else :
                shown_board[row][column] = "-"
    
    for row in shown_board:
        print(row)

def greetings():
    print("===================================Welcome===================================")
    print("===========To start a game enter a position (xy) to place your bet===========")
    print("=============================================================================")

def calculate_xy():
    x=xy//10
    y=xy%10
    return x, y

def enter_positon():
    global xy, game
    
    while True:
        try:
            xy = int(input('Enter position:'))
            x, y = calculate_xy()
            print(f'Your postion is {xy}')

        except ValueError:
            print(f'You entered object, which is not a positive number.')
            continue

        try:
            if board[x][y]==1 or board[x][y]==-1:
                print("=============================Already occupied=============================")
                continue
            else:
                board[x][y]=1
                game+=1
                show_board()
                xy, x, y = 0, 0, 0
                break
        except IndexError:
            print(f'You should enter number in format xy where 0<=xy<=2')
            continue
    
# def return_rand_xy():
#     ox = random.randrange(0, 3)
#     oy = random.randrange(0, 3)
#     return ox, oy

def opponent_move():
    global game
    # ox, oy = return_rand_xy()
    
    # while board[ox][oy]==1 or board[ox][oy]==-1:
    #     ox, oy = return_rand_xy()
    # board[ox][oy]=-1
    move = select_best_move()
    ox = move // 10 
    oy = move % 10
    board[ox][oy] = -1
    print(f'Oppont\'s turn')
    show_board()
    game+=1

def evaluate_board(board_temp):
    results=[]
    results.extend([sum(row) for row in board_temp])
    results.extend([sum(board_temp[r][c] for r in range(rows)) for c in range(cols)])
    results.append(sum(board_temp[i][i] for i in range(rows)))
    results.append(sum(board_temp[i][-i + rows-1] for i in range(rows)))

    for i in results:
        if i == -3:
            return -1
        elif i == 3:
            return 1
    
    for i in range(rows):
        for j in range(cols):
            if board_temp[i][j] == 0:
                return None
        
    return 0 


def minimax(board_temp, is_max, depth=0):
    final_result = evaluate_board(board_temp)
    if final_result is not None:
        if final_result == -1:      # AI wins
            return -10 + depth
        elif final_result == 1:     # Player wins
            return 10 - depth
        else:                 # Draw
            return 0
    
    if is_max == False:
        best_result = float('inf')
        for row in range(rows):
            for col in range(cols):
                if board_temp[row][col] == 0:      
                    board_temp[row][col]= -1
                    minimax_result = minimax(board_temp, True, depth + 1)
                    board_temp[row][col]=0
                    best_result=min(minimax_result, best_result)
        return best_result
    
    else:
        best_result = -float('inf')
        for row in range(rows):
            for col in range(cols):
                if board_temp[row][col] == 0:
                    board_temp[row][col] = 1
                    minimax_result = minimax(board_temp, False, depth + 1)
                    board_temp[row][col] = 0 
                    best_result=max(minimax_result, best_result)
        return best_result
    
def select_best_move():
    moves = []
    best_move = None
    best_move_result = float('inf')

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                board_temp = [r[:] for r in board]
                board_temp[row][col] = -1 
                minimax_result = minimax(board_temp, True)
                minimax_move = row*10+col 
                board_temp[row][col] = 0 
                moves.append([minimax_move, minimax_result])
 
    for move in moves:
        if move[1] < best_move_result:
            best_move = move[0]
            best_move_result = move[1]
    
    print(moves)
    return best_move

def check_board_results(result_board):
    results=[]
    results.extend([sum(row) for row in result_board])
    results.extend([sum(result_board[r][c] for r in range(rows)) for c in range(cols)])
    results.append(sum(result_board[i][i] for i in range(rows)))
    results.append(sum(result_board[i][-i + rows-1] for i in range(rows)))

    for i in results:
        if i == 3:
            print("Player wins")
            time.sleep(3)
            exit()
        elif i == -3:
            print("Oponnent wins")
            time.sleep(3)
            exit()

def check_game_state():
    if game == 9:
            # show_board()
            print("Draw")
            time.sleep(3)
            exit()

def main():
    greetings()
    generete_board()
    show_board()
    
    while game<=9:
        check_game_state()
        enter_positon()
        check_board_results(board)

        check_game_state()
        opponent_move()
        check_board_results(board)

main()