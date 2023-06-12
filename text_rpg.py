class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0
    
class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"You attacked {enemy.name} for {self.attack} damage!")

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def attack_player(self, player):
        player.health -= self.attack
        print(f"{self.name} attacked you for {self.attack} damage!")


def main():
    print("Welcome to Text RPG!")

    player_name = input("Enter your character's name: ")
    player = Player(player_name, 20, 5)

    enemy = Enemy("Orc", 15, 4)

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}'s Health: {player.health}, {enemy.name}'s Health: {enemy.health}")

        action = input("What do you want to do? [Attack/Run]: ").lower()

        if action == "attack":
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_player(player)
            else:
                print(f"You defeated {enemy.name}!")
        elif action == "run":
            print(f"{player.name} ran away...")
            break
        else:
            print("Invalid action. Choose Attack or Run.")

    if not player.is_alive():
        print(f"{player.name} was defeated by the {enemy.name}.")

    print("Game Over!")


if __name__ == "__main__":
    main()