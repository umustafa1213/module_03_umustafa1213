import random


def find_average_score(score_dict: dict) -> float:
    sum_score = 0
    for score in score_dict:
        sum_score = sum_score + score_dict[score]
    average_score = sum_score / len(score_dict)
    return round(average_score, 2)


def ft_data_alchemist() -> None:
    init_list = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
                 "john", "kevin", "Liam"]
    all_name_caps_list = [name.capitalize() for name in init_list]
    caps_only_list = [name for name in init_list if name == name.capitalize()]
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {init_list}")
    print(f"New list with all names capitalized: {all_name_caps_list}")
    print(f"New liest of capitalized names only: {caps_only_list}")
    score_dict = {name: random.randint(9, 1000) for name in all_name_caps_list}
    print(f"Score dict: {score_dict}")
    average_score = find_average_score(score_dict)
    print(f"Score average is {average_score}")
    a = int(average_score)
    high_dict = {name: random.randint(a, 1000) for name in all_name_caps_list}
    print(f"Hight score: {high_dict}")
    return


def main() -> None:
    ft_data_alchemist()


if __name__ == "__main__":
    main()
