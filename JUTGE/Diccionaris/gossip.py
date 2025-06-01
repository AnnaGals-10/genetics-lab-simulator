import sys

PARTNER = dict()
COUPLES = set()
ALONE = set()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    action = parts[0]

    if action == "affair":
        x = parts[1]
        y = parts[2]

        # Remove previous partners if any
        for person in (x, y):
            if person in PARTNER:
                prev = PARTNER[person]
                COUPLES.discard(tuple(sorted((person, prev))))
                ALONE.add(prev)
                ALONE.add(person)
                del PARTNER[prev]
                del PARTNER[person]

        # Add new couple
        COUPLES.add(tuple(sorted((x, y))))
        PARTNER[x] = y
        PARTNER[y] = x
        ALONE.discard(x)
        ALONE.discard(y)

    elif action == "info":
        print("COUPLES:")
        for couple in sorted(COUPLES):
            print(f"{couple[0]} {couple[1]}")
        print("ALONE:")
        for loner in sorted(ALONE):
            print(loner)
        print("----------")
