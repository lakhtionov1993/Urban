team1 = 'Мастера кода'
team2 = 'Волшебники данных'


def party(team1_num, team2_num):
    print('В команде %s участников: %s !' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


def formats(score_2, team1_time):
    print('Команда {} решила задач: {} !'.format(team2, score_2))
    print('{} решили задачи за {} с !'.format(team2, team1_time))


def f_string(score_1, score_2, team1_time, team2_time):
    tasks_total = score_1 + score_2
    time_awg = (team1_time + team2_time) / tasks_total
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = f'Победа команды {team1}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = f'Победа команды {team2}!'
    else:
        challenge_result = f'Ничья!'

    print(f'Команды решили {score_1} и {score_2} задач.')
    print(challenge_result)
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_awg, 1)} секунды на задачу!')


party(5, 6)
formats(42, 18015.2)
f_string(40, 42, 1552.512, 2153.31451)
