from datetime import datetime

from django.shortcuts import render

from .forms import SubsriberForm


def index(request):
    a = 'test'
    today = datetime.now().date().strftime('%A, %d %b %Y')

    form = SubsriberForm(request.POST or None)

    if request.method == 'POST':
        s = request.POST
        print(s)
        print(f"{s['name']} - {s.get('email')}")


    return render(request, 'shop/index.html', locals())
