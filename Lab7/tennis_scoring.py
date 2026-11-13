def parse_score(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split("-")

    if len(parts) != 2:
        raise ValueError("Score must be in A-B format")

    try:
        a, b = int(parts[0]), int(parts[1])
    except ValueError:
        raise ValueError("Score values must be integers")

    if a < 0 or b < 0:
        raise ValueError("Scores cannot be negative")

    return a, b


def game_lead(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    points = {
        '0': 0,
        '15': 1,
        '30': 2,
        '40': 3
    }

    parts = text.split("-")

    if len(parts) != 2:
        raise ValueError("Game score must be in A-B format")

    first, second = parts

    if first not in points or second not in points:
        raise ValueError("Invalid tennis point score")

    return points[first] - points[second]


def set_spread(games_csv):
    if not isinstance(games_csv, str):
        raise ValueError("Input must be a string")

    if not games_csv.strip():
        raise ValueError("Game scores cannot be empty")

    try:
        games = [int(g.strip()) for g in games_csv.split(",")]
    except ValueError:
        raise ValueError("Game scores must be integers")

    if any(g < 0 for g in games):
        raise ValueError("Game scores cannot be negative")

    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    try:
        result = parse_score(user_input)
        print("Points A and B:", result)
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    try:
        result = game_lead(user_input)
        print("Lead in Points:", result)
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    try:
        result = set_spread(user_input)
        print("Spread:", result)
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
