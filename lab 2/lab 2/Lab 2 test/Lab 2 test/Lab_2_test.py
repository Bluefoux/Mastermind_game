#Filip Hinderup
import master_mind_GUI as mmg
import random

turn_count = 0
player = True

def random_correct():
    correct = []
    for i in range (4):
        correct.append(random.randint(0 , 5))
    return correct

def compare_result(player_guess, correct): #looking through the list if the colors are in the correct and if the 
    check = [0, 0, 0, 0] #2 if the color and place are correct and 1 if color is correct, but wrong place
    for i in range(4):
        for k in range(4):
            if player_guess[i] == correct[i]:
                check[i] = 2
                break
            if player_guess[i] == correct[k] and check[k] ==0:
                check[k] =1
                break
    correct_guess_num = check.count(2)
    correct_wrong_place = check.count(1)
    return correct_guess_num, correct_wrong_place

window = mmg.create_GUI() #creates the game window
#correct = random_correct() #creates the ramdom correct color combination
correct = [0, 1, 0, 3]

while player == True and turn_count <7:
   player_guess = mmg.make_guess(turn_count, window)
   correct_guess_num, correct_wrong_place = compare_result(player_guess, correct)
   mmg.peg_feedback(turn_count, correct_guess_num, correct_wrong_place, window)
   turn_count += 1
   if player_guess == correct:
       player = False
   else:
       player = True

if turn_count == 7: #I have to type loser or winner, otherwise it makes you lose
    string = 'Loser'
else:
    string = 'Winner'
mmg.gameover_screen(turn_count, string)



