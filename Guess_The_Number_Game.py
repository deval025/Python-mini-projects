import random as rand
def guess(x):
    random_number = rand.randint(1,x)
    while True:
        num = int(input("Guess The Number :"))
        if random_number==num:
            print("Yup That's The Number!!!!!")
            break
        elif random_number<num:
            print("Sorry You Went Too High!!!!!")
        else:
            print("Sorry You Went Too Low!!!!!")
def Computer_Guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            random_number=rand.randint(low,high)
        else:
            random_number=low
        print(f"is the number {random_number}")
        feedback=input("c for Correct, l for Lower than your number and h for Higher than your number: ").lower()
        if feedback=='h':
            high = random_number-1
        elif feedback=="l":
            low = random_number+1
    print(f"game end the number was {random_number}")
