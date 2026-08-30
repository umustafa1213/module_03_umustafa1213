import sys


def print_list(string_list: list) -> int:
    curr_arg = 1
    list_len = len(string_list)
    for i in range(0, list_len):
        for word in string_list[i].split():
            print(f"Argument {curr_arg}: "
                  f"{word}")
            curr_arg += 1
    return curr_arg - 1


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print()
        return
    else:
        total_arg = print_list(sys.argv[1:])
    print(f"Total arguments: {total_arg}")
    print()


if __name__ == "__main__":
    main()
