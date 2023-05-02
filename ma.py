
def enter_list(offset):
    data = input(f"Enter numbers for row {offset + 1}, each number separated by a space: ")
    lst = data.split()
    return [int(num) for num in lst]


def display_sum_of_rows(list_of_lists):
    print("The sum of each row is:")
    for index, lst in enumerate(list_of_lists):
        print(f"Sum of {index} row: {lst} is {sum(lst)}")


def display_sum_of_columns(list_of_lists):
    max_len = len(max(list_of_lists, key=len))
    print("The sum of each column is:")
    for i in range(0, max_len):
        column = [lst[i] for lst in list_of_lists if len(lst) > i ]
        print(f"Sum of {i} column: {column} is {sum(column)}")


def main():
    list_of_lists = []
    rows = int(input("Enter the number of rows: "))
    for i in range(rows):
        list_of_lists.append(enter_list(i))
    display_sum_of_rows(list_of_lists)
    display_sum_of_columns(list_of_lists)


main()

