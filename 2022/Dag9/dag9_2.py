def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def overcorrect(head, tail):
        if head[0] > tail[0]:
                tail[0] += 1
        elif head[0] < tail[0]:
                tail[0] -= 1
        if head[1] > tail[1]:
                tail[1] += 1
        elif head[1] < tail[1]:
                tail[1] -= 1
        return tail

def main():
        raw = openFile()
        tailpositions = [[].copy() for i in range(9)]
        knots = [[0, 0].copy() for i in range(10)]
        for i in raw:
                command = i.split(" ")[0]
                power = int(i.split(" ")[1])

                print(f"before: [{i}]\t", knots[0], knots[1], knots[2], knots[3], knots[4], knots[5], knots[6], knots[7], knots[8], knots[9])
                if command == "R":
                        for j in range(power):
                                knots[0][0] += 1
                                for x in range(len(knots[1:])):
                                        if abs(knots[x][0] - knots[x + 1][0]) > 1 or abs(knots[x][0] - knots[x + 1][0]) > 1:
                                                knots[x + 1] = overcorrect(knots[x], knots[x + 1])
                                                tailpositions[x].append(knots[x + 1].copy())
                elif command == "L":
                        for _ in range(power):
                                knots[0][0] -= 1
                                for x in range(len(knots[1:])):
                                        if abs(knots[x][0] - knots[x + 1][0]) > 1 or abs(knots[x][0] - knots[x + 1][0]) > 1:
                                                knots[x + 1] = overcorrect(knots[x], knots[x + 1])
                                                tailpositions[x].append(knots[x + 1].copy())
                elif command == "U":
                        for j in range(power):
                                knots[0][1] += 1
                                for x in range(len(knots[1:])):
                                        if abs(knots[x][0] - knots[x + 1][0]) > 1 or abs(knots[x][1] - knots[x + 1][1]) > 1:
                                                knots[x + 1] = overcorrect(knots[x], knots[x + 1])
                                                tailpositions[x].append(knots[x + 1].copy())
                elif command == "D":
                        for j in range(power):
                                knots[0][1] -= 1
                                for x in range(len(knots[1:])):
                                        if abs(knots[x][0] - knots[x + 1][0]) > 1 or abs(knots[x][1] - knots[x + 1][1]) > 1:
                                                knots[x + 1] = overcorrect(knots[x], knots[x + 1])
                                                tailpositions[x].append(knots[x + 1].copy())
                print(f"after:  [{i}]\t", knots[0], knots[1], knots[2], knots[3], knots[4], knots[5], knots[6], knots[7], knots[8], knots[9])
                print("-" * 30)

        unique_tail_positions = []
        tailpositions[8].append([0, 0])
        for i in tailpositions[8]:
                if i not in unique_tail_positions:
                        unique_tail_positions.append(i.copy())
        print(unique_tail_positions)
        print(len(unique_tail_positions))
                


main()
