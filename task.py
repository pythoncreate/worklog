import datetime

class Task:

    def _init__(self):
        self.date = datetime.date.today()
        self.notes = None
        self.task = None
        self.minutes = None

    def input_task(self):
        while True:
            t = (input("Please enter a task: ")).strip().lower()
            if t == "":
                print("That wasn't a valid name. Try again.")
            else:
                self.task = t
                return self.task

    def input_minutes(self):
        while True:
            tm = (input("How Much Time Spent on This Task (in Minutes?) ")).strip().lower()
            try:
                tm = int(tm)
                self.minutes = tm
                return self.minutes
            except ValueError:
                print("That wasn't a valid time. Try again.")

    def input_notes(self):
        while True:
            nts = (input("Please enter any additional notes about this task: ")).strip().lower()
            if nts == "":
                print("That wasn't a valid name. Try again.")
            else:
                self.notes = nts
                return self.notes
