one=open("input.txt", "r") |> x -> readlines(x) .|> x -> split(x, ",") .|> x -> split(x, "-") .|> x -> parse(Int32, x)
println(sum(one .|> x -> issubset(x[1][1]:x[1][2], x[2][1]:x[2][2]) || issubset(x[2][1]:x[2][2], x[1][1]:x[1][2])))
println(sum(one .|> x -> any([i ∈ x[2][1]:x[2][2] for i ∈ x[1][1]:x[1][2]])))
