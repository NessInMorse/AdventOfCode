def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw

def draw(canvas, counter, signal_strength):
        if abs((counter % 40) - signal_strength) <= 1:
                canvas[max(0, counter // 40)][min(40, counter % 40)] = "#"
        return canvas


def main():
        raw = openFile()
        counter = 0
        signal_strength = 1
        canvas = [["." for i in range(40)] for j in range(6)]
        for i in raw:
                canvas = draw(canvas, counter, signal_strength)
                print(counter, signal_strength, canvas[max(0, counter // 40)][min(40, counter % 39)])
                if i.split(" ")[0] == "noop":
                        counter += 1
                if i.split(" ")[0] == "addx":
                        counter += 1
                        canvas = draw(canvas, counter, signal_strength)
                        print(counter, signal_strength, canvas[max(0, counter // 40)][min(40, counter % 39)])
                        signal_strength += int(i.split(" ")[1])
                        counter += 1
                canvas = draw(canvas, counter, signal_strength)


        for i in canvas:
                print(''.join(i))





main()
