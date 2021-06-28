# write your code here
matrix = []

for i in range(0, 3):
    m = []
    for j in range(0, 3):
        m.append(" ")
    matrix.append(m)

print("---------")
for c in matrix:
    print("|", end=" ")
    for m in c:
        print(m, end=" ")
    print("|")
print("---------")


def find_winner(player_name: str, board: list):
    if board[0][0] == board[1][1] == board[2][2] == player_name:
        return '{} wins'.format(player_name)
    elif board[0][2] == board[1][1] == board[2][0] == player_name:
        return '{} wins'.format(player_name)
    else:
        for x_i in range(0, 3):
            cnt = 0
            for y_j in range(0, 3):
                if board[x_i][y_j] == player_name:
                    cnt += 1

            if cnt == 3:
                return '{} wins'.format(player_name)
        for y_j in range(0, 3):
            cnt = 0
            for x_i in range(0, 3):
                if board[x_i][y_j] == player_name:
                    cnt += 1

            if cnt == 3:
                return '{} wins'.format(player_name)


player = 'X'
filled = 0
while True:
    try:
        x, y = input("Enter the coordinates: ").split()
        x = int(x) - 1
        y = int(y) - 1
    except ValueError:
        print("You should enter numbers!")
        continue

    if (x > 2) or (y > 2):
        print("Coordinates should be from 1 to 3!")
        continue

    if matrix[x][y] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    matrix[x][y] = player

    print("---------")
    for c in matrix:
        print("|", end=" ")
        for m in c:
            print(m, end=" ")
        print("|")
    print("---------")

    winner = find_winner(player, matrix)
    if winner:
        print(winner)
        break
    player = 'X' if player != 'X' else 'O'
    filled += 1

    if filled == 9:
        print('Draw')
        break
