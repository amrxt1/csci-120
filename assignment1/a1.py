#815257

fruit_calorie = {
    'apple': 130,
    'avocado' : 50,
    'banana' : 110,
    'cantaloupe' : 50,
    'grapefruit' : 60,
    'grapes' : 90,
    'honeydew melon' : 50,
    'kiwifruit' : 90,
    'lemon' : 15,
    'lime' : 20,
    'nectarine' : 60,
    'orange' : 80,
    'peach' : 60,
    'pear' : 100,
    'pineapple' : 50,
    'plums' : 70,
    'strawberries' : 50,
    'sweet cherries' : 100,
    'tangerine' : 50,
    'watermelon' : 80,
}

def get_calories(fruit):
    if fruit in fruit_calorie:
        return str(fruit_calorie[fruit])

def main():
    print("This program outputs calories of a portion of the entered fruit.")
    print("Enter a FRUIT to continue.")
    print("Enter a EXIT to exit the program.")
    while True:
        fruit = input("Fruit: ").lower().strip()
        if fruit == "exit":
            break
        calories = get_calories(fruit)
        if calories:
            print("Calories: "+calories)
        else:
            print("Invalid Fruit")

main()