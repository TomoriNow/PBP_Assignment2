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
```def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")```

<b> Function showing JSON view </b>
```def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")```
    
<b> Function showing XML view by ID </b>
```def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")```

<b> Function showing JSON view by ID </b>
```def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")```

For the `show_xml` and `show_json` functions, they both accept `request` parameters stores a variable `data = Item.objects.all()` to store all fetched `Item` objects, and returns the previously fetched data as `XML` and `JSON` formats respectively as an  `HttpResponse`.

For the `show_xml_by_id` and `show_json_by_id` functions, they both accept `request` and `id` parameters. They also use `data = Item.objects.filter(pk=id)` to query the result of data given a specific `id` and returns an `HttpResponse` containing the serialized data in `XML` and `JSON` formats respectively. 













