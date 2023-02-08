from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from scents.models import Product
import re
# Create your views here.


def signup(request):
    


    if request.method == "POST":
        fname = None
        lname = None
        address = None
        email = None
        password = None

       # message Error if User edit field's name
        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'Error in First name ')

        if 'lname' in request.POST:
            lname = request.POST['lname']
        else:
            messages.error(request, 'Error in Last name ')

        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'Error in Address ')

        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'Error in Email ')

        if 'password' in request.POST:
            password = request.POST['password']
        else:
            messages.error(request, 'Error in password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is taken')
            return redirect('signup')
        else:
            patt = '\w[\w\.-]*@\w[\w\.-]+\.\w+'
            if re.match(patt, email):

                user = User.objects.create_user(
                    first_name=fname, last_name=lname, email=email,
                    username=email, password=password)
                user.save()
                userProfile = UserProfile(user=user, address=address)
                userProfile.save()

                # clear fields after create accounts
                fname = ''
                lname = ''
                address = ''
                email = ''
                password = ''

                messages.success(request, 'Create account successfully')
                return redirect('signin')

            else:
                messages.error(request, 'Error')
                return render(request, 'accounts/signup.html', {
                    # keep fields if an error happend
                    'fname': fname,
                    'lname': lname,
                    'address': address,
                    'email': email,
                    'password': password
                })

    else:

        return render(request, 'accounts/signup.html')


def signin(request):
    

    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            if 'rememberMe' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or Password')

            return render(request, 'accounts/signin.html', {
                'email': email
            })
            


    else:
        return render(request, 'accounts/signin.html')


def profile(request):
    if request.method == 'POST':
        return redirect('profile')
    else:
        if request.user is not None:
            context = None
            if not request.user.is_anonymous:

                userProfile = UserProfile.objects.get(user=request.user)

                context = {
                    'fname': request.user.first_name,
                    'lname': request.user.last_name,
                    'email': request.user.email,
                    'address': userProfile.address,
                    'password': request.user.password,

                }
            return render(request, 'accounts/profile.html', context)

        else:
            return redirect('signin')


def Edit(request):
    
  
    
    if request.method == 'POST':
        if request.user is not None:
            userProfile = UserProfile.objects.get(user=request.user)

            if request.POST['fname'] and request.POST['lname'] and request.POST['address']and request.POST['password']:

                request.user.first_name = request.POST['fname']
                request.user.last_name = request.POST['lname']
                userProfile.address = request.POST['address']
                if not request.POST['password'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['password'])

                request.user.save()
                userProfile.save()
                messages.success(request, 'Changes had been saved')
                return redirect('signin')

    else:
        return render(request, 'accounts/Edit.html')

def product_fav(request, pro_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        userProfile = UserProfile.objects.get(user=request.user)
        pro_fav = Product.objects.get(pk=pro_id)
        if UserProfile.objects.filter(user=request.user, product_fav=pro_fav).exists():
            userProfile.product_fav.remove(pro_fav)
            messages.success(request, 'Removed from your favorites.')

        else:
            userProfile = UserProfile.objects.get(user=request.user)
            userProfile.product_fav.add(pro_fav)
            return redirect('showFav')

    else:
        
        return redirect('signin')
    return redirect('/scents/' + str(pro_id))

    
def showFav(request):
    
    
    
    context =  None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = UserProfile.objects.get(user=request.user)
        pro = userInfo.product_fav.all()
        context = {'products':pro,
}
        
    return render(request,'scents/showFav.html', context)


def logout(request):

    if request.user.is_authenticated:
        auth.logout(request)

    return redirect('index')
