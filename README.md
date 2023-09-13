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





