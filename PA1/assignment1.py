def print_winner(winning_player):
    print(f"Winner: {winning_player}")

def print_table(numbers_list, table_size):
    max_num_length = len(str(table_size ** 2 - 1))
    if table_size <= 3: #If the table size is less than 3, that means there is no alignment problem.
        for i in range(0, len(numbers_list), table_size):
            row = numbers_list[i:i + table_size]
            formatted_row = [str(num).rjust(max_num_length) for num in row]
            row_sec = "  ".join(formatted_row)
            print("  " + row_sec)
    else: #If the table size is bigger than 3, that means the alignment editing is needed.
        for i in range(0, len(numbers_list), table_size):
            row = numbers_list[i:i + table_size]
            formatted_row = [str(num).rjust(max_num_length) for num in row]
            row_sec = "  ".join(formatted_row)
            print(" " + row_sec)


def win(board, size, user):
    limit_numbers = size ** 2

    # Vertical control
    for i in range(size):
        inner_list = []
        for j in range(i, limit_numbers - size + i + 1, size):
            inner_list.append(board[j])
        if inner_list.count("X") == size:
            return True, "X"
        if inner_list.count("O") == size:
            return True, "O"

    # Horizontal control
    for i in range(size):
        sec_list = board[i * size: (i + 1) * size]
        if sec_list.count("X") == size:
            return True, "X"
        if sec_list.count("O") == size:
            return True, "O"

    # Cross control
    third_list = []
    fourth_list = []
    fifth_list = []

    for r in range(0, size, size - 1):
        if r == 0:
            for c in range(r, size ** 2 - r, size + 1):
                third_list.append(board[c])
                if third_list.count("X") == size:
                    return True, "X"
                if third_list.count("O") == size:
                    return True, "O"
        elif r == 2:
            for b in range(r, size ** 2 - r, size - 1):
                fourth_list.append(board[b])
                if fourth_list.count("X") == size:
                    return True, "X"
                if fourth_list.count("O") == size:
                    return True, "O"
        elif r == 3:
            for b in range(r, size ** 2 - r, size - 1):
                fourth_list.append(board[b])
                if fourth_list.count("X") == size:
                    return True, "X"
                if fourth_list.count("O") == size:
                    return True, "O"
        elif r == 4:
            for w in range(r, size ** 2 - r, size - 1):
                fifth_list.append(board[w])
                if fifth_list.count("X") == size:
                    return True, "X"
                if fifth_list.count("O") == size:
                    return True, "O"
    return False, None

def main(user_type="X"):
    table_size = int(input("What Size Game GoPy?"))
    limit_numbers = table_size ** 2
    numbers_list = []
    splited_list = []
    max_num_length = len(str(table_size ** 2 - 1))

    for i in range(limit_numbers):
        numbers_list.append(str(i))

    if table_size <= 3:
        for i in range(0, len(numbers_list), table_size):
            row = numbers_list[i:i + table_size]
            formatted_row = [str(num).rjust(max_num_length) for num in row]
            row_sec = "  ".join(formatted_row)
            print("  " + row_sec)
    else:
        for i in range(0, len(numbers_list), table_size):
            row = numbers_list[i:i + table_size]
            formatted_row = [str(num).rjust(max_num_length) for num in row]
            row_sec = "  ".join(formatted_row)
            print(" " + row_sec)

    user_move = "1"
    while True:
        move_input = input(f"Player {user_move} turn--> ")
        list_one = ["X", "O"]

        if move_input in numbers_list and int(move_input) < limit_numbers:
            move_input = int(move_input)
            if numbers_list[move_input] not in list_one:
                numbers_list[move_input] = "X" if user_move == "1" else "O"
                print_table(numbers_list, table_size)
                if len(splited_list) > table_size:
                        del splited_list[0:table_size]
                winner, winning_player = win(numbers_list, table_size, list_one)
                if winner:
                    print_winner(winning_player)
                    break
                user_move = "1" if user_move == "2" else "2"
            else:
                print("Please a valid number")
                print_table(numbers_list, table_size)
                user_move = "1" if user_move == "2" else "2"
        else:
            print("Please enter a valid number")
            print_table(numbers_list, table_size)
            user_move = "1" if user_move == "2" else "2"

if __name__ == "__main__":
    main()
