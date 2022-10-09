# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Если AI ходит первым, то выигрывает в 100% случаев

c = 2021
print(f"Количество оставшихся конфет {c}")
import random
player_num = random.randint(1, 2)

def player_type (player_num):
    if player_num == 2:
        name = "AI"
    else:
        name = "Пользователь"
    return name

print (f"Первым ходит {player_type (player_num)}")

play = player_num
count = 0
count2 = player_num

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
        if count2 == 2:
            if count == 0:
                n = 20
                c = c - n
                print(f"AI выбрал {n} конфет")
                print(f"Количество оставшихся конфет {c}")
                count = count + 1
                play = play + 1
            else:
                if c <= 28:
                    n = c
                    c = c - n
                    print(f"AI выбрал {n} конфет")
                    print(f"Количество оставшихся конфет {c}")
                    play = play + 1
                else:             
                    n = 29 - n
                    c = c - n
                    print(f"AI выбрал {n} конфет")
                    print(f"Количество оставшихся конфет {c}")
                    play = play + 1
        else:
            if n < 20 and count == 0:
                n = 20 - n
                c = c - n
                print(f"AI выбрал {n} конфет")
                print(f"Количество оставшихся конфет {c}")
                count = count + 1
                play = play + 1
            else:
                if c <= 28:
                    n = c
                    c = c - n
                    print(f"AI выбрал {n} конфет")
                    print(f"Количество оставшихся конфет {c}")
                    play = play + 1
                else:             
                    n = 29 - n
                    c = c - n
                    print(f"AI выбрал {n} конфет")
                    print(f"Количество оставшихся конфет {c}")
                    play = play + 1

print(f"{player_type (player_num)} выиграл!")