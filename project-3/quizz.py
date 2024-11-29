quection=("How many bones are in the human body?:",
          "In what year did the tsunami come to Sri Lanka?:",
          "What chemical was discovered by Marie Curie?:",
          "Who celebrates Vesak?:",
          "Which animal lays the biggest egg?:")

options=(("A.206","B.118","C.117","D.119"),
         ("A.2004","B.2010","C.2002","D.2005"),
         ("A.Radium and Mercury","B.Polonium and Copper","C.Polonium and Radium","D. Sulfur and Polonium "),
         ("A.Christians","B.Buddhists","C.Hindus","D.Muslims"),
         ("A.Turtle","B.Whale","C.Eagle","D.Ostrich"))

answers=("A","A","C","B","D")

guesses=[]
score=0
quection_num=0

for q in quection:
    print("-----------------------------")
    print(q)
    for o in options[quection_num]:

        print(o);
    guess=input("Enter the answer-A,B,C,D:").upper()
    guesses.append(guess)
    if guess==answers[quection_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[quection_num]} is the correct answer.")
    quection_num+=1

print("--------------------------")
print("--------RESULT-------------")
print("----------------------------")

print("answers:",end=" ")
for a in answers:
    print(a,end=" ")

print()

print("Guesses:",end=" ")
for g in guesses:
    print(g,end=" ")
print()

score=int(score/len(quection)*100)
print(f"Your score is :{score}%")





