students={
    "Ansh":"70",
    "Rahul":"77",
    "Yash":"75"
}
print("menu:")
print("1:Search a student ")
print("2:Add a student ")
print("3.Update student record")
choice=input("choose an option=")

if choice=="1":
    name=input("Enter a name to search = ")
    if name in students:
        print(f"{name}: {students[name]}")
    else:
        print("Name not found")  
elif choice=="2":
    name=input("Enter a name = ")
    marks=input("Enter the marks = ")
    students[name]=marks
    print(f"Student {name} added.")   
    
elif choice=="3":  
    name=input("enter student's name to update = ")
    if name in students:
        marks=input("Enter the marks = ")
        students[name]=marks
        print("marks updated")
    else:
        print("name not found")
        
else:
    print("Please choose the valid option")                     