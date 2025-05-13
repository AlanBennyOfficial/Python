class ToDo:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.tasks = []

    def mark_completed(self):
        self.completed = True

    def display(self):
        return f"{self.title}: {self.description} - {'Completed' if self.completed else 'Not Completed'}"
        
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found in the list.")

    def display_tasks(self):