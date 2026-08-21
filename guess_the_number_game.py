"""
Guess The Number Game
Features:
- Difficulty levels
- Time limit
- Score system
- Game statistics
"""

import time
import random

print("=====================================")
print("     🎮 GUESS THE NUMBER GAME 🎮")
print("=====================================")

def get_game_settings(difficulty):
    if difficulty == "easy":
        return 50, 20, 25
    elif difficulty == "medium":
        return 100, 15, 20
    else:
        return 200, 10, 15

def choose_difficulty():
    while True:
        difficulty = input("Enter a difficulty (easy / medium / hard): ").lower()

        if difficulty in ["easy", "medium", "hard"]:
            max_range, max_attempts, time_limit = get_game_settings(difficulty)
            print(f"\nYou selected {difficulty} mode")
            return max_range, max_attempts, time_limit
        else:
            print("Invalid choice. Please try again.")

def get_guess(max_range):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > max_range:
            print("Guess must be between 1 and", max_range)
            continue

        return guess

def give_hint(guess , number):
    
    distance = abs(guess - number)
            
    if distance <= 10:
        hints = ["🔥 Very close!", "Almost there!", "So close!"]
            
    elif distance <= 30:
         hints = ["Getting closer", "Not far", "Somewhere near"]
            
    else:
        hints = ["Far away", "Not even close", "Way off"]

    print(random.choice(hints))

def handle_win(count, max_attempts, max_range, start_time, best_score):
    print("\n🎉 CORRECT! You guessed it!")
    print("\n================================")
                        
    print("Attempts taken:", count)
    
    base_score = max_attempts - count + 1
                                    
    if max_range == 50:
        multiplier = 1
    elif max_range == 100:
        multiplier = 2
    else:
        multiplier = 3
    
    end_time = time.time()
    time_taken = round(end_time - start_time , 2)
    
    time_bonus = max(0 , int(30 - time_taken))
    
    score = (base_score * multiplier) + time_bonus
    
    if score > best_score:
        best_score = score
            
    print(f"🏆 Score: {score}")
    
    print(f"⏱️ Time taken: {time_taken} seconds")

    return best_score

def handle_loss(number):
    print("Out of attempts!")
    
    print("\n❌ You lost!")
    print("\n========================")
    print(f"The number was: {number}")

def show_game_intro(max_range, max_attempts, time_limit):
    print("\n================================")
    print("🎯 NEW GAME STARTED!")
    print("================================")
    print(f"Range: 1 to {max_range}")
    print(f"Attempts: {max_attempts}")
    print(f"Time limit: {time_limit} sec")

def show_stats(games_played, games_won):
    print("\n===========================")
    print("📊 GAME STATS")
    print("===========================")
    print(f"Games played   : {games_played}")
    print(f"Games won      : {games_won}")

    if games_played > 0:
        win_rate = (games_won / games_played) * 100
        print(f"Win rate: {win_rate:.2f}%")
    

def play_game(max_range , max_attempts , time_limit , best_score):
    won = False

    number = random.randint(1 , max_range)

    start_time = time.time()

    show_game_intro(max_range, max_attempts, time_limit)

    count = 0

    while count < max_attempts:

        if time.time() - start_time > time_limit:
            print("⏲️ Time's up!")
            break

        print("\n--------------------------------")
        print("Attempts left:", max_attempts - count)

        remaining_time = int(time_limit - (time.time() - start_time))
        print(f"⌛ Time left: {remaining_time} sec")

        guess = get_guess(max_range)
    
        count += 1
        
        if guess == number:
            best_score = handle_win(count, max_attempts, max_range, start_time, best_score)
            
            won = True      
            break
            
        else:
            if guess > number:
                print("📉 Try going lower...")
        
            else:
                print("📈 Try going higher...")

            give_hint(guess, number)
        
    if won:
        print("\n🎉 You won! Congratulations! 🥳")
        print("\n===========================")

    else:
        handle_loss(number)
        
    print("Best score so far:", best_score)

    return best_score, won

if __name__ == "__main__":
    max_range, max_attempts, time_limit = choose_difficulty()

    best_score = 0

    games_played = 0
    games_won = 0  

    while True:
        best_score, won = play_game(max_range , max_attempts , time_limit , best_score)

        games_played += 1

        if won:
            games_won += 1

        show_stats(games_played, games_won)

        print("\n==============================")
        print("What do you want to do next?")
        print("1️⃣  Play again")
        print("2️⃣  Change difficulty")
        print("3️⃣  Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            continue

        elif choice == "2":
            max_range, max_attempts, time_limit = choose_difficulty()

        elif choice == "3":
            print("Thanks for playing! 🎮")
            break

        else:
            print("Invalid input.")