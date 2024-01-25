import random
animals = ["Lion", "Elephant", "Giraffe", "Tiger", "Zebra",
           "Kangaroo", "Penguin", "Koala", "Panda", "Gorilla",
           "Cheetah", "Hippopotamus", "Rhinoceros", "Dolphin", "Kangaroo",
           "Polar Bear", "Crocodile", "Peacock", "Ostrich", "Giraffe"]
fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry",
          "Watermelon", "Mango", "Pineapple", "Cherry", "Kiwi",
          "Pear", "Peach", "Plum", "Blueberry", "Raspberry",
          "Pomegranate", "Lemon", "Avocado", "Cranberry", "Coconut"]

statutory_items= ["Pen", "Pencil", "Notebook", "Eraser", "Highlighter",
                    "Stapler", "Paper clips", "Binder", "Ruler", "Scissors",
                    "Glue stick", "Correction tape", "Calculator", "Sticky notes", "Markers",
                    "Whiteboard", "Folders", "Rubber bands", "Paper shredder", "Desk organizer"]

flowers = ["Rose", "Tulip", "Sunflower", "Lily", "Daisy",
           "Orchid", "Carnation", "Chrysanthemum", "Hyacinth", "Peony",
           "Daffodil", "Gerbera", "Iris", "Poppy", "Marigold",
           "Camellia", "Hibiscus", "Lavender", "Azalea", "Bougainvillea"]

words = animals+statutory_items+flowers+fruits
while True:
    
    random_word= random.choice(words)
    print("WOED GUESSING GAME")
    if random_word in animals:
        print("hint:->  It is an animal")
    elif random_word in fruits:
        print("hint:->  It is an fruit")
        
    elif random_word in statutory_items:
        print("hint:->  It is an statniory Item")
        
    if random_word in flowers:
        print("hint:->  It is an flower")
        
    user_guesses = ""
    chanses = 5
    while chanses>0:
        wrong_guess = 0
        for ch in random_word:
            if ch.lower() in user_guesses:
                print(ch,end =" ")
            else:
                wrong_guess+=1
                print("_",end = " ")
        if wrong_guess == 0:
            print("\nYou won, The word is ",random_word)
            again = input("Do you like to play again press Y for\"yes\" and N for \"NO\" ")
            if again.upper() =="Y":
                break
            else:
                quit()
                
        guess = input("\n Make a Guess ")
        user_guesses += guess
        
        if guess not in random_word:
            chanses-=1
            print(f"wrong... You have{chanses} more chanses")
            
            if chanses == 0:
                print(f"Game Over..., The correct word is--->  {random_word}")
                restart = input("Do you like to play again press Y for\"yes\" and N for \"NO\" ")
                if restart.upper() =="Y":
                    break
                else:
                    quit()
                
                
    