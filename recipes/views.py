from django.shortcuts import render

def selection_recipes(request):
    context = {
        'header': 'Список блюд',
        'DATA': {
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
            'russian salad': {
                'картошка': 60,
                'морковь': 24,
                'свекла': 60,
                'соленые огурцы': 24,
                'консервный горошек': 26,
            }

        }
    }

    return render(request, 'recipes.html', context)


def omlet(request, servings=2):
    if servings > 1:
        context = {
            # 'header': 'Ингредиенты для омлета',

            'omlet': {
            'яйца, шт': 2 * servings,
            'молоко, л': 0.1 * servings,
            'соль, ч.л.': 0.5 * servings,
            }
        }
    else:
        context = {
            'omlet': {
                'яйца, шт': 2,
                'молоко, л': 0.1,
                'соль, ч.л.': 0.5,
            }
    }

    # for item in context['omlet'].values():
    #    print(item * 4)
    # print(type(item))

    return render(request, 'omlet.html', context)

def pasta(request):
    context = {
        'header': 'Ингредиенты для Пасты',
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        }
    }
    return render(request, 'pasta.html', context)

def buter(request):
    context = {
        'header': 'Ингредиенты для Бутерброда',
        'buter': {
                'хлеб, ломтик': 1,
                'колбаса, ломтик': 1,
                'сыр, ломтик': 1,
                'помидор, ломтик': 1,
            }
    }
    return render(request, 'buter.html', context)

def russian_salad(request):
    context = {
        'header': 'Ингредиенты для Винегрета',
        'russian_salad': {
                'картошка': 60,
                'морковь': 24,
                'свекла': 60,
                'соленые огурцы': 24,
                'консервный горошек': 26,
            }
    }
    return render(request, 'russian_salad.html', context)