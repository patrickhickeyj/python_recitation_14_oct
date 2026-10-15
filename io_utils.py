import datetime

# --- CODE TO COMPLETE: File Reading & Writing ---
# This group is responsible for implementing the logic to save and load
# to-do lists to and from a text file.
# The expected format for each line in the file is:
# [x or o] YYYY-MM-DD: Task name
# 'x' means completed, 'o' means incomplete.


def write_todo_list(file_path, todos):
    """
    Writes a list of to-do dictionaries to a file.
    Each dictionary has keys: 'task', 'date', 'completed'.
    """
    # Your code here: Open the file and write the data in the specified format.
    # The first line of the file should be "To Do:"
    with open(file_path, "w") as f:
        lines = ["To Do:\n"]
        for todo in todos:
            lines.append(f"{todo['completed']} {todo['date']}: {todo['task']}\n")
        lines = f.writelines(lines)
    return None


def read_todo_list(file_path):
    """
    Reads a file and returns a list of to-do dictionaries.
    Each dictionary should have keys: 'task', 'date', 'completed'.
    """
    # Your code here: Open the file, read each line, parse the data,
    # and create a list of dictionaries. Handle potential errors like bad format.
    with open(file_path, "r") as f:
        lines = f.readlines()
        output = []
        for line in lines:
            first_half_of_line, second_half_of_line = line.strip().split(":")
            if first_half_of_line == "To Do":
                completed_symbol = None
                completed = None
                date = None
                task = first_half_of_line.strip()
            else:
                completed, date = first_half_of_line.strip().split()
                task = second_half_of_line.strip()
            todo = {
                "completed": completed,
                "date": date,
                "task": task,
            }
            output.append(todo)
        return output


if __name__ == "__main__":
    test_todo_list = read_todo_list("todo_list.txt")
    assert test_todo_list[0]["task"] == "To Do"
    assert test_todo_list[1]["task"] == "Review project roadmap"
    assert test_todo_list[1]["date"] == "2025-10-05"
    assert test_todo_list[1]["completed"] == "x"
    write_todo_list("test_write_list.txt", test_todo_list[1:])
    test_todo_list = read_todo_list("test_write_list.txt")
    assert test_todo_list[0]["task"] == "To Do"
    assert test_todo_list[1]["task"] == "Review project roadmap"
    assert test_todo_list[1]["date"] == "2025-10-05"
    assert test_todo_list[1]["completed"] == "x"


# --- Provided functions for input validation ---
# These functions are already complete. You can study them for how to
# handle user input and basic error handling.
def get_integer_input(prompt, min_val=1, max_val=float("inf")):
    while True:
        try:
            choice = input(prompt).strip()
            if not choice:
                return None
            val = int(choice)
            if min_val <= val <= max_val:
                return val
            else:
                print(
                    f"Invalid input. Please enter a number between {min_val} and {max_val}."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_date_input(prompt):
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            return None
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-12-31).")
