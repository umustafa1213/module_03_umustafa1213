import random


class Player():
    def __init__(self, player_name: str, ach: set) -> None:
        self.player_name = player_name
        self.achievements = ach

    def display_achievements(self) -> None:
        print(f"Player {self.player_name}: {self.achievements}")

    def unique_ach(self, player_list: list) -> set:
        unique_set = self.achievements
        for player in player_list:
            if self.player_name == player.player_name:
                pass
            else:
                unique_set = unique_set.difference(player.achievements)
        return unique_set

    def missing_ach(self, ach_list: list) -> set:
        ach_set = set(ach_list)
        return ach_set.difference(self.achievements)


def gen_achievement_set(all_ach: list) -> set:
    player_set: set = set()
    for _ in range(random.randint(4, 13)):
        player_set = player_set.union({(random.choice(all_ach))})
    return player_set


def find_distinct_ach(player_list: list) -> set:
    distinct_ach: set = player_list[0].achievements
    for player in player_list:
        distinct_ach = distinct_ach.union(player.achievements)
    return distinct_ach


def find_common_ach(player_list: list) -> set:
    common_ach: set = player_list[0].achievements
    for player in player_list:
        common_ach = common_ach.intersection(player.achievements)
    return common_ach


def gen_player_achievements() -> None:
    achievements = ["Crafting Genius", "World Saviour", "Master Explorer",
                    "Collector Supreme", "Very Touchable", "Boss Slayer",
                    "Speed Runner", "Serial Killer", "Master Fisher",
                    "Master Explorer", "Sharp Mind", "Treasure Burier",
                    "Somehow Alive", "Obvious Path Finer", "Tinkerer",
                    "Sharp Tongue", "Great Kisser", "Tornado Swordsman"]
    player1 = Player("Alice", gen_achievement_set(achievements))
    player2 = Player("Bob", gen_achievement_set(achievements))
    player3 = Player("Charlie", gen_achievement_set(achievements))
    player4 = Player("Dylan", gen_achievement_set(achievements))
    print("=== Achievement Tracker System ===")
    print()
    player1.display_achievements()
    player2.display_achievements()
    player3.display_achievements()
    player4.display_achievements()
    print()
    player_list = [player1, player2, player3, player4]
    print(f"All distinct achievements: {find_distinct_ach(player_list)}")
    print()
    print(f"Common achievements: {find_common_ach(player_list)}")
    print()
    print(f"Only {player1.player_name} has: {player1.unique_ach(player_list)}")
    print(f"Only {player2.player_name} has: {player2.unique_ach(player_list)}")
    print(f"Only {player3.player_name} has: {player3.unique_ach(player_list)}")
    print(f"Only {player4.player_name} has: {player4.unique_ach(player_list)}")
    print()
    print(f"{player1.player_name} is missing: "
          f"{player1.missing_ach(achievements)}")
    print(f"{player2.player_name} is missing: "
          f"{player2.missing_ach(achievements)}")
    print(f"{player3.player_name} is missing: "
          f"{player3.missing_ach(achievements)}")
    print(f"{player4.player_name} is missing: "
          f"{player4.missing_ach(achievements)}")


def main() -> None:
    gen_player_achievements()
    return


if __name__ == "__main__":
    main()
