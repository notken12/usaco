"""
ID: kendotz1
LANG: PYTHON3
TASK: ariprog
"""

def do_solution_from_end(length, number):
    sum_set = set()
    for i in range(number + 1):
        for j in range(number + 1):
            sum_set.add(i*i + j*j)

    sum_list = list(sum_set)
    sum_list.sort()
    length_list = len(sum_set)
    sum_frozenset = frozenset(sum_set)

    result_list = []
    for i in range(length_list - 1, length - 2, -1):
        # print(i)
        list_end = sum_list[i]
        delta = 1
        max_step = list_end // (length - 1)
        list_next = sum_list[i - delta]
        now_step = list_end - list_next

        while now_step <= max_step:
            in_set = True
            for n in range(length - 2):
                list_next -= now_step
                if list_next not in sum_frozenset:
                    in_set = False
                    break
            if in_set:
                result_list.append([list_end - now_step * (length - 1), now_step])
                print(list_end - now_step * (length - 1), now_step)
            delta += 1
            list_next = sum_list[i - delta]
            now_step = list_end - list_next

    result_list.sort(key=lambda r: (r[1], r[0]))

    ret = []
    if len(result_list) == 0:
        return 'NONE\n'
    for i in range(len(result_list)):
        ret.append(str(result_list[i][0]) + ' ' + str(result_list[i][1]) + '\n')
    print(ret)
    print(len(ret))
    return ret

file_read = open("ariprog.in", 'r')
input_lines = file_read.readlines()
file_read.close()

length = int(input_lines[0].strip())
number = int(input_lines[1].strip())
result = do_solution_from_end(length, number)
file_write = open("ariprog.out", 'w')
output_lines = file_write.writelines(result)
file_write.close()