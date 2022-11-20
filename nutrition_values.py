import noms
from scraping_menu import scrape
#from calc import val

client = noms.Client("SsIueuWnAo3d0kqKGdbxlY45vRaWoyE2FW4kCcrC")
names_of_food = scrape("breakfast")
tot_cal = 0
tot_prot = 0
tot_carb = 0
tot_fat = 0
ans=[tot_prot, tot_fat, tot_carb, tot_cal]
for item in names_of_food:
    while ans[3] <= 500:
        food_dict_daily = {}
        results = client.search_query(item)
        food_dict = results.json
        try:
            res = food_dict['items'][0]
        except TypeError:
            break

        abc = res['fdcId']
        food_dict_daily[abc] = 50


        food_objs = client.get_foods(food_dict_daily)
        meal = noms.Meal(food_objs)

        r = noms.report(meal)
        val_list = []
        for i in r:
            for i['name'] in ['Protein', 'Fat', 'Carbs', 'Calories']:
                val_list.append(i['value'])
                print(val_list)
                break
        for j in range(0, 4):
            ans[j] += val_list[j]
        print(item)
        print(ans[3])
        break


"""pantry_food = client.get_foods(food_dict_daily)
recommendations = noms.generate_recommendations(meal, pantry_food, noms.nutrient_dict, 3)
for rec in recommendations:
    print(round(rec[2] * 100, 2), 'g', "of", pantry_food[rec[1]].desc)"""