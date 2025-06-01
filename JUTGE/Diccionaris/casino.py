import sys

inside = set()
profits = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    name = parts[0]
    action = parts[1]

    if action == "enters":
        if name in inside:
            print(f"{name} is already in the casino")
        else:
            inside.add(name)
            if name not in profits:
                profits[name] = 0

    elif action == "leaves":
        if name not in inside:
            print(f"{name} is not in the casino")
        else:
            print(f"{name} has won {profits[name]}")
            inside.remove(name)

    elif action == "wins":
        if name not in inside:
            print(f"{name} is not in the casino")
        else:
            amount = int(parts[2])
            profits[name] += amount

print("----------")
for name in sorted(inside):
    print(f"{name} is winning {profits[name]}")
