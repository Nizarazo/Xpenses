from django.shortcuts import render


def expense_list(request):
    return render(request, "core/expense_list.html", {
        'age': 23,
        'color': 'blue',
        'to_buy': [
            'milk',
            'coffee',
            'ice cream',
        ]

    })