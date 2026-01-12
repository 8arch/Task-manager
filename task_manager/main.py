
from menus import menu_print_task, edit_task_menu, remove_menu_status

from services import(
    add_task,
    remove_task,
    set_task_status,
    print_tasks,
    clear_tasks,
)

from constants import (TEXT_USER_CHOICE)
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
                "5. СБРОС ЕЖЕДНЕВНИКА\n" )
            
            user_num = int(input(TEXT_USER_CHOICE))
        
            if user_num == 1:
                while True:
                    try:
                        result = menu_print_task(tasks = task_list, func = print_tasks)
                        if result == 0:
                            break
                    except ValueError as e:
                        print(e)
     
            if user_num == 2:
                edit_task_menu(tasks = task_list, func = add_task, status = True)
         
            if user_num == 3:
                while True:
                    try: 
                        print(
                            "\n" 
                            "1. удалить задачи по имени\n"
                            "2. удалить задачи по статусу")
                        
                        input_user = int(input(TEXT_USER_CHOICE))
                        
                        if input_user == 1:
                            edit_task_menu(tasks = task_list, func = remove_task, status = False)
            
                        if input_user == 2: 
                            remove_menu_status(tasks = task_list)
                        
                        if input_user == 0:
                            break
                    
                    except ValueError as e:
                        print(e)
                                         
                                                        
            if user_num == 4: 
                edit_task_menu(tasks = task_list, func = set_task_status, status= True)
            
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

