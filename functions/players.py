from typing import Any


def players_repr(players: list[dict], sorting_key: str = None) -> None:
    try:
        players_sorted = sorted(players, key=lambda x: x.get(sorting_key))
    except TypeError:
        players_sorted = sorted(players, key=lambda x: x.get("name"))

    for player in players_sorted:
        print(f"{player['name']}, {player['age']}, {player['number']}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    players.append(player)
    print(
        f"\nPlayer with name {player.get('name')}, age {player.get('age')},"
        f" number {player.get('number')} successfully added."
    )
    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    players = [
        player for player in players if player.get("name").lower() != name.lower()
    ]
    print(players)
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    matched_players = []
    for player in players:
        if field in player and str(player[field]).lower() == str(value).lower():
            matched_players.append(player)
    print(matched_players)
    return matched_players


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""
    for player in players:
        if player.get("name").lower() == name.lower():
            print(player)
            return player

    print("Player not found")


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Michael", "age": 33, "number": 23},
        {"name": "Kevin", "age": 32, "number": 7},
        {"name": "Charles", "age": 30, "number": 34},
        {"name": "Shaquille", "age": 31, "number": 32},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]
    sorting_keys = ["name", "age", "number"]

    while True:
        if not (user_input := input(f"Enter your choice {options}: ")):
            break

        match user_input.lower():
            case "repr":
                if not (sorting_key := input(f"Enter sorting key {sorting_keys}: ")):
                    players_repr(players=team)
                else:
                    players_repr(players=team, sorting_key=sorting_key)

            case "add":
                name = input("Enter the player's name: ")
                age = input("Enter player's age: ")
                number = input("Enter player's number: ")

                if name and age and number:
                    player = {
                        "name": name.capitalize(),
                        "age": int(age),
                        "number": int(number),
                    }
                    team = players_add(players=team, player=player)
                else:
                    print("Invalid input. Please enter all required information.")

            case "find":
                field = input(f"Enter field you want to search {sorting_keys}: ")
                value = input("Enter value you want to find: ")

                if field and value:
                    players_find(players=team, field=field, value=value)
                else:
                    print("Invalid input. Please enter both field and value to search.")

            case "del":
                if player_name := input(
                    "Enter name of the player you want to delete: "
                ):
                    team = players_del(players=team, name=player_name)
                else:
                    print("Invalid input. Please enter player's name to delete.")

            case "get":
                if player_name := input("Enter player's name you want to get: "):
                    players_get_by_name(players=team, name=player_name)
                else:
                    print("Invalid input. Please enter player's name to get.")

            case "exit":
                exit()


if __name__ == "__main__":
    main()
