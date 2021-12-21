data = open("input.txt").read().split("\n")

player1_pos = int(data[0][-1])
player2_pos = int(data[1][-1])

player_score = [0,0]

board = [1,2,3,4,5,6,7,8,9,10]

die = 0
rolls = 0

while True:
    move = 0
    for _ in range(3):
        rolls += 1
        die += 1
        if die == 101:
                die = 1
        move += die
    for _ in range(move):
        player1_pos += 1
        if player1_pos == 11:
            player1_pos = 1
    player_score[0] += board[player1_pos-1]
    if player_score[0] >= 1000:
        print(player_score)
        print(rolls)
        print(player_score[1] * rolls)
        break

    move = 0
    for _ in range(3):
        rolls += 1
        die += 1
        if die == 101:
            die = 1
        move += die
    for _ in range(move):
        player2_pos += 1
        if player2_pos == 11:
            player2_pos = 1
    player_score[1] += board[player2_pos-1]
    if player_score[1] >= 1000:
        print(player_score[0] * rolls)
        break