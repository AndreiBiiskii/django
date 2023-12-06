from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def kitchen(request):
    servings = request.GET.get('servings')
    dish = request.path_info.split('/')[1]
    recipe = dict()
    if servings:
        for ingredient, amount in DATA[dish].items():
            recipe[ingredient] = amount * int(servings)
    else:
        recipe = DATA[dish]
    print(recipe)
    context = {'recipe': recipe}
    return render(request, 'calculator/order.html', context)
