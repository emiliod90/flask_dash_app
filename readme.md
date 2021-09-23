# Flask + Dash Application

See this for style: https://github.com/jimmybow/Flask_template_auth_with_Dash

Inspired by https://hackersandslackers.com/plotly-dash-with-flask/
https://mattupstate.com/blog/how-i-structure-my-flask-applications/ 

## Poetry for Package Management

Any Python file is a module, its name being the file's base 
name/module's __name__ property without the .py extension. 
A package is a collection of Python modules, i.e., a package 
is a directory of Python modules containing an additional __init__.py file. 
The __init__.py distinguishes a package from a directory that just happens 
to contain a bunch of Python scripts. Packages can be nested to any depth, 
provided that the corresponding directories contain their own __init__.py file.

### Install Poetry
conda install -c conda-forge poetry

### Create package or create a pyproject.toml interactively
### see Poetry CLI https://python-poetry.org/docs/cli/
poetry new [package-name]
poetry new devdashapp
Or run poetry init


DONT USE DASH IN FILE NAMES for py modules

### install first round
poetry install

### Manage dependencies using the Poetry cli
### Use poetry add, poetry remove
poetry add flask
poetry add dash
poetry add requests

Alternatively run poetry install after adding the dependencies into the pyproject.toml file

### Update dependencies with
poetry update
poetry self:update

## Flask development

### Organise Flask Application Factory layout
### include route for Dash application

/app
├── /application
│   ├── __init__.py
│   ├── auth.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── /static
│   │   ├── /dist
│   │   └── /src
│   └── /templates
├── config.py
├── start.sh
└── wsgi.py

The entirety of our app lives in the /application folder, with the creation of our app happening in __init__.py. The init file is where we actually create what's called the Application Factory.

### create a flask app object within __init__.py
The initialization of our app happens within the init_app() function following the Flask Application Factory pattern.
### create an entry point to start app within wsgi.py

### Add config.py
Create Config Class to model the environment variables
FLASK_APP = environ.get("FLASK_APP")
FLASK_ENV = environ.get("FLASK_ENV")

### add .env file to house environment variables 
FLASK_APP=wsgi.py
FLASK_ENV=development

### embed the Dash app within the app __init__.py
Import Dash application using
from .plotlydash.dashboard import init_dashboard
app = init_dashboard(app)
### create the dash app within plotlydash/dashboard1.py 
importing a file called dashboard.py from a directory in our Flask app called /plotlydash. Inside dashboard.py is a single function which contains the entirety of a Plotly Dash app in itself:

We pass our top-level Flask app into Dash as server, hence dash_app = Dash(server=server). This effectively spins up a Dash instance using our Flask app at its core, as opposed to its own!

Note Dash has full control over anything we build beneath the hierarchy of our prefix

## Notice for Dash App structure
Because we create our own app i.e. app = Flask we cannot use the same structure used by the official Dash documentatiom i.e. app = dash.Dash 

## Running in Development
### run script
poetry run [script-name] executes a script defined in  the [tool.poetry.scripts] section of pyproject.toml.
### to run app via gunicorn
gunicorn --bind=0.0.0.0:5000 --timeout 600 wsgi:app
or
poetry run python wsgi.py

### uvicorn
$ poetry run uvicorn main:app --reload --host 0.0.0.0 --port 3000

See Uvicorn settings https://www.uvicorn.org/settings/
See Gunicorn settings - https://docs.gunicorn.org/en/develop/configure.html 

# Building and Publishing for package
poetry build: Builds the source and wheels archives.
poetry publish: Publishes the output of the previous build to the project's external repository (likely PyPi).


# Prepping for Deployment to Azure
### add requirements in root
Add a requirements.txt file in the root of your project that specifies your direct dependencies. App Service then installs those dependencies automatically when you deploy your project.
The requirements.txt file must be in the project root for dependencies to be installed. Otherwise, the build process reports the error: "Could not find setup.py or requirements.txt; Not running pip install." If you encounter this error, check the location of your requirements file.

App Service automatically defines an environment variable named WEBSITE_HOSTNAME with the web app's URL, such as msdocs-hello-world.azurewebsites.net. It also defines WEBSITE_SITE_NAME with the name of your app, such as msdocs-hello-world.

### Export a requirements.txt file
poetry export -f requirements.txt --output requirements.txt --without-hashes

### Update environment variables on Azure

# Azure Production
For Flask, App Service looks for a file named application.py or app.py and starts Gunicorn as follows:
### If application.py
gunicorn --bind=0.0.0.0 --timeout 600 application:app
### If app.py
gunicorn --bind=0.0.0.0 --timeout 600 app:app

### Customise start up command using .sh file
gunicorn --bind=0.0.0.0:5000 --timeout 600 wsgi:app

Add this to Azure startup.sh file and run the Azure CLI command or add it via Configuration settings in https://docs.microsoft.com/en-gb/azure/app-service/configure-common#configure-general-settings 

### add startup.sh to App service via CLI
az webapp config set --resource-group <resource-group-name> --name <app-name> --startup-file "<custom-command>"
az webapp config set --resource-group PortfolioApp --name devdashapp --startup-file startup.sh

# Setup Git repo for multiple push from local
### First one 
git remote add origin https://github.com/emiliod90/flask_dash_app.git
git remote set-url --add --push origin https://github.com/emiliod90/flask_dash_app.git
### Second one
git remote set-url --add --push origin https://emydesouza@dev.azure.com/emydesouza/Flask%20Dash%20App/_git/Flask%20Dash%20App

git branch -M main
git push -u origin main

