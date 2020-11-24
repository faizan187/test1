from django.shortcuts import render


def index(request):
    my_dict = {'insert_content': 'Hello I m from firstAPP'}
    return render(request, 'first_app/index.html', my_dict)
