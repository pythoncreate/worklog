import csv
from task import Task

class TaskList:

    def __init__(self):
        self.task_list = []

    def app_task(self, task):
        self.task_list.append(task)

    def save_task_to_file(self,filename,task):
        with open(filename, 'a', newline="\n", encoding="utf-8") as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, delimiter=",")
            # writing the data rows
            csvwriter.writerow([task.date, task.task, task.minutes, task.notes])

    def read_task_from_file(self,filename):
        with open(filename, 'r') as csvfile:
            task_reader = csv.reader(csvfile, delimiter=',')
            for row in task_reader:
                task = Task()
                task.date = row[0]
                task.task = row[1]
                task.minutes = row[2]
                task.notes = row[3]
                self.task_list.append(task)
        return self.task_list

    def dates(self):
        dates = []
        for task in self.task_list:
            if task.date not in dates:
                dates.append(str(task.date))
        return sorted(dates)

    def minutes(self):
        minutes = []
        for task in self.task_list:
            if task.minutes not in minutes:
                minutes.append(int(task.minutes))
        return sorted(minutes)

    def text(self):
        text = []
        for task in self.task_list:
            text.append(task.task)
            text.append(task.notes)
        return sorted(text)
