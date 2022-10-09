# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

c = 2021
print(f"Количество оставшихся конфет {c}")
import random
player_num = random.randint(1, 2)

def player_type (player_num):
    if player_num == 2:
        name = "Bot"
    else:
        name = "Пользователь"
    return name

print (f"Первым ходит {player_type (player_num)}")

play = player_num

while c > 0:
    if play % 2 == 0:
        player_num = 2
    else:
        player_num = 1

    if player_num == 1:
        print(f"{player_type (player_num)} введите число конфет ")
        n = int(input())
        if n > 28:
            print("Количество конфет должно быть не больше 28")
        else:
            c = c - n
            print(f"Количество оставшихся конфет {c}")
            play = play + 1
    else:
        if c > 28:
            n = random.randint(1, 28)
            c = c - n
            print(f"Bot выбрал {n} конфет")
            print(f"Количество оставшихся конфет {c}")
            play = play + 1
        else: 
            n = c
            c = c - n
            print(f"Bot выбрал {n} конфет")
            print(f"Количество оставшихся конфет {c}")
            play = play + 1

print(f"{player_type (player_num)} выиграл!")