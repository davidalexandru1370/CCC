import copy


def part_1():
    file = "2024/1.in"
    output = "2024/level1_1.out"
    with open(file, "r") as f:
        lines = f.readlines()
        n = int(lines[0])
        for line_index in range(1, len(lines)):
            tables = 0

            line = lines[line_index]
            words = line.split(" ")
            x = int(words[0])
            y = int(words[1])

            tables += x // 3 * y
            with open(output, "a") as f:
                f.write(str(tables) + "\n")


def part_2():
    folder = "2024/"
    output = "2024/output2/"
    for index in range(1, 2):
        with open(folder + f'input2/level2_{index}.in', 'r') as f:
            lines = f.readlines()
            n = int(lines[0])
        with open(folder + f'output2/level2_{index}.out', 'w') as file:
            file.write("")
            for line in lines[1:]:
                x = int(line.split(" ")[0])
                y = int(line.split(" ")[1])
                total = int(line.split(" ")[2])
                table_id = 1
                output = ""
                for _ in range(y):
                    for idx in range(0, x // 3):
                        output += (f"{table_id} " * 3)
                        table_id += 1
                    output = output[:-1]
                    output += "\n"
                with open(folder + f'output2/level2_{index}.out', 'a') as file:
                    file.write(output + "\n")


def part_3():
    folder = "2024/"
    output = "2024/output3/"
    for index in range(0, 6):
        with open(folder + f'input3/level3_{index}.in', 'r') as f:
            lines = f.readlines()
            n = int(lines[0])
        with open(folder + f'output3/level3_{index}.out', 'w') as file:
            file.write("")
            for line in lines[1:]:
                x = int(line.split(" ")[0])
                y = int(line.split(" ")[1])
                result = [[0 for _ in range(x + 1)] for _ in range(y)]
                table_id = 1
                output = ""
                for y1 in range(y):
                    for idx in range(0, x // 3):
                        result[y1][idx * 3] = table_id
                        result[y1][idx * 3 + 1] = table_id
                        result[y1][idx * 3 + 2] = table_id
                        table_id += 1

                top_right_corner = x - 1
                idx: int = 0
                while result[idx][top_right_corner] == 0:
                    while idx <= y - 3:
                        result[idx][top_right_corner] = table_id
                        result[idx + 1][top_right_corner] = table_id
                        result[idx + 2][top_right_corner] = table_id
                        table_id += 1
                        idx += 3
                    idx = 0
                    top_right_corner -= 1

                with open(folder + f'output3/level3_{index}.out', 'a') as file:
                    for row in result:
                        output = " ".join([str(c) for c in row])
                        file.write(output[:-1] + "\n")
                    file.write("\n")


def part_4():
    folder = "2024/"
    output = "2024/output4/"
    for index in range(0, 6):
        with open(folder + f'input4/level4_{index}.in', 'r') as f:
            lines = f.readlines()
            n = int(lines[0])
        with open(folder + f'output4/level4_{index}.out', 'w') as file:
            file.write("")
            for line in lines[1:]:
                x = int(line.split(" ")[0])
                y = int(line.split(" ")[1])
                z = int(line.split(" ")[2])
                result = [[0 for _ in range(x)] for _ in range(y)]
                candidate = [[0 for _ in range(x)] for _ in range(y)]
                table_id = 1
                output = ""

        # 1 - vertical desk
        # 2 - right desk

                def bkt(row, col, rows, cols, tables):
                    nonlocal z
                    if tables == z:
                        nonlocal result
                        result = copy.deepcopy(candidate)
                        return

                    if row >= rows or col >= cols:
                        return

                    #for 1
                    if row + 2 < rows:
                        candidate[row][col] = 1
                        bkt(row + 4, col, rows, cols, tables + 1)
                        if col + 2 < cols:
                            candidate[row][col] = 1
                            bkt(row, col + 2, rows, cols, tables + 1)
                        else:
                            bkt(row + 4, 0, rows, cols, tables + 1)


                    #for 2
                    if col + 2 < cols:
                        candidate[row][col] = 2
                        bkt(row, col + 4, rows, cols, tables + 1)
                        if row + 2 < rows:
                            candidate[row][col] = 2
                            bkt(row + 2, col, rows, cols, tables + 1)
                        else:
                            bkt(row + 2, 0, rows, cols, tables + 1)

                    candidate[row][col] = 0

                bkt(0, 0, y, x, 0)
                visited = set()
                for row in range(len(result)):
                    for col in range(len(result[0])):
                        if (row, col) not in visited:
                            if result[row][col] == 1:
                                result[row][col] = 'X'
                                result[row + 1][col] = 'X'
                                result[row + 2][col] = 'X'
                                visited.add((row + 1, col))
                                visited.add((row + 2, col))
                                table_id += 1
                            elif result[row][col] == 2:
                                result[row][col] = 'X'
                                result[row][col + 1] = 'X'
                                result[row][col + 2] = 'X'
                                visited.add((row, col + 1))
                                visited.add((row, col + 2))
                                table_id += 1
                            else:
                                result[row][col] = '.'
                            visited.add((row, col))
                with open(folder + f'output4/level4_{index}.out', 'a') as file:
                    for row in result:
                        output = "".join([str(c) for c in row])
                        file.write(output + "\n")
                    file.write("\n")





if __name__ == "__main__":
    # part_1()
    # part_2()
    # part_3()
    part_4()
