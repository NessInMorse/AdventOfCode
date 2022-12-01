def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def main():
        raw = openFile()
        data = [int(raw[0])]
        for i in range(1, len(raw)):
                if raw[i] != "":
                        data[-1] += int(raw[i])
                else:
                        data.append(0)
        s = sorted(data)
        print(s[-1] + s[-2] + s[-3])

main()
