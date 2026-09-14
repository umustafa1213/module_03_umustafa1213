import math


def list_validator(processed_list: list) -> bool:
    for word in processed_list:
        try:
            float(word)
        except ValueError:
            print(f"Error on parameter '{word.strip()}': "
                  f"could not convert string to "
                  f"float: '{word.strip()}'")
            return False
    return True


def make_tuple(processed_list) -> tuple:
    coordinates = ((float(processed_list[0]),
                    float(processed_list[1]),
                    float(processed_list[2])))
    return coordinates


def distance_two_set(first_p: tuple, second_p: tuple) -> float:
    x_square = (second_p[0] - first_p[0]) * (second_p[0] - first_p[0])
    y_square = (second_p[1] - first_p[1]) * (second_p[1] - first_p[1])
    z_square = (second_p[2] - first_p[2]) * (second_p[2] - first_p[2])
    return math.sqrt(x_square + y_square + z_square)


def check_len(processed_list: list) -> bool:
    try:
        if (len(processed_list) != 3):
            raise Exception("Invalid syntax")
        else:
            return True
    except Exception as e:
        print(e)
        return False


def get_player_pos() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    processed_list = input("Enter new coordinates as "
                           "floats in format 'x,y,z': ").split(",")
    while not check_len(processed_list) or not list_validator(processed_list):
        processed_list = input("Enter new coordinates as "
                               "floats in format 'x,y,z': ").split(",")
    first_coord = make_tuple(processed_list)
    print(f"Got a first tuple: {first_coord}")
    print(f"It includes: X={first_coord[0]:.1f}, Y={first_coord[1]:.1f},"
          f" Z={first_coord[2]:.1f}")
    print(f"Distance to center: "
          f"{distance_two_set((0, 0, 0), first_coord):.4f}")
    print()
    print("Get a second set of coordinates")
    processed_list = input("Enter new coordinates as "
                           "floats in format 'x,y,z': ").split(",")
    while not check_len(processed_list) or not list_validator(processed_list):
        processed_list = input("Enter new coordinates as "
                               "floats in format 'x,y,z': ").split(",")
    second_coord = make_tuple(processed_list)
    print("Distance between the 2 sets of coordinates: "
          f"{distance_two_set(first_coord, second_coord):.4f}")


def main() -> None:
    get_player_pos()
    return


if __name__ == "__main__":
    main()
