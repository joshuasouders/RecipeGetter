This is the backend for a service that will take submitted URLs to popular recipe sites, scrape those sites, format a grocery list for those recipes, and present the recipes in an easily readable format. It is very useful for people who want to make a weekly mealplan but don't want to do the work of compiling grocery lists and keeping track of all of the recipe links themselves.

Currently the input is a JSON file formatted like:

```
{ 
	"recipies": [
		{
			"meal": "Monday Main", 
			"url": "http://allrecipes.com/Recipe/Honey-Baked-Chicken-II/Detail.aspx?evt19=1&referringHubId=662"
		},
		{
			"meal": "Monday Side", 
			"url": "http://allrecipes.com/Recipe/Gourmet-Mushroom-Risotto/Detail.aspx?event8=1&prop24=SR_Thumb&e11=mushroom&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i1&scale=2&ismetric=0"
		},
		{
			"meal": "Tuesday Main", 
			"url": "http://allrecipes.com/Recipe/Sandys-Homemade-Broccoli-and-Cheddar-Soup/Detail.aspx?event8=1&prop24=SR_Title&e11=chili%20mild&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i3"
		}
	]
}
```

and the output is a HTML file that is suitable to use for your weekly meal plan. While it isn't at a point where it's ready to be used by the public, I currently use it weekly and improve upon it (categorizing groceries into produce/meat/etc) until I get the time to finish it, build a real frontend, and release it.

Right now it's 100% Python. While I really needed this product to fill a personal need, I also wanted to experiment with Python scraping and HTML generation.