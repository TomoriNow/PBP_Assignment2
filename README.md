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

urlpatterns = [
    ...
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'), 
    ...
]


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

# PBP_Inventory | Assignment 6

## Explain the difference between asynchronous programming and synchronous programming.
Asychnronous programming is a method of programming that utilizes non-blocking architechture so that the execution of a task does not depend on a another task in the program. This means that tasks can run simultaneously. Asynchronous programming has characterisitcs such as multi-thread (which means operations or programs can run in parallel), non-blocking (which means it has the ability to send multiple requests to a server), and also has the ability to increase the throughput of the program since it has multiple (parallel) operations that run at the same time. For example, in a client-server architechture asynchronus program can make a request to the server and continue working while waiting a response from the server which is more efficient.

Conversely, Synchronous programming utilizes blocking architechture so that the execution of a task in the program is dependent on completing the one before it. Each task needs an answer or appropriate response before moving on to the next task. Synchronous programming has characteristics such as single-thread (only one operation or program can run at a time), blocking (which means it will only send the server one request at a time and wait for the server's response to the request before moving on to another task), and also has the characteristic of being more methodical and slow.

## In the implementation of JavaScript and AJAX, there is an implemented paradigm called the event-driven programming paradigm. Explain what this paradigm means and give one example of its implementation in this assignment.

The event-driven programming paradigm is based on the idea that a program could be implemented to be "event-driven", meaning that the program is designed to respond to user actions/events (either through their hardware or software) such as user interactions (mouse button clicks/movement/scrolling, keyboard pressses, etc) and system events (timers, file input/output, network communication/events, etc). Thus, the flow of a program is determined by events that occur during its execution by waiting for specific events to occur and then triggering corresponding event handlers or callbakcs to respond to those events. 

One example of its implementation in this assignment is through the JavaScript code (and AJAX implementation) placed in the body of the `main.html` page between the `<script></script>` tags. For instance, the `async` function called `getProducts` utilizes the `fetch()` API (which provides an interface to fetch resources including across network) to get the JSON data asynchronously from the web application in the event that the user clicks the `Add Product` button in the `Add Product by Ajax` user interface. Then, the `refreshProducts` function will wait for the event/result from `getProducts` async function and update the table according to the product that the user added which can be seen from `const products = await getProducts()`.

## Explain the implementation of asynchronous programming in AJAX.

The implementation of asynchronous programming in AJAX utilizes a particular way of using JavaScript in order to apply asynchronous programming. AJAX usually downloads the data from a server in the background (or sending data to the server in the background) and allows dynamically updating a page (and updating the data on the page asynchronously) without making the user wait or have to refresh/reload the web page multiple times every time a change is made to the page. AJAX essentially avoids the "click-wait-refresh" pattern. This is because AJAX could use XML, text, or JSON to send the data to the server. Methodically speaking, when an event occurs on the web page, an `XMLHttpRequest` object is created by JavaScript which then sends a request to the server. The server then processes the request and returns an appropriate response to the web page and is read via JavaScript. Following this, JavaScript will trigger actions based on the response read such as updating (Inserting or Deleting or Editing) the data on the web page.


## In this semester, the implementation of AJAX is done using the Fetch API rather than the jQuery library. Compare the two technologies and write down your opinion which technology is better to use.


The Fetch API and jQuery are both tools used for making asynchronous requests in web development, but they differ significantly in terms of their technical approach and capabilities.

The Fetch API is a modern JavaScript API which provides a standardized way to make HTTP requests. It offers a more flexible and promise-based approach (making requests with a `Promise`) for handling asynchronous operations and fetching resources (including across network). With the Fetch API, you can make requests to servers and handle responses using `Promises`, allowing for cleaner and more concise code. It supports various data formats, not just XML, and is versatile for working with JSON, text, or other data types. Additionally, the Fetch API is lightweight and does not require any additional libraries or dependencies, making it a great choice for developing a web application.

On the other hand, jQuery is a popular JavaScript library that has been used extensively for AJAX requests in the past. It provides a simplified and cross-browser-compatible way to perform AJAX operations. jQuery abstracts many of the complexities of handling different browsers and provides a consistent API for making AJAX calls. However, jQuery is a larger library and includes many other features beyond AJAX, which may lead to unnecessary overhead if you are only using it to process AJAX requests. It also relies on callback functions, which can make the code less readable and harder to maintain compared to the Promise-based approach of the Fetch API.

In my opinion, If you're building a modern web application and want a lightweight and flexible solution with minimum overhead and dependencies, the Fetch API is the better choice compared to jQuery. However, if you're maintaining a legacy project (such as a website that has been running for a very long time) or need to ensure compatibility with older browsers, jQuery's simplicity and cross-browser support may still be the appropriate choice.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

* __AJAX GET.__<br>

To start implementing AJAX GET into the inventory, I had to set up the `get_product_json` function in order to return JSON data for each product item in the data table. This was done in `views.py` and the following function:

```py
def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
```

This function accepts an HTTPrequest as its parameter and filters every product according to the specific user currently logged in using `product_item = Item.objects.filter(user=request.user)` and then returns JSON data.

Along with this function I also implemented a `add_product_ajax` function in `views.py` after importing `from django.views.decorators.csrf import csrf_exempt` and the `@csrf_exempt` decorator such as the following:

```py
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, price=price, description=description, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

This function also accpets an HTTPrequest from the web browser and checks if it uses the `POST` method. If the condition is satisfied, it will get the fields `name`, `price`, `amount`, `description` from the request (according to the specified data in `models.py` and the web browser) using the AJAX `.get()` method and returns a `new_product` which is an instance of the `Item` object with the corresponding fields/attributes and request values. This will then return an `HttpResponse` and a `HttpResponseNotFound` otherwise.

Both of these functions are then routed for their URL path in the `urlpatterns` list in `urls.py`:

```py

from main.views import get_product_json, add_product_ajax

urlpatterns = [
    ...
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    ...
]


```

* __AJAX POST.__<br>

To create a button that opens a modal with a form for adding an item, I first implemented the code for the table structure in `main.html` (and modified it according to the design in Assignment 5 using Tailwind CSS):

```py
<div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                <table id="product_table" class="w-full text-sm text-left text-gray-500 dark:text-gray-400"></table>
</div>
```

Afterwards, I created a `<script>` tag block at the end of the file in order to use AJAX POST and asynchronous programming. The first function made was the `getProducts()` function that uses the `fetch()` API to return the products in JSON format from the data table in the web application:

```py
async function getProducts() {
    return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
``` 

Then, I made another function called `refreshProducts()` that is used to refresh product data in the data table asynchronously. I also modified the function so that it utilizes Tailwind CSS for its design accordingly inside the `htmlString`, and also added the `amount` field so for the data table. Note that every last item in the data table was also made into a different color from the previous items using an `if` condition (by getting the last index of the `products` array):

```py
async function refreshProducts() {
            document.getElementById("product_table").innerHTML = ""
            const products = await getProducts()
            let htmlString = `
            <thead class="text-xs text-left text-sm text-gray-700 w-full uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-6 py-3">Name</th>
                    <th scope="col" class="px-6 py-3">Price</th>
                    <th scope="col" class="px-6 py-3">Amount</th>
                    <th scope="col" class="px-6 py-3">Description</th>
                    <th scope="col" class="px-6 py-3">Date Added</th>
                    <th scope="col" class="px-6 py-3">Modify Product</th>
                </tr>
            </thead>`
            
            products.forEach((item, index) => {
                if (index == products.length-1) {
                    htmlString += `\n
                    <tbody>
                            <tr class="font-bold dark:bg-yellow-300 text-gray-900">
                            <td class="px-6 py-4">${item.fields.name}</td>
                            <td class="px-6 py-4">${item.fields.price}</td>
                            <td class="px-6 py-4">${item.fields.amount}</td>
                            <td class="px-6 py-4">${item.fields.description}</td>
                            <td class="px-6 py-4">${item.fields.product_release_date}</td>
                            <td class="px-6 py-4">
                                <button class="cursor-pointer bg-red-500 text-white rounded-md px-2 py-2" onclick="deleteProduct(${item.pk})">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    </tbody>`
                } else {
                    htmlString += `\n
                    <tbody>
                            <tr class="font-bold dark:bg-gray-300 text-gray-900">
                            <td class="px-6 py-4">${item.fields.name}</td>
                            <td class="px-6 py-4">${item.fields.price}</td>
                            <td class="px-6 py-4">${item.fields.amount}</td>
                            <td class="px-6 py-4">${item.fields.description}</td>
                            <td class="px-6 py-4">${item.fields.product_release_date}</td>
                            <td class="px-6 py-4">
                                <button class="cursor-pointer bg-red-500 text-white rounded-md px-2 py-2" onclick="deleteProduct(${item.pk})">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    </tbody>`
                } 
                 
                        })
            
            document.getElementById("product_table").innerHTML = htmlString
        }
    
        refreshProducts()
```


Following this I contiued to create the Modal form to add the products that is customized by Tailwind CSS which was different from when we had to use Bootstrap for the previous modal form that was in the tutorial:

```py
<div class="relative flex min-h-screen flex-col pl-7 py-7 overflow-hidden dark:bg-gray-200">
        
        <!--modal trigger-->
        <div>
            <label for="tw-modal" class="curosr-pointer rounded bg-black px-4 py-4 text-white active:bg-slate-400">Add Product by Ajax</label>
            <a href="{% url 'main:create_product' %}" class="px-3">
                <button class="cursor-pointer dark:bg-yellow-400 text-white rounded-md ml-5 px-4 py-4 font-semibold">
                    Add New Product
                </button>
            </a>
        </div>
        
        <div class="pb-5 pt-10 relative">
            <h5 class="font-bold">Last login session: {{ last_login }}</h5>
        </div>
        
        <input type="checkbox" id="tw-modal" class="peer fixed appearance-none opacity-0"/>
        
        <!---modal-->
        <label for="tw-modal" class="pointer-events-none invisible fixed inset-0 flex cursor-pointer items-center justify-center overflow-hidden overscroll-contain bg-slate-700/30 opacity-0 transition-all duration-200 ease-in-out peer-checked:pointer-events-auto peer-checked:visible peer-checked:opacity-100 peer-checked:[&>*]:translate-y-0 peer-checked0[&>*]:scale-100">
            <!--modal box-->
            <label class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-blue-400 dark:border-gray-700 h-fit max-w-lg scale-90 overflow-y-auto overscroll-contain shadow-2xl transition" for="">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white pb-5 pt-5 pl-5">Add New Product</h1>
                <form id="form" onsubmit="return false;" class="px-5">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="block mb-2 text-l font-medium text-gray-900 dark:text-white">Name:</label>
                        <input type="text" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="block mb-2 text-l font-medium text-gray-900 dark:text-white">Price:</label>
                        <input type="number" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="price" name="price"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="block mb-2 text-l font-medium text-gray-900 dark:text-white">Description:</label>
                        <textarea class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="description" name="description"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="block mb-2 text-l font-medium text-gray-900 dark:text-white">Amount:</label>
                        <input type="number" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="amount" name="amount"></input>
                    </div>
                </form>
                <div class="mt-7 ml-5 mb-5">
                    <label for="tw-modal" type="button" class="cursor-pointer dark:bg-red-500 text-white rounded-md px-2 py-2 font-semibold transition-all duration-200 ease-in-out peer-checked:pointer-events-auto peer-checked:visible peer-checked:opacity-100 peer-checked:[&>*]:translate-y-0 peer-checked0[&>*]:scale-100">Close</label>
                    <button type="button" class="cursor-pointer dark:bg-green-500 text-white rounded-md ml-3 px-2 py-2 font-semibold" id="button_add" for="tw-modal">Add Product</button>
                </div>
            </label>
    </div>
```

The modal form here is activated by a button `Add Product by Ajax` (that is set in the same div as the `<table>` tag) and when the user clicks on it (this is an event-driven programming paradigm) which opens up the full-customized modal form. Note that the modal form has the fields listed according to the form in `models.py`. When the user clicks `Add Product` after filling out all the fields, the new product will be displayed in the data table in the web page. If no fields are entered/if the fields are incomplete, a new product will not be listed in the data table. Additionally, the modal form will close after adding the product when the user clicks the `Close` button or clicks on an area outside the modal form (which is an overlay made with Tailwind CSS).


To add the products to the main web page it also requires a  new function in the JavaScript tag called `addProduct()`:

```py
function addProduct() {
    fetch("{% url 'main:add_product_ajax' %}", {
    method: "POST",
    body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)
    
    document.getElementById("form").reset()
    return false
}

```

This function uses the `fetch()` API that fethces the add product feature from the url `{% url 'main:add_product_ajax' %}` using the `POST` method in AJAX to create a new FormData taken from the modal form: `new FormData(document.querySelector('#form'))`. This code also wraps the data before sending it to the server, and then the modal form will be reset using `document.getElementById("form").reset()`. The `addProduct()` function is then set as the `onclick` function for the modal's `Add Product` button using `document.getElementById("button_add").onclick = addProduct` inside the `<script>` tag.

Additional to this, I also created a delete feature for the data table in the main web page by creating the `deleteProduct` function inside the `<script>` tag and creating a `delete_product_ajax` in `views.py` which is then routed as a URL path in `urls.py`.

1. In `views.py`:
```py
@csrf_exempt
def delete_product_ajax(request, id):
    product = Item.objects.get(pk=id)
    product.delete()
    return HttpResponse(b"DELETED", status=201)
```

2. In `urls.py`:

```py

from main.views import delete_product_ajax

urlpatterns = [
    ...
    path('delete-product-ajax/<int:id>', delete_product_ajax, name='delete_product_ajax'),
    ...
]

```

3. In `main.html` inside the `<script>` tag:

```py
function deleteProduct(id) {
    fetch("/delete-product-ajax/" + id, {
    method: "POST"
    }).then(refreshProducts)
            
    document.getElementById("form").reset()
    return false
        }
```

Note that the `deleteProduct()` function uses the `fetch()` API and the `POST` method, as well as receives the `id` of each item in the parameter (which is `item.pk` when you call the function). The function is implemented this way (as an attribute) in the `htmlString` for the table inside the `<button>` tag for delete:

```py
onclick="deleteProduct(${item.pk})"
```

Finally, the `collectstatic` command was ran on the terminal using the command `python manage.py collectstatic` which collects all static files from all the applications and places them in a folder called `static` in the root directory of the Django Project. Then, `/static/` was written in the `.gitignore` file so that the static folder could be ignored when deploying the web application.
