tasks=[]
def addt():
    task=input("enter a task = ")
    tasks.append(task)
    print(f"Task {task} added to the list. ")
    
def deletet():
    task=input("Enter a task to delete = ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} deleted from the list. ")
        
    else:
        print(f"Task not found in a list.")
        
def cleart():
    con=input("Do you want to clear the tasks (y/n) = ")
    if con=='y':
        tasks.clear()
        print("All task has been cleared.")
    else:
        print("operation undone")    
        
def listt():
    if not tasks:
        print("There are no task currently . ")
    else:
        print("Current Tasks : ")
        for index, task in enumerate(tasks):
            print(f"Task {index} . {task}")
            
            
if __name__=="__main__":
    print("Your To Do List")
    while True:
        print("Select the option.")
        print("1. Add a  task ")
        print("2. Delete a task ")
        print("3. List tasks ")
        print("4. Clear all task")
        print("5. Quit")
    
        choice =input("Enter your choice")
    
        if(choice=="1"):
            addt()
            
        elif(choice=="2"): 
            deletet()
        elif(choice=="3"):
            listt()        
        elif(choice=="4"):
            cleart()    
        elif(choice=="5"):
            break 
        else:
            print("Invalid input.")
        