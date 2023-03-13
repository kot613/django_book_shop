# e_shop_book Project #
This project is not intended for commercial use.
The project was implemented with the help of Django
## Prerequisites ##

- python >= 3.10
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
python -m venv venv
venv/bin/activate
venv\Scripts\activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirements.txt
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000

***
The BookStore has got 3 apps, the different apps and their purpose are described here:

### Ebook app
Responsible for the implementation of book data.
#### Author
The Author model contains information about the author, such as the author's name, description, profile picture.

+ name: CharField
+ description: TextField
+ image: ImageField
+ slug = SlugField

#### Publication
The Publication model contains information about the publication house.

+ name: CharField
+ slug = SlugField

#### Genre
The Genre model contains information about the book genre.

+ name: CharField
+ slug = SlugField

#### Book
The Book model contains information about the book, such as the title, author, publication, description, profile picture.

+ name = CharField
+ author = ForeignKey(Author)
+ publication = ForeignKey(Publication)
+ genres = ManyToManyField(Genre)
+ year = PositiveSmallIntegerField
+ num_page = PositiveSmallIntegerField
+ format = CharField
+ isbn = CharField
+ language = CharField
+ image = ImageField
+ price = PositiveSmallIntegerField
+ slug = SlugField
+ availability = BooleanField
+ annotation =TextField
+ description = TextField
+ created = DateTimeField(auto_now_add=True)

#### Comment
The Comment model contains information about the comment.

+ name: ForeignKey(User)
+ message: TextField
+ create_at: DateTimeField
+ post = ForeignKey(Book)

#### Controllers
+ Book_list - 
The controller responsible for views the list of books.
+ Book_detail - 
Controller responsible for reviewing the book.
+ Author_detail - 
Controller responsible for reviewing the autor.
+ Create_comment - 
Controller responsible for generating reviews.
+ Search_results - 
The controller responsible for the search form.
The search is based on the title of the book, its description and the year of publication.
The search is also performed by the author of the book or his biography.
+ AboutView - 
The controller responsible for displaying the "about" page
+ PaymentView - 
The controller responsible for displaying the "payment" page
+ DeliveryView - 
The controller responsible for displaying the "delivery" page

### Newsletter app
Newsletter subscription app.

#### Newsletter
The Newsletter model contains information about the subscriber.

+ email: EmailField
+ date: DateTimeField(auto_now_add=True)
+ active: BooleanField(default=True)

#### Controllers

+ CreateNewsletter - 
The controller responsible for the create newsletter form.
***
### Basket app
App is responsible for the user's shopping cart

#### Order
The Order model contains information about the order, such as the first and last name, phone and email user, address delivery. It also contains data on the cost of the order and whether it has been paid.

+ last_name: CharField
+ first_name: CharField
+ phone: CharField
+ email = EmailField
+ city = CharField
+ address = CharField
+ order = CharField
+ price = IntegerField
+ payment = BooleanField
+ user_id = CharField

#### Controllers

+ basket_add, basket_remove, basket_detail, checkout - 
The controller responsible for operations with the user's shopping cart.
***
### Users app
App is responsible for register, logging in and logging out of the user.



