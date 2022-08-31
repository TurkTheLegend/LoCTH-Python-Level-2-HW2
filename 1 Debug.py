def do_something(l):
    answer = 0
    array = [[1, 2, 3], [4.4, 5, "6"], [list("78"), 9.0, 10 / 1], [None]]
    for i in range(4):
        for j in range(l):
            answer += array[i][j]
    return answer

x = int(input())
do_something(x)