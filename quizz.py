print("""
________________________________________________________________________________
                        * WELCOME TO QUIZZ *
                        ----------------------
        instructions:if answer is correct you are awarded 1 point
                     if answer is wrong you are awarded 0 points
_______________________________________________________________________________
      """)
def fun1():
    quiz_questions={"Q1:Who developed the Python language?":["A.Zim Den","B.Guido van Rossum","C.Niene Stom","D.Wick van Rossum"] ,
                    "Q2:Which one of the following is the correct extension of the Python file??":["A. .py","B. .p","C. .python","D. .c"],
                    "Q3:Which character is used in Python to make a single line comment?":["A. #","B.//","C./","D.!"]}
    quiz_ans=("B","A","A")
    user_ans=[]
    
    for que,ans in quiz_questions.items():
        print(que)
        list=ans
        for i in list:
            print(i)
        your_option=input("enter your option:")
        your_option=your_option.upper()
        user_ans.append(your_option)
        
    i=0
    score=0
    print("_______________________________________________________________________")
    print("                       * Summary *                                        ")
    while(i<len(quiz_ans)):
         for j in quiz_ans:
            if(j==user_ans[i]):
                print("Q[{0}]:your answer is correct".format(i+1))
                score+=1
            else:
                 print("Q[{0}]:your answer is wrong correct answer is {1}".format(i+1,j))
                 print()
            i=i+1
    print("_________________________________________________________________________")
    print("your score is :",score)
    
fun1()
print("__________________________________________________________________________")
print("Do you want to participate again?:")
reattempt=input("""press A if yes
press B if No
""")
print("**************************************************************************")
reattempt=reattempt.upper()

if('A'==reattempt):
    fun1()
else:
    print("Thank you!please participate again")