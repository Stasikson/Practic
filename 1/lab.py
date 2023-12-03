
def func():
    players = [19, 19, 26, 25, 20, 18, 30, 24, 27]
    all_players = 0
    step = 0

    for el in players:
        all_players += el
        step += 1

    older_player = players[0]
    for el in players:
        if el > older_player:
            older_player = el

    result = all_players / step
    print('Середній вік ' ,result)
    print('Найстарший гравець ', older_player)
    print('Різниця віку ', older_player - result)


print(func())
