function openFile()
        infile = open("input.txt", "r")
        raw = readlines(infile)
        close(infile)
        return raw
end

function findRegexMatch(regex::Regex, string::String)
        return eachmatch(regex, string) |> collect
end



function part1()
        raw = openFile()
        cargo = []
        for i in raw
                number_count = length(findRegexMatch(r"[0-9]", i))
                char_and_number_count = length(findRegexMatch(r"[A-Za-z0-9]", i))
                if number_count == char_and_number_count && number_count > 0
                        cargo = ["" for i ∈ 1:parse(Int32, (split(i, " ")[end-1]))]
                end
        end
        # cargo = ["NZ", "DCM", "P"]
        start = false
        for i in raw
                if start
                        move = split(i, " ")
                        cargo[parse(Int32, move[6])] = reverse(cargo[parse(Int32, move[4])][1:parse(Int32, move[2])]) * cargo[parse(Int32, move[6])]
                        cargo[parse(Int32, move[4])] = cargo[parse(Int32, move[4])][parse(Int32, move[2]) + 1:end]
                else
                        if i != "" && length(findRegexMatch(r"[0-9]", i)) == 0
                                i = replace(i, '[' => "  ")
                                i = replace(i, ']' => " ")
                                i = rstrip(i)

                                line = split(i, " ")
                                volgorde = reverse(line)

                                for i ∈ range(1, length(volgorde), step=4)
                                        cargo[8 - (i ÷ 4) + 1] *= volgorde[i]
                                end
                        end
                end
                if i == ""
                        start = true
                end
        end
        for i in cargo
                print(i[1])
        end
        println()
end

function part2()
        raw = openFile()
        cargo = []
        for i in raw
                number_count = length(findRegexMatch(r"[0-9]", i))
                char_and_number_count = length(findRegexMatch(r"[A-Za-z0-9]", i))
                if number_count == char_and_number_count && number_count > 0
                        cargo = ["" for i ∈ 1:parse(Int32, (split(i, " ")[end-1]))]
                end
        end
        # cargo = ["NZ", "DCM", "P"]
        start = false
        for i in raw
                if start
                        move = split(i, " ")
                        cargo[parse(Int32, move[6])] = cargo[parse(Int32, move[4])][1:parse(Int32, move[2])] * cargo[parse(Int32, move[6])]
                        cargo[parse(Int32, move[4])] = cargo[parse(Int32, move[4])][parse(Int32, move[2]) + 1:end]
                else
                        if i != "" && length(findRegexMatch(r"[0-9]", i)) == 0
                                i = replace(i, '[' => "  ")
                                i = replace(i, ']' => " ")
                                i = rstrip(i)

                                line = split(i, " ")
                                volgorde = reverse(line)

                                for i ∈ range(1, length(volgorde), step=4)
                                        cargo[8 - (i ÷ 4) + 1] *= volgorde[i]
                                end
                        end
                end
                if i == ""
                        start = true
                end
        end
        for i in cargo
                print(i[1])
        end
        println()
end




part1()
part2()
# main()
