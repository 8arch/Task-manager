
from typing import Callable
import shlex

from constants import (
    DAYS,
    TEXT_USER_INPUT,
    TEXT_SUCCESS_ADD,
    TEXT_SKIPPED_ADD,
    TEXT_SKIPPED_SET,
    ERROR_VALID,
    ERROR_DAY
)

from utils import valid_day, get_status

from services import (
    print_tasks, 
    add_task, 
    remove_task, 
    remove_status_all, 
    remove_status_day
)

def menu_print_task(tasks: dict[str, list], func: Callable) -> int | None:
     
        print(
            "\n"
            "1. Показать все задачи\n"
            "2. Показать задачи за день"
        )
        input_user = int(input("Выберите действие: "))
            
        if input_user == 1:
            func(tasks)
            
        elif input_user == 2:
            input_day = input("Введите день: ")
            input_day = valid_day(input_day)
            if input_day in DAYS:
                func(tasks = tasks, day = input_day)
            else:
                raise ValueError(ERROR_DAY)
        
        elif input_user == 0:
            return 0
          
        else:
            raise ValueError(ERROR_VALID)

def edit_task_menu(tasks: dict[str, list], func: Callable[[dict[str, list]], dict], status: str):
    
    if status:
        user_status, user_day, *user_task = shlex.split(input(TEXT_USER_INPUT))
        
        get_st= get_status(user_status)
        result = func(tasks = tasks, day = user_day, task_input = user_task, status = get_st)
        
    else:
        user_day, *user_task = shlex.split(input(TEXT_USER_INPUT))
        result = func(tasks = tasks, day = user_day, task_input = user_task)
    
    if result["success"]:
        print(TEXT_SUCCESS_ADD)
        for i, task in enumerate(result["success"], 1):
            print(f" {i}. {task}")
    
    if result["failed"]:
        print(TEXT_SKIPPED_ADD)
        for i, task in enumerate(result["failed"], 1):
            print(f" {i}. {task}")
    
    if result.get("skipped"):
        print(TEXT_SKIPPED_SET)
        for i, task in enumerate(result["skipped"], 1):
                print(f" {i}. {task}")
        
        
def remove_menu_status(tasks: dict[str, list]):
    
    input_user, input_status = shlex.split(input(
         "\nвведите день и статус или просто статус: "))
    
    get_st = get_status(input_status)
    if input_user.strip() == "-н":
        result = remove_status_all(tasks = tasks, status = get_st)
        print(
        f"Успешно удалено [{len(result)}] задач с статусом [{get_st}]"
        if result else f"Задачи с статусом [{get_st}] отсутствуют")
        return
    day_valid = valid_day(input_user)
    if day_valid in DAYS:
        result = remove_status_day(tasks = tasks, day = input_user, status = get_st)
        print(
            f"Успешно удалено [{len(result)}] задач с статусом [{get_st}] в день недели [{day_valid}]" 
            if result else f"нет задач с статусом [{get_st}] в день недели [{day_valid}]")
        
