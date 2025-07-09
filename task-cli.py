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
        return self.__createdAt
    
    @property
    def updatedAt(self):
        return self.__updatedAt
    
    def __str__(self):
        return f"{self.__id}: {self.__description} - {self.__status}"

def add_task(task_list, description):
    new_task = Task(description)
    task_list.append(new_task)
    print(f"Task added successfully (ID: {new_task.id})")

def list_tasks(task_list, status=None):
    if status:
        for task in task_list:
            if task.status == status:
                print(task)
    else:
        for task in task_list:
            print(task)

def start_application():
    task_list = []
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
        


def main():
    start_application()

main()