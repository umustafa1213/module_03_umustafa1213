import random
import typing


def gen_event() -> typing.Generator[tuple, None, None]:
    player_names = ["Alice", "Tom", "Umar", "Grace", "Anton", "Robute Guill",
                    "Himari", "Jorge", "Skeptor", "Silla", "Lara", "Tiberos",
                    "Black Beard", "Titus", "Vis Telimus", "Aequa", "Verity",
                    "FitzChivalry", "Burrich", "Jorge", "Patience", "Chade",
                    "Lanistia", "Caeror", "Sanguinius", "Behemoth", "Conor",
                    "Indol", "Iro", "Maya", "Fives", "Echo", "Anakin", "Spade",
                    "Mario", "Peach", "Gallahad", "Aizawa", "Miguel", "Sara"]
    events = ["run", "eat", "drink", "swim", "pray", "clean", "run",
              "play catch", "dig", "shoot", "climb", "marathon", "fly",
              "govern", "biking", "martial law", "sing", "rest", "jump",
              "burn wood", "barbecue", "laught", "have sex", "diving",
              "fencing", "bake", "dance", "patrol", "guard", "spy",
              "report", "study", "drive", "research", "meditate"]
    while True:
        yield (random.choice(player_names), random.choice(events))


def consume_event(random_list: list) -> typing.Generator[tuple, None, None]:
    while len(random_list) > 0:
        index = random.randint(0, len(random_list) - 1)

        event = random_list[index]
        del random_list[index]

        yield event


def main() -> None:
    event_gen_obj = gen_event()
    random_list: list = []
    for i in range(0, 1000):
        random_event = next(event_gen_obj)
        print(f"Event {i}: Player {random_event[0]} "
              f"did action {random_event[1]}")
    for i in range(0, 10):
        random_list = random_list + [next(event_gen_obj)]
    print(f"Built list of 10 events: {random_list}")
    consuming_obj = consume_event(random_list)
    for i in range(0, len(random_list)):
        discarded_event = next(consuming_obj)
        print(f"Got event from list: {discarded_event}")
        print(f"Remains in list: {random_list}")
    return


if __name__ == "__main__":
    main()
