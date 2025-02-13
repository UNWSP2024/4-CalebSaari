total_rainfall = 0.0
total_months = 0.0

number_of_years = int(input("How many years? "))

#rainfall per month
for years in range(1, number_of_years +1):
    print("Year", years)

    for months in range(1, 13):
       rainfall = float(input("Rainfall per month:"))
       total_rainfall += rainfall
       total_months += 1

#average
average_rainfall = total_rainfall / total_months

#display
print("Number of months:", total_months)
print("Total inches of rain:", total_rainfall)
print("The average rainfall:", average_rainfall)

#Caleb Saari 2/13/25 Wk4 Program 3 Average Rainfall