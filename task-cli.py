from datetime import datetime
import itertools
import logging

class Task:
    id_iter = itertools.count(start=1)

    def __init__(self, description):
        self.__id = next(Task.id_iter)
        self.__description = description
        self.__status = "todo"
        self.__createdAt = datetime.now()
        self.__updatedAt = self.__createdAt

    @property
    def id(self):
        return self.__id
    
    @property
    def description(self):
        return self.__description
    
    @property
    def status(self):
        return self.__status
    
    @property
    def createdAt(self):
        return self.__createdAt.strftime('%a %d %b %Y, %I:%M%p')
    
    @property
    def updatedAt(self):
        return self.__updatedAt.strftime('%a %d %b %Y, %I:%M%p')
    
    def update(self, new_description):
        self.__description = new_description
        self.__updatedAt = datetime.now()
    
    def __str__(self):
        return f"{self.__id}: {self.__description} - {self.__status}"

def add_task(task_list, description):
    new_task = Task(description)
    task_list[new_task.id] = new_task
    print(f"Task added successfully (ID: {new_task.id})")

def list_tasks(task_list, status=None):
    if status:
        for task in task_list.values():
            if task.status == status:
                print(task)
    else:
        for task in task_list.values():
            print(task)

def update_task(task_list, id, new_description):
    try:
        task_list[int(id)].update(new_description)
    except KeyError:
        logging.error(f"Task with id: {id} does not exist.")
    except ValueError:
        logging.error(f"Incorrect index. Index must be an integer.")

def start_application():
    task_list = {}
    while True:
        command = input("task-cli ")
        parts = command.split()        
        if parts[0] == "add":
            try:
                add_task(task_list, parts[1])
            except IndexError :
                logging.error("No description")
        elif parts[0] == "list":
            try:
                list_tasks(task_list, parts[1])
            except IndexError:
                list_tasks(task_list)
        elif parts[0] == "update":
            try:
                update_task(task_list, parts[1], parts[2])
            except IndexError:
                logging.error("Incorrect input. Please input ID and description.")


def main():
    logging.basicConfig(
        format="%(levelname)s - %(message)s",
        style="%"
    )
    start_application()

main()