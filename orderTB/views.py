from django.shortcuts import render, HttpResponse
from orderTB.models import Orders

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from orderTB.forms import SignUpForm

def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def toFloat(a):
    if(a):
        return float(a)
    else:
        return 0

def Dashboard(request):
    name = request.user.first_name+ ' '+request.user.last_name
    data = reversed(Orders.objects.all())

    return render(request,'dashboard.html',{'data':data, 'name':name})

def Order(request):
    name = request.user.first_name+ ' '+request.user.last_name
    if request.method == "POST":
        print 'in POST request'
        order_id = request.GET['order_id']
        element = Orders.objects.get(id=order_id)
        count = Orders.objects.all().count()

        a= Orders.objects.create(product_name= element.product_name,cost_price=toFloat(element.cost_price)*66,order_id= count+1,order_status= 'active',product_url=element.product_url)

        a.save()
        return redirect('home')


    if request.method == "GET":
        print 'in GET request'
        order_id = request.GET['order_id']
        element = Orders.objects.get(id=order_id)
        data = {
            'product_name': element.product_name,
            'price': toFloat(element.cost_price)*66,
            'order_id': element.order_id,
            'order_status': element.order_status,
            'product_url': element.product_url
        }

        return render(request,'order.html',{'data':data, 'name':name})
