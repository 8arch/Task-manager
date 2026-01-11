
import shlex

from services import(
    add_task,
    remove_task,
    set_task_status,
    print_tasks,
    clear_tasks,
    remove_status_all,
    remove_status_day
)

from utils import valid_day

from constants import (
    DAYS,
    STATUS_DONE,
    STATUS_NOT_DONE,
    TEXT_USER_INPUT,
    TEXT_SUCCESS_ADD,
    TEXT_SKIPPED_ADD,
    TEXT_SUCCESS_REMOVE,
    TEXT_FAILED_REMOVE,
    TEXT_SUCCESS_SET,
    TEXT_FAILED_SET,
    TEXT_SKIPPED_SET,
    TEXT_USER_CHOICE,
    ERROR_VALID,
    ERROR_DAY
)

from storage import (Reading_tasks, save_tasks)



def main():
    
    while True:
        try:
            print(
                "\n"
                "1. ПОСМОТРЕТЬ ЗАДАЧИ\n"
                "2. ДОБАВИТЬ ЗАДАЧУ\n"
                "3. УДАЛИТЬ ЗАДАЧУ\n"
                "4. ОТМЕТИТЬ ЗАДАЧУ\n"
                "5. СБРОС ЕЖЕДНЕВНИКА\n"
            )
            
            user_num = int(input(TEXT_USER_CHOICE))
        
            if user_num == 1:
                while True:    
                    try: 
                        print(
                            "\n"
                            "1. Показать все задачи\n"
                            "2. Показать задачи за день"
                        )
                        input_user = int(input("Выберите действие: "))
                        
                        if input_user == 1:
                            print_tasks(task_list)
                        
                        if input_user == 2:
                            input_day = input("Введите день: ")
                            input_day = valid_day(input_day)
                            if input_day in DAYS:
                                print_tasks(tasks = task_list, day = input_day)
                            else:
                                raise ValueError(ERROR_DAY)
                        
                        elif input_user == 0:
                            break
                        
                        else:
                            print("\n", ERROR_VALID)
                            
                    except ValueError as e:
                        print(e)
    
            if user_num == 2:
                
                    user_status, user_day, *user_task = shlex.split(input(TEXT_USER_INPUT))

                    if user_status == "-":
                        user_status = STATUS_NOT_DONE
                    elif user_status == "--":
                        user_status = STATUS_DONE
                    else:
                        raise ValueError(ERROR_VALID)
                        
                    result = add_task(tasks = task_list, day = user_day, tasks_input = user_task, status = user_status)
                    
                    if result["success"]:
                        print(TEXT_SUCCESS_ADD)
                        for i, task in enumerate(result["success"], 1):
                            print(f" {i}. {task}")
                            
                    if result["skipped"]:
                        print(TEXT_SKIPPED_ADD)
                        for i, task in enumerate(result["skipped"], 1):
                            print(f" {i}. {task}")
                                   
            if user_num == 3:
                while True:
                 try:
                     
                    print(
                        "\n" 
                        "1. удалить задачи по имени\n"
                        "2. удалить задачи по статусу"
                    )
                    
                    input_user = int(input(TEXT_USER_CHOICE))
                    
                    if input_user == 1:
            
                        user_day, *user_task = shlex.split(input(TEXT_USER_INPUT))
                        
                        result = remove_task(tasks = task_list, day = user_day , tasks_input = user_task)
                        
                        if result["success"]:   
                            print(TEXT_SUCCESS_REMOVE)
                            for i, task in enumerate(result["success"], 1):
                                print(f" {i}. {task}")
                                    
                        if result["failed"]:
                            print(TEXT_FAILED_REMOVE)
                            for i, task in enumerate(result["failed"], 1):
                                print(f" {i}. {task}")
                    
                    if input_user == 2: 
                        
                        input_user, input_status = shlex.split(input(
                            "\nвведите день и статус или просто статус: "))
                        
                        if input_user.strip() == "-н":
                            if not input_status.strip() == "-" or "--":
                                raise ValueError(ERROR_VALID)
                            
                            if input_status.strip() == "-":
                                input_status = STATUS_NOT_DONE
                            else:
                                input_status = STATUS_DONE
                                        
                                result = remove_status_all(tasks = task_list, status = input_status)
                                print(
                                    f"Успешно удалено [{len(result)}] задач с статусом [{input_status}]"
                                    if result else f"Задачи с статусом [{input_status}] отсутствуют")
                        
                        elif input_user in DAYS:
                            if not input_status == "-" or "--":
                                raise ValueError(ERROR_VALID)
                            
                            if input_status.strip() == "-":
                                input_status = STATUS_NOT_DONE
                            else:
                                input_status = STATUS_DONE
                            
                            result = remove_status_day(tasks = task_list, day = input_user, status = input_status)
                            print(
                                f"Успешно удалено [{result}] задач с статусом [{input_status}] в день недели [{input_user}]" 
                                if result else f"нет задач с статусом [{input_status}] в день недели [{input_user}]")
                    
                        else:
                            raise ValueError(ERROR_VALID)
                    
                    if input_user == 0:
                        break
                 
                 except ValueError as e:
                     print(e)
                                         
                                                        
            if user_num == 4:
                    try:
                        user_status, user_day, *user_task = shlex.split(input(TEXT_USER_INPUT))
                        
                        if user_status == "-":
                            user_status = STATUS_NOT_DONE
                        elif user_status == "--":
                            user_status = STATUS_DONE
                        else:
                            raise KeyError(ERROR_VALID)
                            
                        result = set_task_status(
                            tasks = task_list,
                            day = user_day,
                            tasks_input = user_task,
                            status = user_status
                        )
                    
                    except KeyError as e:
                        print(e)
                    
                    except ValueError as e:
                        print(e)
                    
                    else:
                        if result["skipped"]:
                            print(TEXT_SKIPPED_SET)
                            for i, task in enumerate(result["skipped"], 1):
                                 print(f" {i}. {task}")
                        
                        if result["success"]:
                            print(TEXT_SUCCESS_SET)
                            for i, task in enumerate(result["success"], 1):
                                 print(f" {i}. {task}")
                            
                        if result["failed"]:
                             print(TEXT_FAILED_SET)
                             for i, task in enumerate(result["failed"], 1):
                                 print(f" {i}. {task}")
            

            if user_num == 5:
                while True:
                    input_user = input("Потвердить сброс? [да/нет] ")
                    if input_user == "да":
                        result = clear_tasks(tasks = task_list)
                        if result:
                            print(f"Сборс успешно выполнен. Удалено [{result}]  задачи")
                        else:
                            print("\n", "[", "Ни одна задача еще не добавлена", "]")
                            break
                    if input_user == "нет":
                        break
            
            if user_num == 0:
                break
            
            
        except ValueError as e:
            print("ошибка: ", e)


if __name__ == "__main__":
    
    task_list = Reading_tasks()
    main()

