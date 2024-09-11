from Body.speak import Speak
import random
from Body.Listen import MicExecution
def game_play():
    Speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = MicExecution().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                Speak("ROCK")
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")
            elif (com_choose == "paper"):
                Speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")
            else:
                Speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                Speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : Jarvis :- {Com_score}")

            elif (com_choose == "paper"):
                Speak("paper")
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")
            else:
                Speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                Speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")
            elif (com_choose == "paper"):
                Speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")
            else:
                Speak("Scissors")
                print(f"Score:- ME :- {Me_score} : Jarvis :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- You :- {Me_score} : Jarvis :- {Com_score}")

