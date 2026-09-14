import sys


def dictionary_validator(cmd_args: list) -> list:
    try:
        if len(cmd_args) == 1:
            raise Exception("No items provided")
        else:
            return (cmd_args[1:])
    except Exception as e:
        print("Error -", e)
        return ["error"]


def inventory_maker(cmd_args: list) -> dict:
    inventory: dict = {}
    for arg in cmd_args:
        if ":" in arg:
            try:
                cur_arg = arg.split(":")
                if cur_arg[0] in inventory:
                    print(f"Redundant item '{cur_arg[0]}' - discarding")
                else:
                    inventory.update({cur_arg[0]: int(cur_arg[1])})
            except ValueError as e:
                print(f"Quantity error for '{cur_arg[1]}':", e,
                      f"{cur_arg[0]}")
        else:
            print(f"Error - invalid parameter '{arg}'")
    return inventory


def show_items(inventory: dict) -> None:
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(list((inventory.keys())))} items: "
          f"{sum(inventory.values())}")
    return


def show_items_ratio(inventory: dict) -> None:
    item_list = list(inventory.keys())
    for item in item_list:
        ratio = round((inventory[item] / sum(inventory.values())) * 100, 1)
        print(f"Item {item} represents {ratio}%")
    return


def show_item_stats(inventory: dict) -> None:
    item_list = list(inventory.keys())
    highest_key = item_list[0]
    highest_value = inventory[item_list[0]]
    lowest_key = item_list[0]
    lowest_value = inventory[item_list[0]]
    for item in item_list:
        if inventory[item] > highest_value:
            highest_key = item
        else:
            pass
        if inventory[item] < lowest_value:
            lowest_key = item
        else:
            pass
    print(f"Item most abundant: {highest_key} with quantity "
          f"{inventory[highest_key]}")
    print(f"Iten least abundant: {lowest_key} with quantity "
          f"{inventory[lowest_key]}")


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    unprocessed_args = dictionary_validator(sys.argv)
    if unprocessed_args == ["error"]:
        return
    inventory = inventory_maker(unprocessed_args)
    print(f"Got inventory: {inventory}")
    show_items(inventory)
    show_items_ratio(inventory)
    show_item_stats(inventory)
    to_add = {"Lara's_Heart": 1}
    try:
        item = list(to_add.keys())[0]
        value = int(list(to_add.values())[0])
        if item in inventory:
            inventory[item] = inventory[item] + value
        else:
            inventory.update({item: value})
        print(f"Updated inventory: {inventory}")
    except Exception as e:
        print(f"Error - {e}")
        print(f"Current Inventory: {inventory}")

    return


def main() -> None:
    ft_inventory_system()
    return


if __name__ == "__main__":
    main()
