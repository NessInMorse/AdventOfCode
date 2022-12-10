def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw

def main():

        raw = openFile()
        timelines = [20, 60, 100, 140, 180, 220]
        counter = 1
        signal_strength = 1
        total = []

        for i in raw:
                if i.split(" ")[0] == "noop":
                        counter += 1
                if i.split(" ")[0] == "addx":
                        counter += 1
                        if counter in timelines:
                                print(counter * signal_strength)
                                total.append(counter * signal_strength)
                        signal_strength += int(i.split(" ")[1])
                        counter += 1
                if counter in timelines:
                        total.append(counter * signal_strength)
        print(sum(total))





main()
