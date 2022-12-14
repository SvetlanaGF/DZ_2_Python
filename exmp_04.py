print('Здача 4.')
people_many = [0, 0, 0, 0, 0, 0]
count_people = len(people_many)
continuation = 1

while count_people > 0:
    while continuation == 1:
        print('Сколько человек отсчитать (от 1 до', count_people, '): ')
        m = int(input())

        for i in range(m):
            people_many[i] = people_many[i] + 1
        
        for i in range(m,count_people):
            people_many[i] = people_many[i] + 2
        
# если мало осталось игроков - как выйти
        if m >= count_people:
            continuation = 0
            count_people = 0
            break
        else:
            people_many[m] = people_many[m-1] + people_many[m]
            # print(people_many)
            del people_many [m-1]
            print(people_many)
            people_finish = m
            how_much_money_people_finish = people_many [m-1]
            print(f'Раунд окончен. Счастливчик под номером', people_finish)
            print(f'У него монет -', how_much_money_people_finish)
            continuation = int(input('Продолжаем игру(да-1/нет-0)? '))
            count_people = count_people-1
            # print(count_people)
                
    else:
        print('Игра остановлена пользователем.')
        count_people = 0
        break
        
else: print('Игроки закончились!')