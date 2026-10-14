"""todoy_list.py: initialize classes"""
# import datetime

from io_utils import write_todo_list, read_todo_list


class Todo:
    """
    Represents a single To-Do item. Stores task name, date, and completion status.
    """

    status = None

    def __init__(
        self, task, date, completed=False
    ):  # what should the default value be?
        # initialize the todo class
        self.set_task(task)
        self.set_date(date)
        self.set_completed(completed)

    def get_task(self):
        """
        get the task name
        """
        return self.__task

    def get_date(self):
        """
        get the task date
        """
        return self.__date

    def is_completed(self):
        """
        get the task completion status
        """
        return bool(self.__completed)

    def set_task(self, new_task):
        self.__task = new_task

    def set_date(self, new_date):
        self.__date = new_date

    def set_completed(self, status):
        self.__completed = status

    def toggle_completion(self):
        # Flip completion status
        if self.is_completed():
            self.set_completed(False)
        else:
            self.set_completed(True)

    def to_dict(self):
        """
        Converts the Todo object to dictionary format with keys like:
        {'task': 'task name', 'date': datetime.date(2025, 1, 1), 'completed': False}
        """
        todo_item = {}
        todo_item["task"] = self.__task
        todo_item["date"] = self.__date
        todo_item["completed"] = self.__completed
        return todo_item

    def __str__(self):
        return f"(task: {self.__task}, date: {self.__date}, completed: {self.__completed})\n"


# --- CODE TO COMPLETE: TodoList Class ---
# The TodoList class manages a collection of Todo objects.
# This is the central hub for adding, removing, and updating tasks.
# It should store a list of Todo objects (private variable).


class TodoList:
    """
    Manages a collection of Todo objects for a specific list.
    """

    def __init__(self, name, items):
        # TODO: Your code here
        self.set_name(name)
        self.set_items(items)

    def get_name(self):
        # TODO: Your code here: Return the list's name
        return self.__name

    def get_items(self):
        # TODO: Your code here: Return the list of Todo items
        return self.__items

    def set_name(self, new_name):
        # TODO: Your code here: Update the list's name
        self.__name = new_name

    def set_items(self, new_items):
        # TODO: Your code here: Update the list of Todo items
        self.__items = new_items

    def add_task(self, task_name, date):
        # TODO: Your code here: Create a new Todo object and add it to the list of items.
        new_task = Todo(task_name, date)
        hold_list = self.get_items()[:]
        hold_list.append(new_task)
        self.set_items(hold_list)

    def remove_task(self, index):
        """Removes a task by its 0-based index."""
        # TODO Your code here: Safely remove the item at the specified index.
        hold_list = self.get_items()[:]
        if index < len(hold_list):
            del hold_list[index]
        self.set_items(hold_list)

    REPLACE_THIS = None

    def mark_complete(
        self, index, status=True
    ):  # what might the default status be for mark complete?
        """Sets the completion status of a task by its 0-based index."""
        # TODO Your code here: Use the index to find the correct Todo object and update its status.
        hold_list = self.get_items()
        if index < len(hold_list):
            hold_list[index].set_completed(status)

    def save_to_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        write_todo_list(file_path, self.get_items())

    def load_from_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        return read_todo_list(file_path)

    def __str__(self):
        """
        Returns a formatted string representing the list.
        """
        temp_items = self.get_items()[:]
        s1 = "----------\n"
        s2 = ""
        for item in temp_items:
            s2 += item.__str__()
        return s1 + s2


t1 = Todo("Task 1", "Date 1")
t2 = Todo("Task 2", "Date 2")
item_holder = [t1, t2]
list_1 = TodoList("List 1", item_holder)
list_1.mark_complete(0)

print(t1)
print(list_1)
