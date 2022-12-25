function openfile()
        a::IOStream = open("input.txt", "r")
        raw = readlines(a)
        close(a)
        return raw
end

function is_all_digit(s)
        options = "0123456789"
        return all([i in options for i in s])
end


function main()
        raw = openfile()
        # println(raw)
        keys = []
        computer = Dict()
        for line ∈ raw
                command = split(line, ':')
                # println(command)
                push!(keys, command[1])
                if is_all_digit(strip(command[2]))
                        computer[command[1]] = parse(Int64, strip(command[2]))
                else
                        computer[command[1]] = strip(command[2])
                end
                # println(computer)
        end

        while typeof(computer["root"]) != Int64
                for i in keys
                        if typeof(computer[i]) != Int64 && typeof(computer[i]) != Float64
                                # println(computer[i])
                                sub_commanders = split(computer[i], " ")
                                comm1 = sub_commanders[1]
                                expression = sub_commanders[2]
                                comm2 = sub_commanders[3]
                                # println("-" ^ 20)
                                # println("$comm1 $comm2")
                                # println("$(computer[comm1]) $(computer[comm2])")
                                if typeof(computer[comm1]) == Int64  && typeof(computer[comm2]) == Int64
                                        if expression == "+"
                                                computer[i] = computer[comm1] + computer[comm2]
                                        elseif expression == "-"
                                                computer[i] = computer[comm1] - computer[comm2]
                                        elseif expression == "*"
                                                computer[i] = computer[comm1] * computer[comm2]
                                        else
                                                computer[i] = Int64(round(computer[comm1] / computer[comm2]))
                                        end
                                end


                        end
                end
        end
        println("-" ^ 25)



end

main()
