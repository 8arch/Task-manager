

from constants import(
    DAYS,
    ERROR_DAY,
    ERROR_TASK,
    ERROR_INPUT_TASK,
    ERROR_VALID
)

from utils import (
    valid_task,
    valid_day,
    checking_for_issues
)

from storage import save_tasks

def add_task (*,
    tasks: dict[str, list[dict]],
    day: str,
    tasks_input: list[str],
    status: str
) -> dict[str: list, str: list]:
    
    day = valid_day(day)
    if day not in DAYS:
        raise ValueError (ERROR_DAY)
    elif not tasks_input:
        raise ValueError (ERROR_INPUT_TASK)
    
    normalized: set = valid_task(tasks_input, vers_add= True) 
    if not normalized:
        raise ValueError
    
    else:
        success_add = []
        skipped_tasks = []
        
        
        for task in tasks[day]:
            if task["name"] in normalized:
                skipped_tasks.append(task["name"])
                normalized.remove(task["name"])
        
        for task in normalized:
            tasks[day].append({"name": task, "status": status})
            success_add.append(task)
        
        save_tasks(tasks)
        return {
                "success": success_add,
                "skipped": skipped_tasks
            }



def remove_task (*,
    tasks: dict[str, list[dict]],
    day: str,
    tasks_input: list[str],
) -> dict[str: list, str: list]:
    
    day = valid_day(day)
    
    if day not in DAYS:
        raise ValueError(ERROR_DAY)
    elif not tasks[day]:
        raise ValueError(ERROR_TASK)          
    elif not tasks_input:
        raise ValueError(ERROR_INPUT_TASK)
    
    normalized: set = valid_task(tasks_input, vers_add= False)
    if not normalized:
            raise ValueError(ERROR_VALID)
    
    else:
        success_remov = []
        failed_remov = [] 
        
        day_tasks = tasks.get(day, [])
        new_tasks = []

        for task in day_tasks:
            if task["name"].lower() in normalized:
                success_remov.append(task["name"])
                normalized.remove(task["name"].lower())
            else:
                new_tasks.append(task)

        tasks[day] = new_tasks
        failed_remov.extend(normalized)

                    
        save_tasks(tasks)
        return {
            "success": success_remov,
            "failed": failed_remov
        }
               

def remove_status_all(*, tasks: dict[str, list[dict]], status: str) -> list:
    
    all_tasks = []
    for Day in tasks:
            
        if not tasks[Day]:
            continue
            
        days_tasks = tasks.get(Day, [])
        new_tasks = []
        
        for task in days_tasks:
            if task["status"] == status:
                all_tasks.append(task["name"])
            else:
                new_tasks.append(task)
                
        tasks[Day] = new_tasks
    
    save_tasks(tasks)
    
    return all_tasks
       
    

def clear_tasks(tasks: dict[str, list[dict]]) -> int:
    check = checking_for_issues(tasks = tasks, full_result= True)
    number_of_tasks = []
    for day, len_tasks in check.items():
        if len_tasks > 0:
            tasks[day] = []
            number_of_tasks.append(len_tasks)
    
    save_tasks(tasks)
    return sum(number_of_tasks)
    
       
def remove_status_day(*, tasks: dict[str, list[dict]], day: str, status: str) -> list:
    
    if day not in DAYS:
        raise ValueError(ERROR_DAY)
    
    day = valid_day(day)
    
    if not tasks[day]:
        raise ValueError(ERROR_TASK)
        
    day_tasks = tasks.get(day, [])
    remov_tasks = []
    new_tasks = []
        
    for task in day_tasks:
        if task["status"] == status:
            remov_tasks.append(task["name"])
        else:
            new_tasks.append(task)
    tasks[day] = new_tasks
    
    save_tasks(tasks)
    return remov_tasks

            
def set_task_status(
    *,
    tasks: dict[str, list[dict]],
    day: str,
    tasks_input: list[str],
    status: str
) -> dict[str: list, str: list, str: list]:
    
    print("set -")
    day = valid_day(day)
      
    if day not in DAYS:
        raise ValueError (ERROR_DAY)
    elif not tasks_input:
        raise ValueError (ERROR_INPUT_TASK)
    elif not tasks[day]:
        raise ValueError (ERROR_TASK)
    
    normalized: set = valid_task(tasks_input, vers_add= False)
    if not normalized:
            raise ValueError (ERROR_VALID)
    else:
        success_changed = [] 
        failed_added = [] 
        skipped_tasks = []
             
                        
        day_tasks = tasks.get(day, [])
            
        for task in day_tasks:
            
            print(1, task["name"].lower())
            
            if task["name"].lower() in normalized:
                    
                if task["status"] == status:
                        skipped_tasks.append(task["name"])
                else:
                    task["status"] = status
                    success_changed.append(task["name"])
                    normalized.remove(task["name"].lower())
                    if not normalized:
                        break
            
        if normalized:        
                failed_added.extend(normalized)
                
        save_tasks(tasks)
        return {
            "success": success_changed,
            "failed": failed_added,
            "skipped": skipped_tasks  
        }


def print_tasks(tasks: dict[str, list[dict]], day: str = None) -> None:
    
    if day in tasks:
        print("\n", day)
        if not tasks[day]:
            print(" (пусто)")
        for i, task in enumerate(tasks[day], 1):
            print(f" {i}. {task['name']} - {task['status']}")
        
        
    else:
        for day, day_tasks in tasks.items():
            print(f"\n{day}:")

            if not day_tasks:
                print("  (пусто)")
                continue

            for i, task in enumerate(day_tasks, 1):
                status = task["status"]
                print(f"  {i}. {task['name']} - [{status}]")




