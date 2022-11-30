# e_shop_book Django Project #
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
