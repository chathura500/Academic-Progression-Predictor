Dict = {}#dictionary varibles
pass_input = 0#varibles which are used for the progressions 
defer_input = 0
fail_input = 0
total = 0

def inputs():# defining a function for the progression outcomes

    total = pass_input + defer_input + fail_input
    if total != 120:
        print("Your total is Incorrect select y")
    elif pass_input == 120 and defer_input == 0 and fail_input == 0:# 4 logics for the progression outcomes
        Q = (pass_input,defer_input,fail_input)
        Dict[ID]=("Progress"+str(Q))

             
    elif pass_input == 100:
        Y = (pass_input,defer_input,fail_input)
        Dict[ID]=("module trailer"+str(Y))
        

    elif pass_input <= 80 and fail_input <= 60:
        X = (pass_input,defer_input,fail_input)
        Dict[ID]=("Do not Progress – module retriever"+str(X))

    elif fail_input >= 80:
        Z = (pass_input,defer_input,fail_input)
        Dict[ID]=("Exclude"+str(Z))

running = True
while running:
    ID = str(input("Enter the student uow number: "))
    try:
        pass_input = int(input("\nplease enter your credit at pass : "))
        if pass_input not in range(0,140, 20):
            print("Out of range")

    except ValueError:
        print("Integer is requried")
        continue
    try:
        defer_input = int(input("\nplease enter your credit at defer : "))
        if defer_input not in range(0,140, 20):
            print("Out of range")

    except ValueError:
        print("Integer is requried")
        continue             
    try:
        fail_input = int(input("\nplease enter your credit at fail : "))
        if fail_input not in range(0,140, 20):
            print("Out of range")

    except ValueError:
        print("Integer is requried")
        continue

    inputs()
    question=str(input("select 'y' to continue to print the dictionary print the dictionary select 'n': "))
    if question=="Y" or question=="y":
        continue
    else:
        print(Dict)
        break
             
        
    
#global - https://www.w3schools.com/python/python_variables_global.asp
#exe file- https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
#dictionary - https://stackoverflow.com/questions/14147369/make-a-dictionary-in-python-from-input-values        
            
    
    
