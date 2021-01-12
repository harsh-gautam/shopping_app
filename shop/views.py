from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from shop.models import Product, Order
from math import ceil
import json, datetime
from django.core.serializers.json import DjangoJSONEncoder
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # query_set = Product.objects.all()
    all_products = []
    categories = {dic['category'] for dic in Product.objects.values('category')}
    for category in categories:
        all_products.append([category, Product.objects.filter(category=category)])
    context = {'all_products':all_products}
    # print(context)
    return render(request, 'shop/index.html', context=context)
    
def product(request, pid):
    product = Product.objects.get(product_id=pid)
    f_price = int((product.price*product.discount)/100) + product.price
    return render(request, 'shop/product.html', {'product':product, 'fprice':f_price})


def update_order_status(oid, status):
    now = datetime.datetime.now().strftime("%c")
    obj = Order.objects.get(order_id=oid)
    obj.updates = obj.updates + ", " + f"${status} at ${now}"
    obj.save()

def checkout(request):
    status = False
    if request.method == "POST":
        NAME = request.POST.get('name')
        EMAIL = request.POST.get('email')
        ADDRESS_1 = request.POST.get('address-1', ' ')
        ADDRESS_2 = request.POST.get('address-2')
        CITY = request.POST.get('city', ' ')
        COUNTRY = request.POST.get('country', 'India')
        STATE = request.POST.get('state', ' ')
        if ADDRESS_2 != None:
            ADDRESS = ADDRESS_1 + ", " + ADDRESS_2 
        else:
            ADDRESS = ADDRESS_1
        ZIP = request.POST.get('zip')
        PHONE = request.POST.get('phone')
        PAYMENT_METHOD = request.POST.get('paymentMethod')
        ITEMS = request.POST.get('itemsJson')

        now = datetime.datetime.now().strftime("%c")
        orders = Order( name=NAME,
                        email=EMAIL,
                        phone=PHONE, 
                        address=ADDRESS, 
                        city=CITY, 
                        state=STATE, 
                        country=COUNTRY, 
                        zipcode=ZIP, 
                        payment_mode=PAYMENT_METHOD, 
                        itemsjson=ITEMS,
                        updates=f"Order placed at ${now}")
        orders.save()
        status = True

    products_data = Product.objects.all().values_list('product_id','product_name', 'price')
    products_json = json.dumps(list(products_data), cls=DjangoJSONEncoder)
    # print(products_json)
    return render(request, 'shop/checkout.html', {'products': products_json, 'status': status})

def cart(request):
    products_data = Product.objects.all().values_list('product_id','product_name', 'price', 'image', 'discount')
    products_json = json.dumps(list(products_data), cls=DjangoJSONEncoder)
    # print(products_json)
    return render(request, 'shop/cart.html', {'products': products_json})

def myorders(request):
    if request.method == "POST":
        try:
            json_obj = json.loads(request.body)
            EMAIL = json_obj['email']
            orders = Order.objects.filter(email=EMAIL).values('order_id', 'itemsjson', 'totalprice', 'updates')
            orders_json = {}
            for order in orders:
                keys = list(json.loads(order['itemsjson']).keys())
                ids =  [key[-1] for key in keys]# taking order id
                products = Product.objects.filter(product_id__in=ids).values('product_id', 'product_name')
                t = {'products': list(products), 'totalprice': order['totalprice'], 'updates': order['updates']}
                orders_json[order['order_id']] = t
            print(orders_json)
            return JsonResponse(orders_json)
        except Exception as e:
            return JsonResponse({})
    # for order in orders:
    #     itemsjson = 

    return render(request, 'shop/trackorders.html')

def help(request):
    return render(request, 'shop/help.html')

def search(request):
    return render(request, 'shop/search.html')

def about(request):
    return render(request, 'shop/about.html')
    
def categories(request):
    return render(request, 'shop/not-ready.html')

