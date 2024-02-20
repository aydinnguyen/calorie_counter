import requests


api_key = "W/E5sJAjip63mPy3JfAYIw==xWcqbq4NayuEaMtE"
headers = {"X-Api-Key":api_key}

name = input("What is your name? ")
gender = input("Are you a male or a female?")
age = int(input("how old are you?"))
weight = int(input("how much do you wheigh in kg?"))
height = int(input("how tall are you?"))

if (gender == "female"):
  caloriesToConsume = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
else:
  caloriesToConsume = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)

meals = {
  "breakfast" : [],
  "lunch" : [],
"dinner" : [],
"snack" : [],
}

totalCalories = 0

for meal,m in meals.items():
  foodAmount = int(input(f"how much food did you eat/drink for {meal}?"))
  for i in range(foodAmount):
    food = input("Food/Drink: ")
    url = "https://api.api-ninjas.com/v1/nutrition?query="+food
    website = requests.get(url,headers=headers)
    websiteList = website.json()
    try:
      meals[meal].append(websiteList[0]['calories'])
      print(f"{food} added succesfully.")
    except:
      print(f"Error adding {food}")

  totalCalories += sum(m)


print(meals)

def mealTotalCalories():
  for k,v in meals.items():
    print(f"for {k} you ate a total of {sum(v)} calories!")

def caloriesForTheDay():
  print(f"Total calories to consume: {caloriesToConsume}")
  print(f"Your calorie total today is: {totalCalories}")
  if(totalCalories > caloriesToConsume):
    print("you have exeeded your calorie limit!")
  else:
    print(f"you have {caloriesToConsume - totalCalories} calories left to consume.")


def menu():
  print("--------------------")
  print("YOUR INFO")
  print(f"""
  NAME: {name}
  AGE: {age}  
  HEIGHT: {height}
  WEIGHT: {weight}
  GENDER: {gender}
  """)
  print("--------------------")
  caloriesForTheDay()
  print("--------------------")
  mealTotalCalories()

menu()