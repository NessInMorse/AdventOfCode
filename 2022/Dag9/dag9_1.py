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
        tailpositions = []
        head, tail = ([0, 0], [0, 0])
        firstmove = True
        for i in raw:
                command = i.split(" ")[0]
                power = int(i.split(" ")[1])

                print(f"before: [{i}]\t", head, tail)
                if command == "R":
                        for j in range(power):
                                head[0] += 1
                                if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                                        tail = overcorrect(head, tail)
                                        tailpositions.append(tail.copy())
                elif command == "L":
                        for j in range(power):
                                head[0] -= 1
                                if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                                        tail = overcorrect(head, tail)
                                        tailpositions.append(tail.copy())
                elif command == "U":
                        for j in range(power):
                                head[1] += 1
                                if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                                        tail = overcorrect(head, tail)
                                        tailpositions.append(tail.copy())
                elif command == "D":
                        for j in range(power):
                                head[1] -= 1
                                if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                                        tail = overcorrect(head, tail)
                                        tailpositions.append(tail.copy())
                print(f"after:  [{i}]\t", head, tail)
                print("-" * 30)

        print(tailpositions)
        tailpositions.append([0, 0])
        unique_tail_positions = []
        for i in tailpositions:
                if i not in unique_tail_positions:
                        unique_tail_positions.append(i.copy())
        print(unique_tail_positions)
        print(len(unique_tail_positions))
                


main()
