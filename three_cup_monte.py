from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

list1 = [" ","o"," "]
shuffle_result = shuffle_list((list1))
# print(shuffle_result)

def player_guess():
    guess = ''
    while guess not in [0,1,2]:
       try:
           guess = int(input("Pick 0 , 1 or 2 : "))
           if guess not in [0,1,2]:
               print("Please enter 0, 1 or 2 only")
       except Exception:
           print("Invalid Input")

    return guess

guess_result = player_guess()
# print(guess_result)

def check_guess(shuffle_result,guess_result):
    if shuffle_result[guess_result]=="o":
        print("Correct Guess")
       # print(shuffle_result)
    else:
        print("Wrong Guess")
        print(shuffle_result)

check_guess(shuffle_result,guess_result)