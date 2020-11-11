import sys

def knight_pos(i, king_pos):
    if i[1] < 7 and i[1] > 2:
        if king_pos == [i[0]-1,i[1]-2] or king_pos == [i[0]-2,i[1]-1] or king_pos == [i[0]-2,i[1]+1] or king_pos == [i[0]-1,i[1]+2]:
            return True
        else:
            return False
    elif i[1] == 7:
        if king_pos == [i[0]-1,i[1]-2] or king_pos == [i[0]-2,i[1]-1] or king_pos == [i[0]-2,i[1]+1]:
            return True
        else:
            False
    elif i[1] == 2:
        if king_pos == [i[0]-2,i[1]-1] or king_pos == [i[0]-2,i[1]+1] or king_pos == [i[0]-1,i[1]+2]:
            return True
        else:
            False
    elif i[1] == 1:
        if king_pos == [i[0]-2,i[1]+1] or king_pos == [i[0]-1,i[1]+2]:
            return True
        else:
            False
    else:
        if king_pos == [i[0]-1,i[1]-2] or king_pos == [i[0]-2,i[1]-1]:
            return True
        else:
            False

def rook_pos(i, king_pos,actual_board):
    fl = 0
    for k in range(6,0,-1):
        if actual_board[k][i[1]-1] == 'k':
            fl = 1
            break
        elif actual_board[k][i[1]-1] != '#':
            fl = 0
            break
        else:
            fl = 0
    f = 0
    for k in range(i[1]-2, 0, -1):
        if actual_board[7][k] == 'k':
            f = 1
            break
        elif actual_board[7][k] != '#':
            f = 0
            break
        else:
            f = 0
    fk = 0
    for k in range(i[1]-2,8):
        if actual_board[7][k] == 'k':
            fk = 1
            break
        elif actual_board[7][k] != '#':
            fk = 0
            break
        else:
            fk = 0
    if fl == 1:
        return True
    elif f == 1:
        return True
    elif fk == 1:
        return True
    else:
        return False

def bishop_pos(i, king_pos,actual_board):
    x, y = i[0]-1, i[1]-1
    fl = 0
    while(y>0):
        if actual_board[x-1][y-1] == 'k':
            fl = 1
            break
        elif actual_board[x-1][y-1] != '#' and actual_board[x-1][y-1] != 'k':
            fl = 0
            break
        else:
            fl = 0
        x = x-1
        y = y-1
    x, y = i[0]-1, i[1]-1
    f = 0
    while(y<7):
        if actual_board[x-1][y+1] == 'k':
            f = 1
            break
        elif actual_board[x-1][y+1] != '#' and actual_board[x-1][y+1] != 'k':
            f = 0
            break
        else:
            f = 0
        x = x-1
        y = y+1
    if fl == 1:
        return True
    elif f == 1:
        return True
    else:
        return False

def inline_pos(i,king_pos,actual_board):
    inline_checks = ['Q','R']
    fl = 0
    if king_pos[0] == 7:
        if i[1] > king_pos[1]:
            for k in range(i[1]-1,9):
                if actual_board[6][k] in inline_checks:
                    fl = 1
                    break
                else:
                    fl = 0
        if i[1] < king_pos[1]:
            for k in range(i[1]-1, -1, -1):
                if actual_board[6][k] in inline_checks:
                    fl = 1
                    break
                else:
                    fl = 0
        if fl == 1:
            return True
        else:
            return False
    else:
        return False

def diogo_pos(i,arr):
    diog_check = ['Q','B']
    for j in range(len(arr)):
        if arr[j] in diog_check:
            if j+1 == i[1] - 1 or j+1 == i[1] + 1:
                return True
    return False 

def othervalue_check(arr):
    vals = ['R','Q','B','K']
    for i in arr:
        if i in vals:
            return True
    return False

def waysToGiveACheck(board):
    actual_board = []
    pos_pwn_promo = []
    king_pos = []
    check = 0
    for i in board:
        arr = [j for j in str(i)]
        actual_board.append(arr[2:-2])
    actual_board = actual_board[::-1]
    for j in range(8):
        for k in range(8):
            if actual_board[j][k] == 'P':
                if j+1 == 7:
                    if actual_board[j+1][k] == '#':
                        pos_pwn_promo.append([j+2,k+1])
            if actual_board[j][k] == 'k':
                king_pos.append([j+1,k+1])
    for i in pos_pwn_promo:
        if othervalue_check(actual_board[6]):
            if inline_pos(i,king_pos[0],actual_board):
                check += 4
        if (knight_pos(i, king_pos[0])):
            check += 1
        if rook_pos(i, king_pos[0],actual_board):
            check += 2
        if bishop_pos(i, king_pos[0],actual_board):
            check += 2
        if diogo_pos(i, actual_board[7]):
            check += 4
    if check > 4:
        return 4
    else:
        return check

if __name__ == '__main__':
    t = int(input().strip())
    result = []
    for a in range(t):
        board = []
        for board_i in range(8):
            board_t = [str(board_temp) for board_temp in input().strip().split(' ')]
            board.append(board_t)
        result.append(waysToGiveACheck(board))
    for res in result:
        print(res)