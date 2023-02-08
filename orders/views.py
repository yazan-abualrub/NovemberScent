from django.shortcuts import render, redirect
from django.contrib import messages
from scents.models import Product
from orders.models import Order
from orders.models import OrderDetails
from django.utils import timezone
from orders.models import Payment



def addToCart(request):

    if request.method == "POST" and 'AddToCart' in request.POST and request.user.is_authenticated and not request.user.is_anonymous:

        pro_id = request.POST['pro_id']
        quantity = request.POST['quantity']

        order = Order.objects.all().filter(user=request.user, is_finished=False)
        

        pro = Product.objects.get(id=pro_id)

        if order:
            oldOrder = Order.objects.get(user=request.user, is_finished=False)

            if OrderDetails.objects.all().filter(order=oldOrder,
                                                 product=pro).exists():
                orderdetails = OrderDetails.objects.get(
                    order=oldOrder, product=pro)
                orderdetails.quantity += int(quantity)
                orderdetails.save()
            else:
                orderdetails = OrderDetails.objects.create(
                    product=pro, order=oldOrder, price=pro.price, quantity=quantity)

        else:
            newOrder = Order()
            newOrder.user = request.user
            newOrder.OrderDate = timezone.now()
            newOrder.is_finished = False
            newOrder.save()
            orderdetails = OrderDetails.objects.create(
                product=pro, order=newOrder, price=pro.price, quantity=quantity)

        return redirect('cart')

    else:
        return redirect('signin')


def cart(request):

    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.all().filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.all().filter(order=order)
            total = 0
            for sub in orderdetails:
                total += sub.price * sub.quantity
            context = {
                'products': Product.objects.all(),
                'order': order,
                'orderdetails': orderdetails,
                'total': total,
            }

    return render(request, 'orders/cart.html', context)


def RemoveFromCart(request, orderdetails_id):

    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            orderdetails.delete()

    return redirect('cart')


def AddQty(request, orderdetails_id):

    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            orderdetails.quantity += 1
        orderdetails.save()
    return redirect('cart')


def SubQty(request, orderdetails_id):

    if request.user.is_authenticated and not request.user.is_anonymous and orderdetails_id:
        orderdetails = OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id == request.user.id:
            if orderdetails.quantity > 1:
                orderdetails.quantity -= 1
                orderdetails.save()

    return redirect('cart')


    
def payment(request):
    context = None
    ShipAddress = None
    ShipPhone = None

    if request.method == "POST" and 'ButtonPayment' in request.POST and 'ShipAddress' in request.POST and 'ShipPhone' in request.POST:

        ShipAddress = request.POST['ShipAddress']
        ShipPhone = request.POST['ShipPhone']


        if request.user.is_authenticated and not request.user.is_anonymous:
            if Order.objects.all().filter(user=request.user, is_finished=False):
                order = Order.objects.get(user=request.user, is_finished=False)

                payment = Payment(order=order, ShipAddress=ShipAddress, ShipPhone=ShipPhone)
                payment.save()
                order.is_finished = True
                order.save()
                messages.success(request, 'Order is finished')

        context = {
            
            'ShipAddress': ShipAddress,
            'ShipPhone': ShipPhone,            
        }

        return redirect('myorders')

    else:

        if request.user.is_authenticated and not request.user.is_anonymous:
            if Order.objects.all().filter(user=request.user, is_finished=False):
                order = Order.objects.get(user=request.user, is_finished=False)
                orderdetails = OrderDetails.objects.all().filter(order=order)
                total = 0
                for sub in orderdetails:
                    total += sub.price * sub.quantity
                context = {
                    'products': Product.objects.all(),
                    'order': order,
                    'orderdetails': orderdetails,
                    'total': total
                }

    return render(request, 'orders/payment.html', context)

def Myorders(request):
    
    context = None
    AllOrders = None

    if request.user.is_authenticated and not request.user.is_anonymous:
        AllOrders =  Order.objects.filter(user=request.user)

    context = {'AllOrders':AllOrders,    
            }

    return render(request, 'orders/myorders.html', context)
