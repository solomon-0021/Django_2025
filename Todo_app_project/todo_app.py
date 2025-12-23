import json



class TodoApp:
    def __init__(self, tasks):
        self.tasks = tasks
        self.load_tasks()

    def display_menu(self):
        """Show the user what they can do"""
        print("\n📝 My To-Do App")
        print("================")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Save & Exit")
        print("================")

    def add_task(self):
        """Add a new task to our list"""
        task = input("What do you need to do? ")
        if task.strip():  # Make sure they didn't just hit enter
            self.tasks.append({"task": task, "completed": False})
            print(f"✅ Added: '{task}'")
        else:
            print("Oops! You can't add an empty task.")

    def view_tasks(self):
        """Show all tasks in a nice format"""
        if not self.tasks:
            print("\n🎉 No tasks! You're all caught up!")
            return

        print(f"\n📋 You have {len(self.tasks)} task(s):")
        print("-" * 40)

        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task["completed"] else "⏳"
            task_text = task["task"]
            if task["completed"]:
                task_text = f"~~{task_text}~~"  # Strikethrough effect
            print(f"{i}. {status} {task_text}")

    def complete_task(self):
        """Mark a task as completed"""
        if not self.tasks:
            print("No tasks to complete!")
            return

        self.view_tasks()
        try:
            task_num = int(input("\nWhich task did you complete? (Enter number): "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1]["completed"] = True
                task_name = self.tasks[task_num - 1]["task"]
                print(f"🎉 Marked '{task_name}' as complete!")
            else:
                print("That task number doesn't exist.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        """Remove a task from the list"""
        if not self.tasks:
            print("No tasks to delete!")
            return

        self.view_tasks()
        try:
            task_num = int(
                input("\nWhich task do you want to delete? (Enter number): ")
            )
            if 1 <= task_num <= len(self.tasks):
                deleted_task = self.tasks.pop(task_num - 1)
                print(f"🗑️ Deleted: '{deleted_task['task']}'")
            else:
                print("That task number doesn't exist.")
        except ValueError:
            print("Please enter a valid number.")

    def save_tasks(self):
        """Save tasks to a file"""
        try:
            with open("todo.json", "a") as file:
                json.dump(self.tasks, file, indent=2)
            print("💾 Tasks saved successfully!")
        except Exception as e:
            print(f"Oops! Couldn't save tasks: {e}")

    def load_tasks(self):
        """Load tasks from file when starting the app"""
        try:
            with open("todo.json", "r") as file:
                tasks = json.load(file)
            print(f"📂 Loaded {len(tasks)} saved task(s)!")
        except FileNotFoundError:
            print("No saved tasks found. Starting fresh!")
        except Exception as e:
            print(f"Couldn't load tasks: {e}")


def main():
    """Main program loop"""
    print("Welcome to your personal To-Do App! 🚀")
    tasks = []  # Global list to hold tasks

    app = TodoApp(tasks)
    

    while True:
        app.display_menu()
        choice = input("\nWhat would you like to do? (1-5): ")

        if choice == "1":
            app.add_task()
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            app.complete_task()
        elif choice == "4":
            app.delete_task()
        elif choice == "5":
            app.save_tasks()
            print("Thanks for using the To-Do App! Goodbye! 👋")
            break
        else:
            print("Hmm, that's not a valid option. Please try again.")


if __name__ == "__main__":
    main()
