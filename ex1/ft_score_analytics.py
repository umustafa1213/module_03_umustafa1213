import sys


def list_processor(score_list: list) -> list:
    processed_list: list = []
    for i in range(0, len(score_list)):
        try:
            processed_list = processed_list + [int(score_list[i])]
        except ValueError:
            print(f"Invalid paramter: '{score_list[i]}'")
        i += 1
    return processed_list


def show_analytics(processed_list: list) -> None:
    print(f"Scores processed: {processed_list}")
    print(f"Total players: {len(processed_list)}")
    print(f"Average score: {sum(processed_list)/len(processed_list):.1f}")
    print(f"High score: {max(processed_list)}")
    print(f"Low score: {min(processed_list)}")
    print(f"Score range: {max(processed_list) - min(processed_list)}")


def ft_score_analytics(score_list: list) -> None:
    print("=== Player Score Analytics ===")
    if len(score_list) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics"
              ".py <score1> <score2> ...")
        return
    else:
        processed_list = list_processor(score_list[1:])
    if len(processed_list) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics"
              ".py <score1> <score2> ...")
        return
    show_analytics(processed_list)
    return


def main() -> None:
    ft_score_analytics(sys.argv)
    return


if __name__ == "__main__":
    main()
