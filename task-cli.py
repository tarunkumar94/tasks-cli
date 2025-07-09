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

    def set_status_in_progress(self):
        self.__status = "in-progress"
    
    def set_status_done(self):
        self.__status = "done"
    
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
        task_list[int(id)].update(" ".join(new_description).strip("\"\'"))
    except KeyError:
        logging.error(f"Task with ID: {id} does not exist.")
    except ValueError:
        logging.error(f"Incorrect ID. ID must be an integer.")

def delete_task(task_list, id):
    try:
        del task_list[int(id)]
    except KeyError:
        logging.error(f"Task with ID: {id} does not exist.")
    except ValueError:
        logging.error("Incorrect ID. ID must me an integer.")

def set_status_in_progress(task_list, id):
    try:
        task_list[int(id)].set_status_in_progress()
    except KeyError:
        logging.error(f"Task with ID: {id} does not exist.")
    except ValueError:
        logging.error("Incorrect ID. ID must me an integer.")

def set_status_done(task_list, id):
    try:
        task_list[int(id)].set_status_done()
    except KeyError:
        logging.error(f"Task with ID: {id} does not exist.")
    except ValueError:
        logging.error("Incorrect ID. ID must me an integer.")

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
                update_task(task_list, parts[1], parts[2:])
            except IndexError:
                logging.error("Incorrect input. Please input ID and description.")
        elif parts[0] == "delete":
            try:
                delete_task(task_list, parts[1])
            except IndexError:
                logging.error("Please input task ID.")
        elif parts[0] == "mark-in-progress":
            try:
                set_status_in_progress(task_list, parts[1])
            except IndexError:
                logging.error("Please input task ID.")
        elif parts[0] == "mark-done":
            try:
                set_status_done(task_list, parts[1])
            except IndexError:
                logging.error("Please input task ID.")


def main():
    logging.basicConfig(
        format="%(levelname)s - %(message)s",
        style="%"
    )
    start_application()

main()