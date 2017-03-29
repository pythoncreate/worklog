import csv
import re
import datetime
from task import Task
from task_list import TaskList


class Worklog():
    def __init__(self):
        self.filename = "work_log.csv"
        self.tasklist = TaskList()
        self.tasklist.read_task_from_file(self.filename)

    def search_by_date(self):
        for i, d in enumerate(self.tasklist.dates()):
            enum_list = [(i+1,d) for i,d in enumerate(self.tasklist.dates())]
            print(i+1, ':', d)
        while True:
            datereq = input("Select Number To See Tasks For A Date or (m) to Return to Main Menu: ").strip()
            if datereq == 'm':
                log.start_message()
            else:
                try:
                    datereq = int(datereq)

                except ValueError:
                    print("Invalid Entry")
                    continue

                else:
                    found = False
                    for i, d in enum_list:
                        for task in self.tasklist.task_list:
                            if datereq == i and task.date == d:
                                    found = True
                                    print("Date :", task.date,
                                          " Task:", task.task,
                                          " Minutes:", task.minutes,
                                          " Notes: ", task.notes
                                          )
                    if not found:
                        print("Invalid Entry. Please try again")

    def search_by_time(self):
        for i, m in enumerate(self.tasklist.minutes()):
            min_list = [(i+1,m) for i,m in enumerate(self.tasklist.minutes())]
            print(i+1, ':', m)
        while True:
            minreq = input("Select Number To See Time For Tasks or (m) to Return to Main Menu ").strip()
            if minreq == 'm':
                log.start_message()
            else:
                try:
                    minreq = int(minreq)
                except ValueError:
                    print("Invalid Entry")
                    continue

                else:
                    found = False
                    minreq = int(minreq)
                    for i, m in min_list:
                        for task in self.tasklist.task_list:
                            if minreq == int(i) and int(task.minutes) == m:
                                    found = True
                                    print("Date :", task.date,
                                          " Task:", task.task,
                                          " Minutes:", task.minutes,
                                          " Notes: ", task.notes
                                          )
                    if not found:
                        print("Invalid Entry. Please try again")



    def exact_search(self):
        while True:
            found = False
            exreq = input("Enter Text or (m) to Return to Main Menu: ").strip()
            if exreq == 'm':
                log.start_message()
            else:
                for task in self.tasklist.task_list:
                    if re.search(r'%s' % exreq, task.task, re.IGNORECASE) \
                            or re.search(r'%s' % exreq, task.notes, re.IGNORECASE):
                        found = True
                        print("Date :", task.date,
                              " Task:", task.task,
                              " Minutes:", task.minutes,
                              " Notes: ", task.notes
                              )
                if not found:
                    print("Invalid Entry. Please try again")

    def pattern_search(self):
        while True:
            found = False
            preq = input("Enter Text or (m) to Return to Main Menu: ").strip()
            if preq == 'm':
                log.start_message()
            else:
                for task in self.tasklist.task_list:
                    if preq in task.notes or preq in task.task:
                        found = True
                        print("Date :", task.date,
                              " Task:", task.task,
                              " Minutes:", task.minutes,
                              " Notes: ", task.notes
                              )
                if not found:
                    print("Invalid Entry. Please try again")

    def add_task(self):
        task = Task()
        task.input_task()
        task.input_minutes()
        task.input_notes()
        task.date = datetime.date.today()
        self.tasklist.app_task(task)
        self.tasklist.save_task_to_file(self.filename,task)

    def lookup_task(self):
        if len(self.tasklist.task_list) == 0:
            print("Nothing to lookup. Your task log is empty.\n")
            input("Hit Enter/Return to go back and add a task.")
        else:
            while True:
                lookup = input("Lookup by Date(D), Time(T), Exact Search(E) or Pattern(P): ")
                lookup.lower()

                if lookup == 'd':
                    self.search_by_date()
                    break
                elif lookup == 't':
                    self.search_by_time()
                    break
                elif lookup == 'e':
                    self.exact_search()
                    break
                elif lookup == 'p':
                    self.pattern_search()
                    break
                else:
                    print("Sorry invalid option. Please try again")

    def start_message(self):
        while True:

            q = input("Add New Task(1) or Lookup Task(2) or Quit(3): ".strip())

            try:
                q = int(q)

            except ValueError:
                print("Sorry that's an invalid entry. Please try again.")
                continue

            else:
                if q == 1:
                    self.add_task()

                elif q == 2:
                    self.lookup_task()

                elif q == 3:
                    exit()

if __name__ == '__main__':
    log = Worklog()
    log.start_message()
