from random import sample

lottery_list = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
my_ticket = [5,'B','C',1]

# For 9-14 -->
# winner = sample(lottery_list, 4)
# print(f" Any ticket matching these four number/letters is the winner: {winner}")

# For 9-15 -->

session_active = True
attempts = 0

while session_active:

    winner = sample(lottery_list, 4)
    attempts += 1
    if set(winner) == set(my_ticket):
        print("You won!")
        session_active = False
    else:
        print("Your Result:")
        print("Better luck next time!")
        print(f"Attempts: {attempts}")

