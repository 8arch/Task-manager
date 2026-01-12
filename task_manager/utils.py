
from constants import (
    DAYS,
    STATUS_DONE,
    STATUS_NOT_DONE,
    ERROR_VALID,
    ERROR_DAY,
    ERROR_TASK,
    ERROR_INPUT_TASK
)


def valid_task(tasks, vers_add: bool) -> set:
    normalized = set()
    for name in tasks:
        if isinstance(name, str):
            name = name.strip()
            if name != "":
                if vers_add:
                    normalized.add(name)
                if not vers_add:
                    normalized.add(name.lower())     
    return normalized


def valid_day(day: str) -> str:
    day = day.strip()
    day = day.lower()
    return day


def checking_for_issues(tasks: dict[str, list], full_result = False) -> bool | dict:
    len_tasks = {}
    for day in tasks:
        len_tasks[day] = len(tasks[day])
    
    if full_result:
        return len_tasks
    
    if not full_result:
        return any(count > 0 for count in len_tasks.values())
    

def get_status(status: str):
        map_status = {'-': STATUS_NOT_DONE, '--': STATUS_DONE}
        get_status = map_status.get(status)
        if not get_status:
            raise ValueError(ERROR_VALID)
        return get_status
    
def error_handling_input(day: str, tasks_input: list, tasks, full: bool):
    
    day = valid_day(day)
    if day not in DAYS:
        raise ValueError (ERROR_DAY)
    elif not tasks_input:
        raise ValueError (ERROR_INPUT_TASK)
    if full:
        if not tasks[day]:
            raise ValueError (ERROR_TASK)


