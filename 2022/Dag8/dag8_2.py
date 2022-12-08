def openFile():
        infile = open("input.txt", "r")
        raw = infile.read().split("\n")
        infile.close()
        return raw


def part2():
        raw = openFile()
        count = 0
        raw = [[int(j) for j in i] for i in raw]
        score = 0
        scores = []
        for row in range(len(raw)):
                for column in range(len(raw)):
                        up = [raw[r][column] for r in range(len(raw)) if r < row][::-1]
                        left = raw[row][:column][::-1]
                        right = raw[row][column+1:]
                        down = [raw[r][column] for r in range(len(raw)) if r > row]
                        # print(up)
                        # print(left)
                        # print(right)
                        # print(down)
                        pos = 0
                        up_score, left_score, right_score, down_score = (0, 0, 0, 0)
                        while pos < len(up) and up[pos] < raw[row][column]:
                                up_score += 1
                                pos += 1

                        if pos < len(up):
                                up_score += 1


                        pos = 0
                        while pos < len(left) and left[pos] < raw[row][column]:
                                left_score += 1
                                pos += 1


                        if pos < len(left):
                                left_score += 1



                        pos = 0
                        while pos < len(right) and right[pos] < raw[row][column]:
                                right_score += 1
                                pos += 1

                        if pos < len(right):
                                right_score += 1

                        pos = 0
                        while pos < len(down) and down[pos] < raw[row][column]:
                                down_score += 1
                                pos += 1
                
                        if pos < len(down):
                                down_score += 1



                        

                        score = up_score * left_score * right_score * down_score
                        # print(f"score[{row}][{column}] : {score} = {up_score} * {left_score} * {right_score} * {down_score}")
                        # print("-" * 30)
                        scores.append(score)  
        print(max(scores))

part2()
