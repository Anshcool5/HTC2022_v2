import noms

client = noms.Client("SsIueuWnAo3d0kqKGdbxlY45vRaWoyE2FW4kCcrC")

food_dict_daily = {}
query = "Scrambled Egg"
results = client.search_query(query)
food_dict = results.json
try:
    res = food_dict['items'][0]
except TypeError:
    ing = query.split(' ')
    for i in range(len(ing)):
        results = client.search_query(ing[i])
        food_dict = results.json
        res = food_dict['items'][0] 
        abc = res['fdcId']
        food_dict_daily[abc] = 50
        food_objs = client.get_foods(food_dict_daily)
        meal = noms.Meal(food_objs)

        r = noms.report(meal)
        for i in r:
            if i['name'] in ['Protein', 'Fat', 'Carbs', 'Calories']:
                print(i['name'], '\t', i['value'])
abc = res['fdcId']
food_dict_daily[abc] = 50


food_objs = client.get_foods(food_dict_daily)
meal = noms.Meal(food_objs)

r = noms.report(meal)
for i in r:
    if i['name'] in ['Protein', 'Fat', 'Carbs', 'Calories']:
        print(i['value'])