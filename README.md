# PBP_Inventory | Assignment 2

The following link will redirect you to the App: [Click Me!](https://curry-under-armour-inventoryy.adaptable.app/main/)

## How do you implement the tasks in the checklist?

* __Creating a new Django project:__<br>
Before starting the new Django project, I firstly created a new git repository locally and online on GitHub. After preparing the repository, I started creating the Django project by creating a new directory named, "PBP_Inventory". The next step was to initialize the virtual environment by running the command, `python -m venv env`, which was followed by activating it using the script, `env\Scripts\activate.bat` in order to isolate the dependencies and the package. Afterwards, the dependencies were installed in the same directory using `pip install -r requirements.txt` in the `requirements.txt` file, which was followed by configuring the project by adding `*` to `ALLOWED_HOSTS` within `settings.py`, and adding a `.gitignore` file with the contents from the tutorial. Finally, the project was created by running the command `django-admin startproject UnderArmour_Curry_Inventory .`

* __Creating an app with the name main on that project.:__<br>
Firstly, I tested to run the Django server by running `python manage.py runserver`. Once successful, I created an app with the name `main` by running `python manage.py startapp main` which creates a new directory that provides the basic structure for the application. To register `main` as an application, I just added `main` to `INSTALLED_APPS` in `settings.py` within the project directory.

* __Creating a URL routing configuration to access the main app.:__<br>
To configure the URL routing, I modified `urls.py` within the `main` app directory and added, `path('', show_main, name='show_main')` within an list called `urlpatterns` along with some other imports such as `path` from `django.urls` for defining URL patterns, and importing `show_main` function from `main.views` as the view to be displayed each time the URL is utilized by the user.

* __Creating a model on the main app with name Item.:__<br>
I modified `models.py` within the `main` application and imported the code provided in the tutorial (which also included an import `models` from `django.db`). Following this, I changed the name of the class from `Product` to `Item`, and added the `name` as the name of the item on the `CharField` type, `amount` as the count of the item on the `IntegerField` type, `description` as the item despcription with `TextField` type, and `product_release_date` with the `DateField` type.

* __Creating a function in views.py that returns an HTML template containing the application name, my name, and my class.:__<br>
This step was done in the `views.py` file inside the `main` application directory. I added the `show_main` function that takes the `request` parameter to handle HTTP requests and return the desired view for the user whenever the URL is accessed. The `context` dictionary within the function was modified so that it includes the `appName`, my `name`, and my `class`. To make my website more tailored/specific as an inventory app, I added `description`, `release_date`, and `amount` data to be passed. Note that in `main.html` each data item in `context` is referenced as for example, `{{class}}`

* __Creating a routing in urls.py to map the function inviews.py to an URL.:__<br>
The `urls.py` file inside the `UnderArmour_Curry_Inventory` directory was modified to include the the URL pattern `path('main/', include('main.urls'))` as well as the import `path` and `include` from `django.urls` in order to import URL routes that originate from other apps, such as `main`, into the `urls.py` file. Note that this was then tested using the `python manage.py runserver` to see if it worked.

* __Deploying the app to Adaptable so it can be accessed through the internet.:__<br>
After finalizing the app and testing it to see if it runs locally, I ran the `add`, `commit`, `push` commands to GitHub online so that the local repository synchronizes with the repository online. Afterwards, I went over to Adaptable.io in order to deploy the app by following the same configurations provided in the tutorial.


## Create a diagram explaining the flow of client requests to a Django web app and its response.
<img src="/assets/Flowchart_PBP_Assignment2.png">


## What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?

The purpose of a virtual environment is to help keep dependencies and packages required by different projects (such as a Django project) separated/isolataed from one another as well as from the global/base Python environment so that conflicts with other versions on the computer are prevented. For example, we may need a virtual environment in the case that we are working with more than one Django project or when we are using third-party Python packages to build Django apps. 

Note that it is possible to create a Django web app without a virtual environment and install Django globally, however, it is highly recommended that a virtual environment is utilized. This is because installing Django globally could case version conflicts and system-level package dependencies issues (such as updating the wrong Django version for a Django project).


## What is MVC, MVT, and MVVM? Explain the differences between the three.

MVC, MVT, and MVVM are essentially industry-recognized concept/architechture design patterns to develop applications. 

MVC stands for Model-View-Controller, which is an architechtural pattern that splits the code into 3 components/layers while developing the application. The Model component is in charge of handling the domain/application logic and communicates directly with the database as well as network layers. Model in MVC also defines certain rules that manage data handling, processing, and modifications. The View component displays the Model's stored data and is accountable for data representation/visualization in the user interface. The Controller in MVC is a component that integrates a relationship between the View and Model components so that the core app logic gets updated of every user response and updates the Model. The key difference in MVC is that the Model has no understanding/knowledge of the View (interface) or the Controller component.

MVT is known as the Model-View-Template architechtural design pattern, which is a pattern utilized to systematically separate key components of an application as well as organize and manage code in a structured manner. The Model component in MVT is utilized for storing the application's data, its structure, as well as the application logic in order to manage and organize data. It also manages communications with the database. The View component is responsible for the presentation of logic and the visualization of data managed by the Model in the MVT architechture; it acts a presentation manager that retrieves data from the Model and displays it to the user, which is the clear difference from MVVM and MVC patterns. Conversely, the Template component is utilized to seperate HTML code from the app logic. The Template manages and designs the user interface in the application by fetching the data from the Model and the input from the View component to process the data and manage the interface in MVT.

Lastly, MVVM is known as the Model-View-ViewModel Architechtural Pattern, which suggests separating the data presentation logic from the core business logic aspect of the application; it provides a clear separation between the domain/application logic and the presentation logic. For instance, the Model component is accountable for abstracting sources of data, and then works together with the ViewModel component to retrieve and save that data. The View component informs the ViewModel on any action/input from the user in the application. It essentially observes the ViewModel component for any notifications and then binds the data to the ViewModel; note that it does not contain any application logic. ViewModel is a component that is exclusive to the MVVM pattern, thus making this the primary difference from MVT and MVC. This component abstracts the view layer and acts as a "wrapper" for the application data. In other words, it exposes the streams of relevant data to the View component, and creates a link between the Model and View component.

# PBP_Inventory | Assignment 3

## What is the difference between `POST` form and `GET` form in Django?

The `POST` form in Django is a HTTP method that returns Django's login form that the browser bundles up, encodes it for the purpose of transmission, and then receives its response in return. Conversely, the `GET` form is an HTTP method that bundles up submitted data from the form into a string and then utilizes it to create a URL that contains the address where the data should be sent, as well as data keys and values. 

The difference between the two is that the `POST` method is utilized to submit (internally) the data of form elements to a web server using the HttpPost object without URL parameters, and to also used to change the state of the system or create requests to make changes in the database. On the other hand, the `GET` method is utilized to submit the data of form elements to a webserver using URL parameters, and used for requests that do not affect the state of the system/database.

## What are the main differences between XML, JSON, and HTML in the context of data delivery?

In the context of data delivery, XML (Extensible Markup Language) is a markup language that provides rules in defining any type of data that would be transmitted. In particular, XML uses tags to differentiate between data attributes from the actual data for information exchange. Additionally, XML, stores data in a tree structure that displays information layers, starting with a root and having child elements.

 On the other hand, JSON (JavaScript Object Notation) is another type of data representation or an open data interchange format that is human and machine-readable, making it more simpler and flexible. JSON represents data using an Object (a collection of key-value pairs to create a structure similar to a map) and an Array (an ordered collection of values separated by commas).
 
 Differing further from these two, HTML (HyperText Markup Language) is a language used to create the basic structure of web pages and link them together. HTML documents are usually made up of tags (`< >`) to manage and separate the structure of the web page. In data delivery, HTML is utilized to render web information and not exactly data interchange between end-users, however, more towards in displaying the contents of the web page in a structured and visually attractive manner.
 
 ## Why is JSON often used in data exchange between modern web applications?

JSON is often used in data exchange between modern web applications because of its fast data interchange and web service processing results, human-readable text/code, lightweight characteristic, as well as fewer coding requirements. JSON is text-based, making it very lightweight for developers and provides an easy-to-parse data format which implies less code needed for parsing purposes. Additionally, JSON also provides better schema support for databases, and is highly interoperable/compatible between applications/technologies such as WebSocket, GraphSQL, and RESTful (Representational State Transfer) web services.

## Explain how you implemented the checklist above step-by-step.

* __Create a form input to add a model object to the previous app.__<br>
In creating the `form` input, I first created a `forms.py` file inside the `main` folder. In the file, a class called `ProductForm` was created with the parameter `ModelForm` that was imported from `django.forms`. An additional class called `Meta` was nested within `ProductForm`, at which I had the `model = Item` that was imported from `main.models` that will be used to point to the `Item` model used by the form. A `fields = ["name", "price", "description"]` list was also created to select the attributes from `Item` as form fields; note that `product_release_date` was not added from `Item` since the date would be added automatically. Afterwards, I added a function called `create_product` in the `views.py` file in the `main` directory that accepts the parameter `request` so that it could automatically add a new product/Item (model object) when the form is submitted. The `ProductForm` is created using the `form = ProductForm(request.POST or None)` which is filled with the user's input in `request.POST`. The form is then validated using `form.is_valid()` and then saved with `form.save()` to the app's database. If valid, the function returns `HttpResponseRedirect(reverse('main:show_main'))` which redirects the page after the form is saved. Otherwise, the function returns `render(request, "create_product.html", context)` which renders `create_product.html`; a file that uses the `create_product` function to add products and create a form with the `POST` method. In the same file, the `show_main` function is modified to include `products = Item.objects.all()` to fetch all `Item` objects from the app's database.

* __Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.__<br>
Adding 5 views for the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats involves updating the `main.html` and `views.py` files. To display this in the app from HTML, I created a table using `<table>` tags and a for-loop to iteratively show the product data (`name`, `price`, `description`, `product_release_date`). A button called `Add New Product` is added using the `<button>` tag and referenced to the `create_product` function in `main` using the `a=href="{% url 'main:create_product' %}"` attritbute.

To add the XML, JSON, XML by ID, and JSON by ID formats as views, the `views.py` file is added with the following functions:

<b> Function showing XML view </b>
```py
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

<b> Function showing JSON view </b>
```py
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
    
<b> Function showing XML view by ID </b>
```py
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

<b> Function showing JSON view by ID </b>
```py
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

For the `show_xml` and `show_json` functions, they both accept `request` parameters stores a variable `data = Item.objects.all()` to store all fetched `Item` objects, and returns the previously fetched data as `XML` and `JSON` formats respectively as an  `HttpResponse`.

For the `show_xml_by_id` and `show_json_by_id` functions, they both accept `request` and `id` parameters. They also use `data = Item.objects.filter(pk=id)` to query the result of data given a specific `id` and returns an `HttpResponse` containing the serialized data in `XML` and `JSON` formats respectively. 


* __Create URL routing for each of the views added in point 2.__<br>
I created the URL routing for each of the views previously by opening the `urls.py` file inside `main` and imported the functions created using `from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id`. Afterwards, I added the following URL paths into the `urlpatterns` list so that they can access the imported functions:

```py
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'), 
        path('xml/', show_xml, name='show_xml'), # URL path for XML
        path('json/', show_json, name='show_json'), # URL path for JSON
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), # URL path for XML by ID
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), # URL path for JSON by ID
]
```

## Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<img src="/assets/htmlView.png">
<img src="/assets/xmlView.png">
<img src="/assets/jsonView.png">
<img src="/assets/xmlByIDView.png">
<img src="/assets/jsonByIDView.png">


# PBP_Inventory | Assignment 4

## Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.
<img src="/assets/loginUser1.png">
<img src="/assets/loginUser2.png">


## What is UserCreationForm in Django? Explain its advantages and disadvantages.
The UserCreationForm in Django is a built-in model that inherits from Django's ModelForm class (and imported from django.contrib.auth.forms) that is used for creating a new user for a web application; note that UserCreationForm has three fields that include username, password1, and password2. 

The advantage of UserCreationForm in Django is that it is simple to implement to a web application as there is a default template from the Django framework to create a form for a particular user. The disadvantage of UserCreationForm is that it is limited to only the three fields of username, password1, and password2. For instance, we cannot add an email field if we were going to send a verification email to a user from the web application. Another disadvantage is the potential of hardcoding confidential/sensitive information to the form which is prone to exploits if visible to the general public. For instance, we may accidentally hardcode personal username or passwords into the UserCreationForm fields and upload it to a public repository (such as GitHub) without noticing.


##  What is the difference between authentication and authorization in Django application? Why are both important?
Authentication in a Django application could be defined as verifying a user to be who they claim to be (process of verifying who a user is when they login), while authorization is determining what an authenticated user is allowed to do (process of verifying that a user has legitimate access to something). Authentication and authorization are both important for four main reasons; in particular, these reasons are security, compliance, user experience, and control. 

Both authentication/authorization ensure that only authorized users could access your API (application program interface) which prevents unauthorized data breaches, access to data, as well as other potential security risks. Additionally, proper authentication/authorization measures ensure compliance from your API in the Django Rest Framework with industry and government regulations. User experience and control are further emphasize the importance of authentication/authorization since users can create a personalized experience with their own accounts that they login to access personal resources(user experience), as well as preventing misuse/abuse to your API through authorization (control).


## What are cookies in website? How does Django use cookies to manage user session data?
Cookies could be defined as small pieces of information sent by a web server to your browser to be stored for future use; cookies will then be sent back by the web browser for future page requests on order to save bandwidth on the network. Additionally, cookies are usually made up of a single name-value pair send in the header of the client's HTTP POST or GET request, and are usually utilized for authentication, user tracking, as well as maintaining user preferences.

Django uses cookies to manage user session data by storing them in a database, which is a model used to store user session data. First, the cookie parameter would be read when it is passed by the browser, and then data would be fetch and stored in a session model by Django. Afterwards, the information in the session would be modified as needed, and the corresponding cookie would then be sent back to the browser in the future whenever it is needed by the web application.

## Are cookies secure to use? Is there potential risk to be aware of?
Generally speaking, cookies are not secure by their nature. What matters is how they are utilized/implemented by the web application and how they are fetch or stored by the web browser. This is because cookies can contain the webpage's header, the user's personal preferences and sensitive information within a particular website, as well as validity and path information on the website. Due to this fact, cookies are prone to potential risks associated with it such as exploitation and attacks from cybercriminals that violate privacy and collect personal/sensitive information. These attacks may include Cross-site request forgery (CSRF), session fixation, cross-site scripting (XSS), cookie tossing attack, cookie overflow attack, and many more.


## Explain how you implemented the checklist above step-by-step

* __Implement registration, login, and logout functions to allow users to access the previous application.__<br>

Firstly, I opened the `views.py` file and imported the necessary imports such as `redirect`, `UserCreationForm`, and `messages`. Following this, a function called `register` was created with the following code:

```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

The `register` function accepts the `request` parameter (which is an HTTPrequest from the web browser) and uses the `POST` method for the request to save the `UserCreationForm` made by `form = UserCreationForm(request.POST)`. If the form created is valid (validated using `form.is_valid()`), the form is saved and a new data from the form is created through `form.save()` with a message  displayed to the user with `messages.success(request, 'Your account has been successfully created!')`. The register function returns `return redirect('main:show_main')` which redirects the page after saving the form. Note that an HTML file called `register.html` was created for the function in the `main\templates` folder afterwards.


After importing `authenticate` and `login` imports (to authenticate and login the user given a successful authentication attempt), the `login_user` function was created next in `views.py` with the following code:

```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

The function essentially authenticates a user utilizing a given username and password sent through the request through the code `authenticate(request, username=username, password=password)`. If a user is present (`user is not None`), then the function allows the user to log in and redirects them to the main page through `HttpResponseRedirect(reverse("main:show_main"))` and collects their cookies on their last login with `response.set_cookie('last_login', str(datetime.datetime.now()))` and returns the response. Otherwise, the function will output a message with the code `messages.info(request, 'Sorry, incorrect username or password. Please try again.')` Then, an HTML file called `login.html` was created in the `main/templates` folder for the login.


Following this and still inside `views.py`, the `logout_user` function was implemented using the following code after importing `logout`:

```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

``` 

This function has the capability delete the currently logged in user session using `logout(request)` and returns the response `HttpResponseRedirect(reverse('main:login'))` after deleting the cookie for every last login of the user with `response.delete_cookie('last_login')`. Following this, a logout button was added to `main.html` and the `show_main` function was modified with in its context variable using `'last_login': request.COOKIES['last_login']` to add `last_login` cookie data to the HTTP response to display on the web page. 

Finally, all three functions are imported to `urls.py` and a new url path to `urlpatterns` were added for each respective function to access them through the import:

```py
from main.views import register
from main.views import login_user
from main.views import logout_user

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), #add url path to register
    path('login/', login_user, name='login'), #add url path to login
    path('logout/', logout_user, name='logout'), #add url path to logout
]

```


* __Create two user accounts with three dummy data entries for each account using the model previously created in the application.__<br>
Two user accounts were created on the web application by registering them as well as creating a username and password for each account. Afterwards, 3 dummy data were added to each account by clicking the `Add New Product` button.


* __Connect Item model with User.__<br>
The Item model was connected with User by first importing `User` to `models.py` and then adding `user = models.ForeignKey(User, on_delete=models.CASCADE)` in the `Item` model (class). Then, the `create_product` in `views.py` was updated as such:

```py

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

```

The function was modified such that the `user` field was set to the `User` object to indicate the product belongs to that user when the user is currently logged-in. Afterwards, the `show_main` function was added with `'name' : request.user.username` so that it can request the corresponding username of the user when the main page is displayed to the user.


# PBP_Inventory | Assignment 5


##  Explain the purpose of some CSS element selector and when to use it.

1. ID Selector: The ID selector is a CSS selector that targets an element within an HTML file that has a specific value for its `id` attritbute. Note that the ID selector is utilized to select one unique element since the id of an element is considered unique within a page. Furthermore, we write a hash (`#`) character followed by the id of an element in order to select the element that has a specific id. For instance, `#something1` selects an HTML element with `id="something1"`.

2. Class Selector: The Class selector targets an HTML element that is specified with a certain value in its `class` attribute. We utilized the Class selector by  writing a period (`.`) and then followed by the defined class name for the element in the HTML file. For instance, `.something2` selects an HTML element with `class="something"`. Note that you can also specify only particular HTML elements is selected by a class such as `element.something2`.

3. Element Selector: The Element selector essentially targets all HTML elements of a particular type. Note that this selector is used when we are trying to apply a style towards all instanecs of a certain HTML element. For example, we can write `h1` which targets an HTML element or tag `<h1>`. We could also write the Element selector without any leading hash (`#`) or period (`.`) characters.


## Explain some of the HTML5 tags that you know.

1. `<nav>`: This tag defines a section of navigation links; specifically used to create a navigation bar/area for a certain website.
2. `<article>`: This tag is used to define an independent piece of content within a document. For example, a newspaper article or an entry in a blog.
2. `<section>`: This tag is used to represent a particular section within the HTML file, such as a section of a document, a header, footer, etc.


##  What are the differences between margin and padding?

According to the CSS Box Model, margin could be defined as the transparent space around the Border of an element (which is another section in the CSS Box Model) and is the outermost layer of the Box Model. Conversely, padding is used to represent the transparent space around the content of an element and is the innermost layer within the CSS Box Model.


## What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?

Tailwind CSS constructs layouts through the composition of predefined utility classes, allowing for a highly adaptable and flexible approach to styling. Its CSS file remains compact, loading only the utility classes applied in a project, which contributes to smaller file sizes. However, mastering Tailwind CSS can be initially challenging because it demands an understanding of how to effectively utilize and combine these utility classes.

Conversely, Bootstrap relies on pre-designed styles and components, offering a collection of readily available designs that can be readily implemented. This framework yields larger CSS files due to the inclusion of numerous predefined components. Bootstrap's strength lies in its ability to maintain design consistency throughout a project using these components. Furthermore, Bootstrap is an excellent choice for beginners, as it presents a gentler learning curve, allowing newcomers to commence with pre-made components and styles.

Tailwind is a good choice when you want fine-grained control over your styles, need to build custom designs, or prefer a more minimalistic and utility-first approach. On the other hand, Bootstrap is a good choice when you want to quickly prototype a project or if you prefer using pre-designed components to speed up development. It's also a good fit for projects where you want a consistent and visually appealing default design.


## Explain how you implemented the checklist above step-by-step.

* __Customize login, register, and add item page as creative as possible.__<br>

Before customizing the pages, I first added the `<meta name="viewport">` tag to the `base.html` file so that my web page could adapy to the size and behavior of mobile devices. Afterwards, I created two new functions in `views.py` called `edit_product` (which also has a corresponding html file called `edit_product.html`) and `delete_product` so that I could edit and delete products on my web application according to their specific id to identify which product belongs to which user:

```py
    def edit_product(request, id):
    # Get product by ID
    product = Product.objects.get(pk = id)

    # Set product as instance of form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save the form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

```py
    def delete_product(request, id):
    # Get data by ID
    product = Product.objects.get(pk=id)
    # Delete data
    product.delete()
    # Return to the main page
    return HttpResponseRedirect(reverse('main:show_main'))
```

Following this, I imported these functions into `urls.py` and created a path url to `urlpatterns` to access both of the imported functions:

```py

from main.views import edit_product, delete_product

...
path('edit-product/<int:id>', edit_product, name='edit_product'),
path('delete/<int:id>', delete_product, name='delete_product'), 
...

```

Afterwards, I customized the pages using Tailwind CSS into my django project. I first had to setup the Tailwind CSS Framework and installed NodeJS and  `django-tailwind` into the project using `python -m pip install django-tailwind` and `python -m pip install django-tailwind[reload]` for automatic page reloads. Then, I had to add `'tailwind'` into the `INSTALLED_APPS` in `settings.py`:

```py
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
]
```

I then initialized a Tailwind CSS compatible Django app by naming it `theme` to the django project using `python manage.py tailwind init` and then proceeded to add `'theme'` into the `INSTALLED_APPS`:

```py
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme'
]
```
I also had to make sure `INTERNAL_IPS` was added to `settings.py`:

```py
INTERNAL_IPS = [
    "127.0.0.1",
]

```

I also installed Tailwind Dependencies using `python manage.py tailwind install` and modified my `base.html` file by adding `{% load static tailwind_tags %}` and `{% tailwind_css %}` into the head to include Tailwind's stylesheet. Configuring automatic page reloads was next by adding `'django_browser_reload'` to `INSTALLED_APPS` and the middleware `'django_browser_reload.middleware.BrowserReloadMiddleware'` to `MIDDLEWARE` in `settings.py`. Finally, I imported `path("__reload__/", include("django_browser_reload.urls")),` into `urlpatterns` in `urls.py` within my main application's root folder and started to use Tailwind by running the command `python manage.py tailwind start`. 


1. The login page was customized using the following code for Tailwind:
```py
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen py-6 flex flex-col justify-center bg-gradient-to-r from-yellow-400 to-blue-500 sm:py-12">
    <div class="relative py-3 sm:max-w-xl sm:mx-auto">
        <div
			class="absolute inset-0 bg-gradient-to-r from-blue-300 to-blue-600 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl">
		</div>
        <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
            <div class="max-w-md mx-auto">
                <div>
                    <h1 class="text-2xl font-semibold">Login</h1>
                </div>
                <div class="divide-y divide-gray-200">
                    <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                        
                        {% if messages %}
                            <ul>
                                {% for message in messages %}
                                    <li>{{ message }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}     
                        
                        <form method="POST" action="{% url 'main:login' %}">
                            {% csrf_token %}
                            <table>
                                <div class="relative">
                                    <tr>
                                        <td class="pr-3 py-4">Username: </td>
                                        <td>
                                            <input type="text" name="username" placeholder="Username" class="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:borer-rose-600 sm:rounded-3xl">
                                        </td>
                                    </tr>
                                </div>
                                
                                <div class="relative">
                                    <tr>
                                        <td class="pr-3 py-4">Password: </td>
                                        <td><input type="password" name="password" placeholder="Password" class="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:borer-rose-600 sm:rounded-3xl"></td>
                                    </tr>
                                </div>
                                <div class="relative">
                                    <tr>
                                        <td class="pb-3"><input class="cursor-pointer bg-blue-500 text-white rounded-md px-2 py-1 font-semibold" type="submit" value="Login"></td>
                                    </tr>
                                </div>
                            
                            </table>
                        </form>
                            
                        <a href="{% url 'main:register' %}" class="bg-blue-500 text-white rounded-md px-2 py-1 font-semibold">Register Account Now</a>
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock content %}
```

2. The register page was customized using the following code for Tailwind CSS along with some additional installations using `django-widget-tweaks` which allowed me to customized and render Django UserCreationForms using `render_field`:

```py
{% extends 'base.html' %}
{% load widget_tweaks %}
{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  
<section class="bg-gray-50 bg-gradient-to-r from-yellow-400 to-blue-500">
    <div class ="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
            Curry Under Armour Inventory
        </a>
        <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">Register</h1>  
                    <form method="POST" class="space-y-4 md:space-y-6" action="{% url 'main:register'%}">  
                        {% csrf_token %}
                        <div>
                            <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Username</label>
                            {% render_field form.username name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Username" required="" %}
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            {% render_field form.password1 name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="" %}
                        </div>
                        <div>
                            <label for="confirm-password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>
                            {% render_field  form.password2 id="confirm-password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""%}
                        </div>
                        <input type="submit" name="submit" value="Create an account" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 cursor-pointer bg-blue-500 text-white rounded-md px-2 py-2 font-semibold text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" />
                        <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                            Already have an account? <a href="{% url 'main:login' %}" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Login here</a>
                        </p>
                    </form>

                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}
            </div>
        </div>
    </div>
</section>

{% endblock content %}
```

3. The add item page was customized using the following code in Tailwind CSS and using `django-widget-tweaks`:

```py
{% extends 'base.html' %} 
{% load widget_tweaks %}
{% block content %}

<section class="bg-gray-50 dark:bg-white-400">
    <div class ="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">Add Product</h1>  
                    <form method="POST" class="space-y-4 md:space-y-6" action="{% url 'main:create_product'%}">  
                        {% csrf_token %}
                        <div>
                            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Product Name</label>
                            {% render_field form.name name="Name" id="Name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Name" required="" %}
                        </div>
                        <div>
                            <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                            {% render_field form.price name="price" id="price" placeholder="Price of Product" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="" %}
                        </div> 
                        <div>
                            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Product Description</label>
                            {% render_field  form.description id="description" placeholder="Product Description" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""%}
                        </div>
                        <div>
                            <label for="amount" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Amount</label>
                            {% render_field  form.amount id="amount" placeholder="Product Amount" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""%}
                        </div>
                        <input type="submit" name="submit" value="Add Product" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 cursor-pointer bg-blue-500 text-white rounded-md px-2 py-2 font-semibold text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" />
                    </form>
            </div>
        </div>
    </div>
</section>

{% endblock %}
```

* __Customize the inventory list page so it becomes more attractive, either by adding colors or using another approach (such as Cards) to show the items, or both.__<br>

I customized the inventory list page using a table to represent the list of items and their descriptions, and moved the add, delete, edit product/item buttons into visually appealing positions (and customized them as well) using Tailwind CSS. Furthermore, I added a navigation bar and customized it as well using Tailwind CSS and placed the logout button on the navigation bar. Following this, I also created an about page for the website that is placed on the navigation bar.

1. Customizing inventory list page on `main.html`:

```py

{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html'%}
    
    <h1 class="text-3xl font-bold text-center py-4 bg-slate-400">Curry Under Armour Inventory</h1>
    <hr>
    <div class="dark:bg-gray-200">
        <p class="font-bold pt-4 px-2">You have saved <u>{{ item_count }} Curry Brand items</u> in this application</p><br>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">Name</th>
                        <th scope="col" class="px-6 py-3">Price</th>
                        <th scope="col" class="px-6 py-3">Amount</th>
                        <th scope="col" class="px-6 py-3">Description</th>
                        <th scope="col" class="px-6 py-3">Date Added</th>
                        <th scope="col" class="px-6 py-3">Modify Amount</th>
                        <th scope="col" class="px-6 py-3">Modify Product</th>
                    </tr>
                </thead>
                {% for product in products %}
                {% comment %} Below is how to show the product data {% endcomment %}
                <tbody>
                    {% if forloop.last %}
                    <tr class="font-bold dark:bg-teal-400 text-gray-900">
                    {% else %}
                    <tr class="font-bold dark:bg-gray-300 text-gray-900">
                    {% endif %}
                        <td class="px-6 py-4">{{product.name}}</td>
                        <td class="px-6 py-4">{{product.price}}</td>
                        <td class="px-6 py-4">{{product.amount}}</td>
                        <td class="px-6 py-4">{{product.description}}</td>
                        <td class="px-6 py-4">{{product.product_release_date}}</td>
                        <td class="px-6 py-4 font-bold">
                            <a href="{% url 'main:increment_product' product.pk %}" class="pr-6">
                                <button class="cursor-pointer bg-green-500 text-white rounded-md px-2 py-2">
                                    Increase Amount
                                </button>
                            </a>
                            <a href="{% url 'main:decrement_product' product.pk %}">
                                <button class="cursor-pointer bg-red-500 text-white rounded-md px-2 py-2">
                                    Decrease Amount
                                </button>
                            </a>
                        </td>
                        <td class="px-6 py-4">
                            <a href="{% url 'main:edit_product' product.pk %}" class="pr-6">
                                <button class="cursor-pointer bg-blue-500 text-white rounded-md px-2 py-2">
                                    Edit
                                </button>
                            </a>
                            <a href="{% url 'main:delete_product' product.pk %}" class="pr-6">
                                <button class="cursor-pointer bg-blue-500 text-white rounded-md px-2 py-2">
                                    Delete
                                </button>
                            </a>
                        </td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
        </div>
        <br />
        <div class="pb-5 px-2 relative">
            <a href="{% url 'main:create_product' %}" class="px-3">
                <button class="cursor-pointer bg-yellow-500 text-white rounded-md px-2 py-2 font-semibold">
                    Add New Product
                </button>
            </a>
        </div>
        <div class="pb-5 px-2 relative">
            <h5 class="font-bold">Last login session: {{ last_login }}</h5>
        </div>
    </div>

{% endblock content %}
```

2. Customizing navigation bar by adding `navbar.html` and using Tailwind CSS:

```py
{% extends 'base.html' %}
{% block content %}

<!-- Main navigation container -->
<nav
  class=" font-sans relative flex w-full flex-nowrap items-center justify-between bg-indigo-400 py-2 text-neutral-500 shadow-lg hover:text-neutral-700 focus:text-neutral-700 dark:bg-#3393FF lg:flex-wrap lg:justify-start lg:py-4"
  data-te-navbar-ref>
  <div class="flex w-full flex-wrap items-center justify-between px-3">
    <div class="ml-2">
      <a class="font-semibold text-xl py-1 text-neutral-800 dark:text-neutral-1000" href="{% url 'main:show_main' %}"
        >Curry Under Armour Inventory</a>
    </div>
    <!-- Collapsible navbar container -->
    <div
      class="!visible mt-2 hidden flex-grow basis-[100%] items-center lg:mt-0 lg:!flex lg:basis-auto"
      id="navbarSupportedContent3"
      data-te-collapse-item>
      <!-- Left links -->
      <ul
        class="list-style-none mr-auto flex flex-col lg:mt-1 lg:flex-row px-5">
        <!-- Features link -->
        <li
          class="ml-2 pl-2 lg:mb-0 lg:pl-0 lg:pr-2"
          data-te-nav-item-ref>
          <h1 class="text-xl dark:text-neutral-200 font-semibold pr-10">Welcome! {{name}}</h1>
        </li>
      </ul>
      <button class="text-xl py-1 font-semibold p-0 text-neutral-500 transition duration-200 hover:text-neutral-700 hover:ease-in-out focus:text-neutral-700 disabled:text-black/30 motion-reduce:transition-none dark:text-neutral-200 dark:hover:text-neutral-400 dark:focus:text-neutral-400 lg:px-2 [&.active]:text-black/90 dark:[&.active]:text-neutral-400">
        <a href="{% url 'main:about' %}">About</a>
      </button>
      <button class="text-xl py-1 font-semibold p-0 text-neutral-500 transition duration-200 hover:text-neutral-700 hover:ease-in-out focus:text-neutral-700 disabled:text-black/30 motion-reduce:transition-none dark:text-neutral-200 dark:hover:text-neutral-400 dark:focus:text-neutral-400 lg:px-2 [&.active]:text-black/90 dark:[&.active]:text-neutral-400">
        <a href="{% url 'main:logout' %}">Logout</a>
      </button>
    </div>
  </div>
</nav>

{% endblock content %}
```

3. Creating About page called `about.html` and adding a URL Path to `urls.py`

```py

{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html'%}

<body class="font-sans dark:bg-gray-200">
    <h1 class="text-3xl font-bold text-center py-4 bg-slate-400">Curry Under Armour Inventory</h1>
    <hr>
    <h5 class="font-bold">Application Name:</h5>

    <p class="py-4">{{ appName }}</p>

    <h5 class="font-bold">Name:</h5>
    <p class="py-4">{{ name }}</p>

    <h5 class="font-bold">Class:</h5>
    <p class="py-4">{{ class }}</p>

    <h5 class="font-bold">Description:</h5>
    <p class="py-4">{{ description }}</p>

    <h5 class="font-bold">Release Date:</h5>
    <p class="py-4">{{ release_date }}</p>
</body>

{% endblock content %}

```






