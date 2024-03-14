from django.shortcuts import render,redirect
from .models import *
from veg.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render
# from .forms import ContactForm


# Ensure the model name is capitalized and matches the model in your models.py

def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_price = data.get('recipe_price')

        print(recipe_name)
        print(recipe_description)
        print(recipe_price)

        # Create a new Recipe object and save it to the database
       ## new_recipe = recipe(name=recipe_name, description=recipe_description, price=recipe_price)
       ## new_recipe.save()
    
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_price = recipe_price,
        )
        # Redirect to a success page or render a template
    queryset = Recipe.objects.all
    print(queryset)
    context = {'queryset': queryset}

    return render(request, 'recipe.html',context) 
def delete_receipe(request,id):
    print(id)
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            # Redirect to a success page or home page after login                            
            return redirect('/') # Adjust the redirect URL as needed
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login/') # Redirect back to the login page with error message
        
    return render(request, 'login.html')



def signup_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username Already Exist.")
            return redirect('/signup/')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )

        messages.success(request, "Account created successfully.")
        # Render the same page to display the success message
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def logout_page(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('/login/')  
    



def form_page(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data.get('subject')
            question = form.cleaned_data.get('question')
            # Here you can save the data to the database or send an email
            return render(request, 'success.html') 
    else:
        form = ContactForm()

    return render(request, 'form.html', {'form': form})









