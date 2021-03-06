import urllib2
import os
import json
from bs4 import BeautifulSoup

htmlstr = '<html><head><!-- Latest compiled and minified CSS --><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"><!-- Optional theme --><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css"><script src="http://code.jquery.com/jquery-1.11.3.min.js"></script><!-- Latest compiled and minified JavaScript --><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script><style>.highlight{background-color:#337AB7;}.directLeft{text-align:left}.directions{width:50%;margin-left:25%;}.linkPrefersSupportingMembership{display:none;}.ingredients{text-align:left;width:50%;margin-left:25%;}ol{padding-left:20px}</style></head><body style="text-align:center"><h1>Recipes</h1>'

produce = []
frozen = []
meat = []
refrigerated = []
middle = []
unknown = []
ignored = []

produce_list = [
    "tomato",
    "cucumber",
    "lettuce",
    "carrot",
    "broccoli",
    "mushroom",
    "chive",
    "cilantro",
    "onion",
    "corn",
    "bell pepper",
    "avacado",
    "potato",
    "shallot",
    "celery",
    "avocado",
    "fresh thyme",
    "fresh ginger",
    "tofu",
    "zucchini",
    "parsley",
    "lemon",
    "asparagus",
    "spinach",
    "squash",
    "kale"
]

produce_exception_list = [
    "celery seed",
    "peeled and diced tomatoes with juice",
    "cornmeal",
    "tomato juice",
    "frozen spinach",
    "frozen chopped spinach",
    "dried parsley"
]

frozen_list = [
    "pie crust",
    "frozen"
]

frozen_exception_list = [

]

meat_list = [
    "beef",
    "bacon",
    "chicken",
    "pork",
    "turkey",
    "steak"
]

meat_exception_list = [
    "cream of chicken"
]

refrigerated_list = [
    "half and half",
    "buttermilk",
    "milk",
    "cheese",
    "sour cream",
    "egg",
    "half-and-half",
    "margarine",
    "refrigerated pizza crust"
]

refrigerated_exception_list = [
    "mac and cheese"
]

middle_list = [
    "cornmeal",
    "toothpaste",
    "rice",
    "vinegar",
    "oil",
    "soup",
    "au jus",
    "can",
    "bean",
    "juice",
    "peeled and diced tomatoes with juice",
    "celery seed",
    "onion soup mix",
    "honey",
    "mustard",
    "curry powder",
    "spice",
    "bread crumb",
    "thyme",
    "soy sauce",
    "coconut",
    "orzo",
    "jam",
    "vanilla extract",
    "nori",
    "mirin",
    "dashi",
    "miso",
    "dressing mix",
    "skewer",
    "barbeque sauce",
    "bread",
    "capers",
    "sauce mix",
    "pesto",
    "pasta",
    "macaroni",
    "ketchup",
    "cocoa",
    "buns",
    "artichoke hearts",
    "gravy",
    "mayonnaise",
    "roll",
    "root beer",
    "barbecue sauce",
    "taco seasoning",
    "enchilada sauce",
    "green chiles",
    "cinnamon",
    "dried rosemary",
    "biscuit dough",
    "tuna",
    "mayo",
    "bleach",
    "chips",
    "mac and cheese",
    "salad dressing",
    "anchovy",
    "trash bags",
    "toothbrush"
]

middle_exception_list = [

]

ignore_list = [
    "salt",
    "pepper",
    "cumin",
    "broth",
    "chili powder",
    "garlic",
    "butter",
    "sugar",
    "baking soda",
    "flour",
    "water",
    "stock",
    "olive oil",
    "lemon juice",
    "lime juie",
    "dried basil",
    "dried oregano",
    "cinamon",
    "sage",
    "cooking spray",
    "nutmeg",
    "Worcestershire",
    "dried parsley",
    "vegetable oil",
    "dried thyme",
    "white vinegar",
    "paprika",
    "italian herb seasoning"
]

ignore_exceptions_list = [
    "bell pepper",
    "buttermilk",
    "flour tortillas",
    "butternut",
    
]

def categorize(ingredient, quantity, meal):
    found = False

    for item in produce_list:
        if item in ingredient and not any(item_to_ignore in ingredient for item_to_ignore in produce_exception_list):
            produce.append([quantity, ingredient, "Produce", meal, item])
            found = True
    if not found:
        for item in meat_list:
            if item in ingredient and not any(item_to_ignore in ingredient for item_to_ignore in meat_exception_list):
                meat.append([quantity, ingredient, "Meat", meal, item])
                found = True
    if not found:
        for item in frozen_list:
            if item in ingredient and not any(item_to_ignore in ingredient for item_to_ignore in  frozen_exception_list):
                frozen.append([quantity, ingredient, "Frozen", meal, item])
                found = True
    if not found:
        for item in refrigerated_list:
            if item in ingredient and not any(item_to_ignore in ingredient for item_to_ignore in refrigerated_exception_list):
                refrigerated.append([quantity, ingredient, "Refrigerated", meal, item])
                found = True
    if not found:
        for item in middle_list:
            if item in ingredient and not any(item_to_ignore in ingredient for item_to_ignore in middle_exception_list):
                middle.append([quantity, ingredient, "Middle", meal, item])
                found = True
    if found is not True:
        unknown.append([quantity, ingredient, "Unknown", meal, "Unknown"])

def filter_check(ingredient, quantity, meal):
    if not any(item in ingredient for item in ignore_list) and not any(item in ingredient for item in ignore_exceptions_list):
        categorize(ingredient, quantity, meal)
    elif any(item in ingredient for item in ignore_exceptions_list):
        categorize(ingredient, quantity, meal)
    else:
        if not any(ignored_item == ingredient for ignored_item in ignored):
            ignored.append(ingredient)

def getCategorization(item):
    return item[4]

with open('C:/Users/jsouders.DOIT/Documents/RecipeGetter/recipies5.json') as recipies_file:
    data = json.load(recipies_file)
    for recipe in data["recipies"]:
        print "==========="
        print "Importing recipe - " + recipe["meal"]
        if "url" in recipe:
            soup = BeautifulSoup(urllib2.urlopen(recipe["url"]).read().decode('utf-8', 'ignore'))
            print ""
            print "Loaded recipe"
            print ""

            htmlstr += "<h3>" + recipe["meal"] + ":&nbsp<a href=\"" + recipe["url"] + "\">" + soup.find(id="itemTitle").get_text() + "</a></h3>"
            if 'notes' in recipe:
                htmlstr += "<h4>Notes: " + recipe["notes"] + "</h4>"
            ingredients = soup.find_all(id="liIngredient")
            
            for i in range(len(ingredients)):
                quantity = ingredients[i].label.p.find(id="lblIngAmount")
                ingredient = ingredients[i].label.p.find(id="lblIngName")

                if quantity is None:
                    quantity = ""
                else:
                    quantity = quantity.get_text()
                    
                if ingredient is None:
                    ingredient = ""
                else:
                    ingredient = ingredient.get_text().lower()

                if (len(quantity.strip()) + len(ingredient.strip())) != 0:
                    #print quantity + "|" + ingredient
                    #print ingredient
                    #print quantity
                    print "Categorizing " + ingredient
                    filter_check(ingredient, quantity, recipe["meal"])

            print ""
            print "Categorization Successful"
            print ""
        else:
            htmlstr += "<h3>" + recipe["meal"] + ":&nbsp" + recipe["notes"] + "</h3>"
        
    for ingredient in data["ingredients"]:
        print "Categorizing " + ingredient
        filter_check(ingredient.lower(), "N/A", "Extra Ingredient")

        print ""
        print "Categorization Successful"
        print ""
                
    print "==========="
    print "Preparing to write to HTML"
    print ""

    htmlstr += '<h1>Ingredients</h1><table style="width:100%" class="table"><tr><th style="text-align:center">Quantity</th><th style="text-align:center">Ingredient</th><th style="text-align:center">Location</th><th style="text-align:center">Meal</th></tr>';
     
    print "Writing Produce"
    for ingredient in sorted(produce, key=getCategorization):
        htmlstr += "<tr></td><td>" + ingredient[0] + "</td><td>" + ingredient[1] + "</td><td>" + ingredient[2] + "</td><td>" + ingredient[3] + "</td></tr>"

    print "Writing Meat"
    for ingredient in sorted(meat, key=getCategorization):
        htmlstr += "<tr><td>" + ingredient[0] + "</td><td>" + ingredient[1] + "</td><td>" + ingredient[2] + "</td><td>" + ingredient[3] + "</td></tr>"

    print "Writing Middle"
    for ingredient in sorted(middle, key=getCategorization):
        htmlstr += "<tr><td>" + ingredient[0] + "</td><td>" + ingredient[1] + "</td><td>" + ingredient[2] + "</td><td>" + ingredient[3] + "</td></tr>"

    print "Writing Refrigerated"
    for ingredient in sorted(refrigerated, key=getCategorization):
        htmlstr += "<tr><td>" + ingredient[0] + "</td><td>" + ingredient[1] + "</td><td>" + ingredient[2] + "</td><td>" + ingredient[3] + "</td></tr>"

    print "Writing Frozen"
    for ingredient in sorted(frozen, key=getCategorization):
        htmlstr += "<tr><td>" + ingredient[0] + "</td><td>" + ingredient[1] + "</td><td>" + ingredient[2] + "</td><td>" + ingredient[3] + "</td></tr>"

    print "Writing Unknown Food"
    for ingredient in sorted(unknown, key=getCategorization):
        htmlstr += "<tr><td>" + ingredient[0] + "</td><td>" + ingredient[1] + "</td><td>" + ingredient[2] + "</td><td>" + ingredient[3] + "</td></tr>"

    htmlstr += "</table><div style=\"text-align:center\">"

    for recipe in data["recipies"]:
        if "url" in recipe:
            soup = BeautifulSoup(urllib2.urlopen(recipe["url"]).read().decode('utf-8', 'ignore'))
            htmlstr += "<h1><a href=\"" + recipe["url"] + "\">" + soup.find(id="itemTitle").get_text() + "</a></h1><h3>(" + recipe["meal"] + ")</h3>"
            htmlstr += soup.find(id="ulReadyTime").get_text()
            if 'notes' in recipe:
                htmlstr += "<h4>Notes: " + recipe["notes"] + "</h4>"
            htmlstr += "<h3>Ingredients</h3><div class=\"ingredients\">"
            
            ingredients = soup.find_all(id="liIngredient")
            
            for i in range(len(ingredients)):
                quantity = ingredients[i].label.p.find(id="lblIngAmount")
                ingredient = ingredients[i].label.p.find(id="lblIngName")

                if quantity is None:
                    quantity = ""
                else:
                    quantity = quantity.get_text()
                    
                if ingredient is None:
                    ingredient = ""
                else:
                    ingredient = ingredient.get_text()

                if (len(quantity.strip()) + len(ingredient.strip())) != 0:
                    htmlstr += quantity + " " + ingredient + "<br>"

            htmlstr += "</div>"
            for tag in soup.find_all("div", class_="directions"):
                htmlstr += str(tag).decode('utf8')
        else:
            htmlstr += "<h1>" + recipe["notes"] + "</h1><h3>(" + recipe["meal"] + ")</h3>"


    htmlstr += "</div><script>$('.table').on('click','tbody tr',function(event){if($(this).hasClass('highlight')){$(this).removeClass('highlight');}else{$(this).addClass('highlight')}});</script></body></html>"
    html_file = open("C:/Users/jsouders.DOIT/Documents/RecipeGetter/recipe5.html","w")
    html_file.write(htmlstr.encode("UTF-8", 'ignore'))
    html_file.close()
    print "Recipies written to HTML file"

    print ""
    print "==========="
    print "Ignored Ingredients"
    print ""
    for ingredient in ignored:
        print ingredient
