function openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end

function main()
        raw = openFile()
        a = ['A', 'B', 'C']
        b = ['X', 'Y', 'Z']

        bonus = [3, 0, 6]

        score = 0
        for inp in raw
                i = split(inp, " ")
                score += bonus[((indexin(i[1], a)[1] - indexin(i[2], b)[1] + 3) % 3) + 1] + (indexin(i[2], b))[1]
        end
        println(score)



        bonus = [0, 3, 6]

        score = 0
        for inp in raw
                i = split(inp, " ")
                second = 0
                if i[2] == "X"
                        second = ((indexin(i[1], a)[1] - 1) + 3) % 3
                elseif i[2] == "Y"
                        second = indexin(i[1], a)[1]
                elseif i[2] == "Z"
                        second = ((indexin(i[1], a)[1] + 1) + 3) % 3
                end
                if second == 0
                        second = 3
                end
                # println(second, " ", bonus[indexin(i[2], b)[1]])
                # println(second + 1, bonus[indexin(i[2], b)])
                score += bonus[indexin(i[2], b)[1]] + second
        end
        println(score)



end

main()
