#function for time delay when runninng the code with python 3.9 software black window
#the delay is to ensure the result is visible for 10 second 
def delay():
  #import operation system to use is dependant functions 
  import os
  #import time to set the delay lenght after that 
  import time
  time.sleep(10)
#the function for try again code
def Try_again():
    #this is the yes list for user possible input to try again
    yes_list = ["YES", "yes", "Yes", "Y", "y"]
    #this is the no list for user possible input to not try again 
    no_list = ["No", "no", "n", "N", "q", "Q", "quite", "Quite", "QUITE"]
    #while loop to allow the user to input several data for several students
    while True:
        #the try and except is to avoid any user input error might occur
        try:
            #try_again variable is to allow user to inpuyt there answer
            try_again = input("Do you want to try again? Yes/No -or q for quit\n ")
            #if statement to run if user inputs anytime in the yes list in try again
            if try_again in yes_list:
                #function calling when user input yes
                student_credit()
            #elif statement to run if user input is not from yes list
            elif try_again in no_list:
                #the next 4 lines is to print the outcome of each category for each outcome
                #each outcome will have * each time user gets one of the outcomes
                print("Progress:    ", "*"*progress)
                print("Trailer:     ", "*"*trailer)
                print("Retriever:   ", "*"*retriever)
                print("Excluded:    ", "*"*excluded)
                #the addition is to add all the outcomes together to calculate the total number of outcomes
                outcomes=progress+trailer+retriever+excluded
                #print empty line

                print("")
                #total outcome displayed 
                print(outcomes," total outcomes you have got")
                #print empty lines
                print("")
                #print the lists with each user input for pass, defer,and fail that result to one of the outcomes
                print("progress=",progress_list)
                print("trailer=",trailer_list)
                print("retriever=",retriever_list)
                print("excluded=",excluded_list)
                #print empty lines
                print("")
                #print empty lines
                print("")
                #to appand on a dictionary that will be user to create a vertical histogram
                result_dictionary["Progress"]=progress
                result_dictionary["Trailer"]=trailer
                result_dictionary["Retriever"]=retriever
                result_dictionary["Excluded"]=excluded

                
                #the histogram has been created with the help of an friend (David Dowski) on 24/11/2021 
                #this is the vertical histogram part 
                #the space variable is to make a format string. 
                #this is to calculate the lenght of space needed for a gap between each star printed

                space = ('%%%ds' % 12) * len(result_dictionary)
                
                # Print the headers of the histogram.

                print("    progress  ",progress,"|  ","trailer   ",trailer,"|  ","retriever  ",retriever,"|","excluded  ",excluded)
                print("")
                #line number for histogram
                line = 0
                #while loop to run the code several time until condition are met
                while True:
                    #add one to line
                    line += 1
                    #current line 
                    current_line = 0
                    #list to append on the start with each gap
                    parts = []
                    #for loop to appnd to each line in parts list and add one to current line
                    for v in result_dictionary.values():
                        #if statement to find which condition are met
                        if v >= line:
                            #add one to current line value
                            current_line += 1
                            #append a star to the parts list
                            parts.append("*")
                        #else statement to run if the if statement is not met
                            
                        else:
                            #appand a gap in the parts list if at least one part of the dictioanry value is equavilite
                            #to the number of stars it has stored in the parts list 
                            parts.append('')
                    #addtional if statement that will run if there is 4 stars in the current line which end of the interior loop
                            #to add one line and start a new line
                    if not current_line:
                        break
                    #print the result of the parts appended list with the spacing calculation result extracted 
                    print( space % tuple(parts) )
                    print("")
                    print(outcomes ," total outcomes you have got")
                    #print empty line
                print("")
                #break of the loop and exit
                break
             



             #else if statement for try again    
            else:
                #display a message to user
                print("Unknown value.\n Try again")
                #run a the try again function 
                Try_again()
        
                #expect incorrect types of input and display message instead of an error code
        except ValueError:
            
            print("Invalid choice.\n Try again")
            Try_again()
        
#this are the variable with a 0 value that will be adding up from the function student credit
outcomes = 0
progress = 0
trailer = 0
retriever = 0
excluded = 0
#empty dictionary to be filled and used for histogram
result_dictionary={}

#empty list to be filled and user for txt file saving and displaying to the user their input for each outcomes
progress_list=[]
trailer_list=[]
retriever_list=[]
excluded_list=[]
#student credit function which is the main part
def student_credit():
    #globel is to convert local variables to a globel one
    #to convert all local variable which can not be user outside the fdunction into a globel variables that can be used outside the functions 
  global passed, defer, fail, outcomes, progress, trailer, retriever, excluded,total, exten
  #while loop

      #try and except error from user inputs 
  try:
            #variables which colllect data from users
        while True:
            passed = int(input("Enter the credit you passed?\n"))
            if (passed % 20) == 0 and passed <=120:
                break
            else:
                print("out of range. \nenter one of the this values (20,40,60,80,100,120)")
                student_credit()
        while True:
            defer = int(input("Enter the credit you deferred?\n"))
            if defer % 20 == 0 and defer <=120:
               break
            else:
               print("out of range. \nenter one of the this values (20,40,60,80,100,120)")   

        while True:
            fail = int(input("Enter the credit you failed in?\n"))
            if fail % 20 == 0 and fail <=120:

                break
            else:
                print("out of range. \nenter one of the this values (20,40,60,80,100,120)")
            #add the values of the user input variables 
        total = passed + defer + fail

        while True:

            #if statement to run if conditions are met
            #the follow if statements and elif  and else statement will be for verifying
            #user input and validating the data before passing them to the next part of the code.
         if total == 120:
                 
                #if conditions are met it will exit the loop
                break
            #alternative if statement to run if the first if statement not met
                

         elif total < 120:
                #dispaly message to the user if the condition are met
                print("Total incorrect as it is lower then 120. please try again and enter the total of you credit.\n "
                      "The total should be 120.")
                student_credit()
         elif total > 120:
                #dispaly message to the user if the condition are met
                print("total incorrect as it is higher then 120. please try again and enter the total of you credit.\n "
                      "The total should be 120.")
        
                #dispaly message to the user if the condition are met
                print("Now")
                student_credit()
         else:
                 #dispaly message to the user if the condition are met
                print("unknown values entered.\nTry again")
                student_credit()
  except ValueError:
           #dispaly message to the user if a wrong value type entered 
            print("you have entered incorrect values.\nPlease enter an integer based values for you credit.")
            student_credit()  
    


#the following if statement and elif statements and else statement will be to identify the stuent
            #input meets which condition and display the result of the condition that it has met
            #when a condition is met a message will be display with the outcome of the user grades
            #the pass, fail, and defer variaable that are used to get the outcome will be storedin the outcome list
            #a 1 will be added to the outcome list when its condtition is met 
  if passed == 120:
      print("Progress")
      progress=progress+ 1
      progress_list.extend([passed,defer,fail])

  elif passed == 100 and defer == 20 and fail == 0:
      print("Progress (Module Trailer)")
      trailer += 1
      trailer_list.extend([passed,defer,fail])
      
      
      

  elif passed == 100 and defer == 0 and fail == 20:
      print("Progress (Module Trailer)")
      trailer += 1
      trailer_list.extend([passed,defer,fail])
      

  elif passed == 80 and defer == 40 and fail == 0:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 80 and defer == 20 and fail == 20:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 80 and defer == 0 and fail == 40:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 60 and defer == 60 and fail == 0:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 60 and defer == 40 and fail == 20:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 60 and defer == 20 and fail == 40:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 60 and defer == 0 and fail == 60:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
     

  elif passed == 40 and defer == 80 and fail == 0:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 40 and defer == 60 and fail == 20:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 40 and defer == 40 and fail == 40:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 40 and defer == 20 and fail == 60:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 40 and defer == 0 and fail == 80:
      print("Exclude")
      excluded += 1
      excluded_list.extend([passed,defer,fail])
      

  elif passed == 20 and defer == 100 and fail == 0:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 20 and defer == 80 and fail == 20:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 20 and defer == 60 and fail == 40:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 20 and defer == 40 and fail == 60:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      

  elif passed == 20 and defer == 20 and fail == 80:
      print("Exclude")
      excluded += 1
      excluded_list.extend([passed,defer,fail])
      

  elif passed == 20 and defer == 0 and fail == 100:
      print("Exclude")
      excluded += 1
      excluded_list.extend([passed,defer,fail])
      

  elif passed == 0 and defer == 120 and fail == 0:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      
      

  elif passed == 0 and defer == 100 and fail == 20:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      
      

  elif passed == 0 and defer == 80 and fail == 40:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      
      

  elif passed == 0 and defer == 60 and fail == 60:
      print("Do Not progress (Module retriever)")
      retriever += 1
      retriever_list.extend([passed,defer,fail])
      
      

  elif passed == 0 and defer == 40 and fail == 80:
      print("Exclude")
      excluded += 1
      excluded_list.extend([passed,defer,fail])
      
      

  elif passed == 0 and defer == 20 and fail == 100:
      print("Exclude")
      excluded += 1
      excluded_list.extend([passed,defer,fail])
      
      

  elif passed == 0 and defer == 0 and fail == 120:
      print("Exclude")
      excluded += 1
      excluded_list.extend([passed,defer,fail])
      
      
  else:
      print("unknown values")
  





#function calling for the credit calculator              
student_credit()
#function calling for try again 
Try_again()


#to open a demo text file and set it to writing on it

print("")
print("="*80)
print("")
f=open('demo.txt', 'w')

f.write("progress=")
#to print the list as string in the text file 
f.write(str(progress_list))
#go the next line
f.write("\n")
f.write("trailer=")
#to print the list as string in the text file 
f.write(str(trailer_list))
#go the next line
f.write("\n")
f.write("retriever=")
#to print the list as string in the text file 
f.write(str(retriever_list))
#go the next line
f.write("\n")
f.write("excluded=")
#to print the list as string in the text file 
f.write(str(excluded_list))
#go the next line
f.write("\n")
f.close()
print("this is the content of a text file")
#open a text file to read its content
f=open("demo.txt","r")
#print the content of the text file as it has been written
lines=f.readlines()
#loop to print each line of the text file 
for line in lines:
  print(line)
  #close the text file
  f.close()
  #print empty lines
print("")
#print empty lines
print("")
#calling delay function to ensure black window version of  python program will not terminate before displaying outcomes 
delay()
