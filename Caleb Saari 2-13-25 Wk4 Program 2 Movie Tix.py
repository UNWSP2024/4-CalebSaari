# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.total = 0.0

another_movie = True

while another_movie:
    movies = input("What movie would you like to see? ")
    tickets = int(input("How many tickets would you like? "))
    total += tickets

    answer = input("What to watch another movie? ")
    if answer == "yes":
        another_movie = True
    else:
        another_movie = False

print("Your total number of tickets is", total)

#Caleb Saari 2/13/25 Wk4 Program 2: Movie Tix
