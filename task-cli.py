from datetime import datetime
import itertools
import json
import logging
from pathlib import Path

class Task:
    id_iter = itertools.count(start=1)

    @classmethod
    def reset_id_counter(cls, start=1):
        cls.id_iter = itertools.count(start=start)

    def __init__(self,
                 id=None,
                 description=None,                 
                 status="todo",
                 createdAt=None,
                 updatedAt=None,):
        if not id:
            self.__id = next(Task.id_iter)
        else:
            self.__id = id
        self.__description = description
        self.__status = status
        self.__createdAt = createdAt or datetime.now().strftime('%a %d %b %Y, %I:%M%p')
        self.__updatedAt = updatedAt or datetime.now().strftime('%a %d %b %Y, %I:%M%p')

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
        return self.__createdAt
    
    @property
    def updatedAt(self):
        return self.__updatedAt
    
    def update(self, new_description):
        self.__description = new_description
        self.__updatedAt = datetime.now().strftime('%a %d %b %Y, %I:%M%p')

    def set_status_in_progress(self):
        self.__status = "in-progress"
        self.__updatedAt = datetime.now().strftime('%a %d %b %Y, %I:%M%p')
    
    def set_status_done(self):
        self.__status = "done"
        self.__updatedAt = datetime.now().strftime('%a %d %b %Y, %I:%M%p')

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
    
    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, \
Status:{self.status}, Created: {self.createdAt}, \
Updated: {self.updatedAt}"
    
    def __repr__(self):
        return f"ID: {self.id}, Description: {self.description}, \
Status:{self.status}, Created: {self.createdAt}, \
Updated: {self.updatedAt}"
    

def add_task(task_list, task_description):
    new_task = Task(description=task_description)
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
        logging.error("Incorrect ID. ID must be an integer.")

def set_status_in_progress(task_list, id):
    try:
        task_list[int(id)].set_status_in_progress()
    except KeyError:
        logging.error(f"Task with ID: {id} does not exist.")
    except ValueError:
        logging.error("Incorrect ID. ID must be an integer.")

def set_status_done(task_list, id):
    try:
        task_list[int(id)].set_status_done()
    except KeyError:
        logging.error(f"Task with ID: {id} does not exist.")
    except ValueError:
        logging.error("Incorrect ID. ID must be an integer.")

def save_tasks_to_file(FILE_NAME, task_list):
    with open(FILE_NAME, "w") as fp:
        json.dump([v.to_dict() for k,v in task_list.items()],
                  fp, 
                  default=str,
                  indent=4)

def load_tasks_from_file(FILE_NAME):
    task_list = {}
    if Path(FILE_NAME).exists():
        with open(FILE_NAME, "r") as fp:
            task_data = json.load(fp)
            for task in task_data:
                task_list[task["id"]] = Task(id=task["id"],
                                             description=task["description"],
                                             status=task["status"],
                                             createdAt=task["createdAt"],
                                             updatedAt=task["updatedAt"])
    return task_list

def start_application(FILE_NAME):  
    task_list = load_tasks_from_file(FILE_NAME)
    max_id = max(task_list.keys())
    if max_id:
        Task.reset_id_counter(start=max_id + 1)
    while True:
        task_list_updated = True
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
                task_list_updated = False
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
        elif parts[0] == "exit":
            break
        if task_list_updated:
            save_tasks_to_file(FILE_NAME, task_list)

def main():
    FILE_NAME = "tasks.json"
    
    logging.basicConfig(
        format="%(levelname)s - %(message)s",
        style="%"
    )
    start_application(FILE_NAME)


main()