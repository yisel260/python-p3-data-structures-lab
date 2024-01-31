spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    
    spicy_foods_names = [food['name'] for food in spicy_foods]


    return spicy_foods_names
    

def get_spiciest_foods(spicy_foods):
    spicy_foods_spiciest = [(food) for food in spicy_foods if food['heat_level'] > 5]
    return spicy_foods_spiciest


def print_spicy_foods(spicy_foods):
    heat_level_peper = "🌶"
    for food in spicy_foods:
         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_peper * food['heat_level']}")
         #print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_peper * food['heat_level']}")

    
         #print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_peper * food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food 
    

def print_spiciest_foods(spicy_foods):
    spiciest_foods_list=get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods_list)


def get_average_heat_level(spicy_foods):

    sum_heat_level = 0
    for food in spicy_foods:
        sum_heat_level += food['heat_level']
    return sum_heat_level/ len(spicy_foods)
    
def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
    
