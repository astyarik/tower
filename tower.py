import random
import time
import os

raund = 1
flour = 1
level = 0
kill = 0
enemy_level = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class character:
    def __init__(self, name, health=10, attack=(1, 3), boss=False):
        self.name = name
        self.max_hp = health * 2 if boss else health
        self.health = self.max_hp
        self.attack = attack
        self.boss = boss
        self.block = False

    def atc(self):
        values = list(range(self.attack[0], self.attack[1] + 1))
        weights = [3 if v == 1 else 1 for v in values]
        return random.choices(values, weights=weights)[0]

    def damage(self, dmg):
        if self.block:
            dmg = dmg // 2
            print("Вы встали за щитом! Урон уменьшен вдвое.")
        self.health -= dmg
        if self.health < 0:
            self.health = 0

    def death(self):
        return self.health <= 0

    def heal(self):
        heal_amount = random.randint(1, 3)
        old_health = self.health
        self.health += heal_amount
        if self.health > self.max_hp:
            self.health = self.max_hp
        if self.health > old_health:
            print(f"{self.name} вылечился на {self.health - old_health} здоровья!")
        else:
            print(f"{self.name} уже на максимуме здоровья!")

    def defence(self):
        self.block = True
        print(f"{self.name} занял защитную стойку!")

    def reset_block(self):
        self.block = False

    def update(self): # Только для врагов
        global enemy_level
        enemy_level += 1
        self.max_hp += random.randint(3, 6)
        self.health = self.max_hp
        mina, maxa = self.attack
        self.attack = (mina + 2, maxa + 2)

    def upd(self): #  Тоже enemy only
        global enemy_level
        enemy_level += 1
        self.max_hp += random.randint(2, 4)
        self.health = self.max_hp
        mina, maxa = self.attack
        self.attack = (mina + 1, maxa + 1)

    def upgrade(self):
        global level, flour
        rand1 = random.randint(0, 1)
        rand2 = random.randint(1, 2)
        level += 1
        self.max_hp += 5
        self.health = self.max_hp
        mina, maxa = self.attack
        self.attack = (mina + rand1, maxa + rand2)
        print(f"Вы улучшили свои навыки! Ваши параметры:\nЗдоровье - {hero.max_hp}\nАтака выросла на 2!\nВаш уровень - {level}\nВы на {flour} этаже")

try:
    ch_time = int(input("Введите целое число.\nЭто будет задержкой (в секундах) после хода, когда показываются результаты "))
except:
    print("Введено некорректное число. Поставлено базовое значение.")
    ch_time = 2

name = input("Введите имя своего героя: ") or "Герой"
hero = character(name)
print(f"Здравствуй, {hero.name}! Твое здоровье - {hero.health}. Начинаем путешествие!")

while True:
    
    answ = int(input("Хотите начать?\n1. Да\n2. Нет\n>>> "))
    if answ == 1:
        pass
    else:
        break

    print(f"\nНа вас напал Враг на {flour} этаже!\n")

    print("\nНа вас напал враг!")

    while flour <= 5:
        if flour == 1:
            print(f"""
                            ┌─────┐
                    Босс -> │  5  │
                            ├─────┤
                            │  4  │
                            ├─────┤
             Вы на {flour} этаже! │  3  │
                            ├─────┤
                            │  2  │
                            ├─────┤
                Вы здесь -> │  1  │
                            └─────┘
            """)
        if flour == 2:
            print(f"""
                            ┌─────┐
                    Босс -> │  5  │
                            ├─────┤
                            │  4  │
                            ├─────┤
             Вы на {flour} этаже! │  3  │
                            ├─────┤
                Вы здесь -> │  2  │
                            ├─────┤
                            │  1  │
                            └─────┘
            """)
        if flour == 3:
            print(f"""
                            ┌─────┐
                    Босс -> │  5  │
                            ├─────┤
                            │  4  │
                            ├─────┤
                Вы здесь -> │  3  │
                            ├─────┤
                            │  2  │
                            ├─────┤
             Вы на {flour} этаже! │  1  │
                            └─────┘
            """)
        if flour == 4:
            print(f"""
                            ┌─────┐
                    Босс -> │  5  │
                            ├─────┤
                Вы здесь -> │  4  │
                            ├─────┤
             Вы на {flour} этаже! │  3  │
                            ├─────┤
                            │  2  │
                            ├─────┤
                            │  1  │
                            └─────┘
            """)
        if flour == 5:
            print(f"""
                            ┌─────┐
        Вы здесь -> Босс -> │  5  │
                            ├─────┤
                            │  4  │
                            ├─────┤
             Вы на {flour} этаже! │  3  │
                            ├─────┤
                            │  2  │
                            ├─────┤
                            │  1  │
                            └─────┘
            """)
        if flour == 5:
            boss_hp = 10 + enemy_level * 5
            boss_atc = (1 + enemy_level, round(3 + enemy_level * 1.5))
            enemy = character("Босс", health=boss_hp, attack=boss_atc, boss=True)
            print(f"ФИНАЛЬНЫЙ БОСС\nСтатистика {hero.name}...\nУ Босса здоровье {enemy.health}, урон {enemy.attack[0]}–{enemy.attack[1]}!")
        else: 
            enemy_hp = 10 + enemy_level * random.randint(3, 6)
            enemy_atc = (1 + enemy_level, round(3 + enemy_level * 1.5))
            enemy = character("Враг", health=enemy_hp, attack=enemy_atc)

        while not hero.death() and not enemy.death():
            hero.reset_block()
            enemy.reset_block()

            clear()

            print(f"Ваши жизни - {hero.health}/{hero.max_hp}, его - {enemy.health}/{enemy.max_hp}")

            try:
                choise = int(input("\nВыберете действие:\n1. Атака, 2. Защита, 3. Лечение\n>>> "))
            except ValueError:
                print("Введите корректное число!")
                continue

            enemy_ch = random.randint(1, 3)

            if choise == 1:
                if enemy_ch == 2:
                    if dmg == 1:
                        dmg = 0
                        print("Урон был пропущен!")
                    else:
                        print("Атака отражена!")
                        dmg = hero.atc() // 2
                else:
                    dmg = hero.atc()
                enemy.damage(dmg)
                if dmg > 0:
                    print(f"Вы нанесли {dmg} урона!")

            elif choise == 2:
                hero.defence()

            elif choise == 3:
                hero.heal()

            else:
                print("Неверный выбор, ход пропущен.")

            if not enemy.death():
                if enemy_ch == 1:
                    dmg = enemy.atc()
                    if choise == 2:
                        if dmg == 1:
                            print("Урон был пропущен!")
                            dmg = 0
                        else:
                            print("Урон был отражен!")
                            dmg = dmg // 2
                    hero.damage(dmg)
                    if dmg > 0:
                        print(f"Враг нанёс {dmg} урона!")

                elif enemy_ch == 2:
                    enemy.defence()

                elif enemy_ch == 3:
                    enemy.heal()
            
            time.sleep(ch_time)

        if hero.death():
            answer = int(input("\nВы погибли. Хотите еще раз?\n1. Да \n2. Нет\n>>> "))
            if answer == 1:
                flour = 1
                level = 0
                kill = 0
                raund += 1
                enemy_level = 0
                hero.health = 10
                continue
            else:
                exit()

        if enemy.death():
            print("\nПобеда! Враг повержен!\n") 
            kill += 1
            hero.upgrade()
            raund += 1

            if flour == 5:
                print("Вы закончили свое путешествие! Поэтому выходим...")
                break
            if flour < 5:
                ans = int(input(f"Выберете действие:\n1. Пойти на {flour + 1} этаж\n2. Продолжить зачищать {flour} этаж\n3. Выйти из башни\n>>> "))
            if ans == 1:
                flour += 1
                print(f"Вы пошли на {flour} этаж... Будьте бдительны!")
                enemy.update()
                break
            elif ans == 2:
                print(f"Вы продолжили зачищать {flour}  этаж...")
                enemy.upd()
                enemy.health = enemy.max_hp
                break
            elif ans == 3:
                print("Выход...")
                exit()

print(f"Игра окончена!\nВот результаты:\nУровень {hero.name} - {level}. Уровень подземелья -  {enemy_level}\nЖизни {hero.name} - {hero.health}, ваша атака - от {hero.attack[0]} до {hero.attack[1]}. У врагов (Помните! У Босса это умножено на 2!) жизней - {enemy.health}, а урона с {enemy.attack[0]} до {enemy.attack[1]}")
print(f"\n{kill} убийств и {raund} сыграных боев\n")
print("\n\nСпасибо за игру!")

time.sleep(2)
