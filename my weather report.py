import datetime
import calendar
#part1
city = input("Enter your city name: ")
temperature = float(input("Enter today's temperature: "))
#part2
if temperature > 35:
   print("It is very hot.")
#part3
if temperature > 25:
   print("Great day to go outside.")
else:
   print("Grab a jacket before you go out.")
#part4
if temperature > 35:
   print("weather:Scorching Hot ")
elif temperature > 25:
   print("weather:warm and sunny")
elif temperature > 15:
   print("weather:cool and breezy")
else:
   print("weather:cold, stay warm")
#part5
current_date = datetime.datetime.now()
current_year = calendar.calendar(current_date.year)
print("city: ",city)
print("current_date: ",current_date)
print("current_year: ",current_year)

