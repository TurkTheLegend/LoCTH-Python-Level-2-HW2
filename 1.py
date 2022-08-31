def do_something(l):
    answer = 0
    array = [[1, 2, 3], [4.4, 5, "6"], [list("78"), 9.0, 10 / 0], [None]]
    for i in range(4):
        for j in range(l):
            answer += array[i][j]
    return answer

x = int(input())
try:
    do_something(x)
except ZeroDivisionError :
    print("Division By Zero")
except IndexError :
    print("List Index Out Of Range")
except TypeError :
    print("Unsupported Operand type(s)")