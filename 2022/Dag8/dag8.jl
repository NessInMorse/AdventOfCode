function openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end


function part1()
        raw = openFile()
        count = 0
        raw = [[parse(Int32, j) for j in i] for i in raw]
        for row in eachindex(raw)
                for column in eachindex(raw[row])
                        if row == 1 || row == length(raw[1]) || column == 1 || column == length(raw)
                                count += 1
                        else
                                # print(row, column)
                                up = all([raw[r][column] for r in eachindex(raw) if r < row] .|> x -> (x < raw[row][column]))
                                left = all(raw[row][begin:column-1] .|> x -> (x < raw[row][column]))
                                right = all(raw[row][column+1:end] .|> x -> (x < raw[row][column]))
                                down = all([raw[r][column] for r in eachindex(raw) if r > row] .|> x -> (x < raw[row][column]))
                                if any((up, down, left, right))
                                        count += 1
                                end
                        end
                end
        end
        println(count)
end



function part2()
        raw = openFile()
        raw = [[parse(Int32, j) for j in i] for i in raw]
        score = 0
        scores = []
        for row in eachindex(raw)
                for column in eachindex(raw[row])
                        up = reverse([raw[r][column] for r in eachindex(raw) if r < row])
                        left = reverse(raw[row][begin:column-1])
                        right = raw[row][column+1:end]
                        down = [raw[r][column] for r in eachindex(raw) if r > row]


                        pos = 1
                        up_score, left_score, right_score, down_score = (0, 0, 0, 0)
                        while pos <= length(up) && up[pos] < raw[row][column]
                                up_score += 1
                                pos += 1
                        end

                        if pos <= length(up)
                                up_score += 1
                        end


                        pos = 1
                        while pos <= length(left) && left[pos] < raw[row][column]
                                left_score += 1
                                pos += 1
                        end


                        if pos <= length(left)
                                left_score += 1
                        end



                        pos = 1
                        while pos <= length(right) && right[pos] < raw[row][column]
                                right_score += 1
                                pos += 1
                        end

                        if pos <= length(right)
                                right_score += 1
                        end

                        pos = 1
                        while pos <= length(down) && down[pos] < raw[row][column]
                                down_score += 1
                                pos += 1
                        end
                
                        if pos <= length(down)
                                down_score += 1
                        end



                        

                        score = up_score * left_score * right_score * down_score
                        # println("score[$(row)][$(column)] : $(score) = $(up_score) * $(left_score) * $(right_score) * $(down_score)")
                        # println("-" ^ 30)
                        append!(scores, score)  
                end
        end

        println(maximum(scores))
end




part1()
println("-" ^ 9)
part2()
