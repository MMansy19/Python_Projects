import random
def check(value,answer):
    if value == answer:
        return 0
    elif value > answer:
        return 1
    else: return -1

while(True):    
    count=0    
    value=int(random.randint(0, 10))
    while(True):
        answer=int(input(("choose a number between 0 and 10: ")))
        try:
            if answer > 10 or answer <0 :
                raise ValueError("Please enter a number between 0 and 10")
        except ValueError as err:
            print(err)
            break
        checked=check(value,answer)
        if checked==0:
            count+=1
            print(f"Congratulations plus 1 \n Your Score is {count}")
            break
        elif checked==1:
            count -= 1
            print(f"Oops, wrong answer  \n Your Score is {count} .. [Hint:answer is higher]")
        else:
            count -= 1 
            print(f"Oops, wrong answer  \n Your Score is {count} .. [Hint:answer is lower]")
    output=input(("Do you want to continue? [y|n]"))
    if output=="n": 
        break
print("Your Score is {count}")        

