def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw

def part1():
        raw = openFile()
        count = 0
        raw = [[int(j) for j in i] for i in raw]
        for row in range(len(raw)):
                for column in range(len(raw)):
                        if row == 0 or row == len(raw[0]) - 1 or column == 0 or column == len(raw) - 1:
                               #print(raw[row][column])
                                count += 1
                        else:
                                # print(row, column)
                                up = all(list(map(lambda x : x < raw[row][column], [raw[r][column] for r in range(len(raw)) if r < row])))
                                left = all(list(map(lambda x : x < raw[row][column], raw[row][:column])))
                                right = all(list(map(lambda x : x < raw[row][column], raw[row][column+1:])))
                                down = all(list(map(lambda x : x < raw[row][column], [raw[r][column] for r in range(len(raw)) if r > row])))
                                if any([up, down, left, right]):
                                        count += 1
        print(count)

part1()
