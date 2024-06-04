#any code taken from other sources in your program code with python program 
#comments.
#Include the following at the top of your program(s). 
# I declare that my work contains no examples of misconduct, such as plagiarism, or 
#collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: chathura nimesh 20211305
 
# Date: 12/13/2022
import sys

#varibles    
a = 0
b = 0
c = 0
d = 0

pass_input = 0
defer_input = 0
fail_input = 0
total = 0
#append lists
progress = []
module_trailer = []
module_retriever = []
exclude = []



    

def inputs():# using define funtion to do the progression outcome in 4 logics
    global a, b, c, d
    Q = 0
    Y = 0
    X = 0
    Z = 0


    total = pass_input + defer_input + fail_input
    if total != 120:
        print("Your total is Incorrect")
                
    elif pass_input == 120 and defer_input == 0 and fail_input == 0:
        print("\nYour progression outcome is : Progress")
        Q = (pass_input,defer_input,fail_input)
        progress.append(Q)
        a = a+1       
    elif pass_input == 100:
        print ("\nYour progression outcome is : Progress (module trailer)")
        Y = (pass_input,defer_input,fail_input)
        module_trailer.append(Y)
        b = b+1        
    elif pass_input >=0 and fail_input <= 60:
        print ("\nYour progression outcome is : Do not Progress – module retriever")
        X = (pass_input,defer_input,fail_input)
        module_retriever.append(X)
        c = c+1        
    elif fail_input >= 80:
        print ("\nYour progression outcome is : Exclude")
        Z = (pass_input,defer_input,fail_input)
        exclude.append(Z)

        d = d+1
running = True
while running:
    while running:
        try:
            pass_input = int(input("\nplease enter your credit at pass : "))
            if pass_input not in range(0,140, 20):
                print("Out of range")
            elif pass_input in range(0,140, 20):
                break
        except ValueError:
                print("Integer is requried")
                continue
            
    while running:
        try:
            defer_input = int(input("\nplease enter your credit at defer : "))
            if defer_input not in range(0,140, 20):
                print("Out of range")
            elif defer_input in range(0,140, 20):
                break
        except ValueError:
               print("Integer is requried")
               continue
                
             
    while running:
        try:
            fail_input = int(input("\nplease enter your credit at fail : "))
            if fail_input not in range(0,140, 20):
                print("Out of range")
            elif fail_input in range(0,140, 20):
                break
        except ValueError:
                print("Integer is requried")
                continue
    inputs()

    x = True
    while x:
        answer = str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:  "))
        if answer == "yes" or answer == "YES" or answer == "Y" or answer == "y":
            x = False
            continue

        if answer == "Q" or answer == "q":
            print("\n")
            print("="*15,"Histogram","="*15,"\n")
            print("Progress : ", a,"*"*a)
            print("module trailer: ",b,"*"*b)
            print("Do not Progress – module retriever : ", c,"*"*c)
            print("Exclude : ", d,"*"*d)
            print(a+b+c+d,"Outcomes in total.")
            print("\n")
            print("="*15,"List (extension)","="*15,"\n""Part 2:"'\n')
            for i in progress:
                print("progress :",*i, sep = " ")
            for i in module_trailer:
                print("module_trailer :",*i, sep = " ")
            for i in module_retriever:
                print("module_retriever :",*i, sep = " ")
            for i in exclude:
                print("exclude :",*i, sep = " ")
        
            with open('abc.txt', 'w') as f:#creating the text file extension using for loop if muliple values are to progression outcome
                print("="*15," Text File (extension)","="*15,"\n""Part 3:"'\n',file =f)
                for i in progress :
                    print("progress :",i,file =f)
                for i in module_trailer:
                    print("module_trailer :",i,file =f)
                for i in module_retriever:
                    print("module_retriever :",i,file =f)
                for i in exclude:
                    print("exclude :",i,file =f)
                sys.exit() 

        else:
            print("Q or Y are only accepted")
            continue

             
        
    
#References
#global - https://www.w3schools.com/python/python_variables_global.asp
#exe file- https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
#dictionary - https://stackoverflow.com/questions/14147369/make-a-dictionary-in-python-from-input-values        
        
            
    
    
