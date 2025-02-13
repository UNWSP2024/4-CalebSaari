total = 0.0

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