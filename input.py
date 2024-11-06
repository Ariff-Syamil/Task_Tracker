import cmd

class userInput (cmd.Cmd) :
    prompt = '>> '
    intro = 'This is Task Tracker by Ariff Syamil.'

    def do_task(self, line):
        # Unique identifier for each task
        task = input("Enter your task: ")
        print("Your task is: " + task)
    
    def do_quit(self, line):
        # Exit the Task Tracker
        return True

if __name__ == '__main__':
    userInput().cmdloop()
    