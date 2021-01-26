## Poetry for Package Management

Any Python file is a module, its name being the file's base 
name/module's __name__ property without the .py extension. 
A package is a collection of Python modules, i.e., a package 
is a directory of Python modules containing an additional __init__.py file. 
The __init__.py distinguishes a package from a directory that just happens 
to contain a bunch of Python scripts. Packages can be nested to any depth, 
provided that the corresponding directories contain their own __init__.py file.

# Install Poetry
conda install -c conda-forge poetry

# Create package or create a pyproject.toml interactively
# see Poetry CLI https://python-poetry.org/docs/cli/
poetry new [package-name]
poetry new devdashapp
Or run poetry init

# install first round
poetry install

# Organise Flask Application Factory layout

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

# Manage dependencies using the Poetry cli
# Use poetry add, poetry remove
poetry add flask
poetry add dash

Alternatively run poetry install after adding the dependencies into the pyproject.toml file

# update dependencies with
poetry update
poetry self:update

# Flask development

# create a flask app object
# Add config.py
# add .env
# update environment variables on Azure
# 


# Development
# run script
poetry run [script-name] executes a script defined in  the [tool.poetry.scripts] section of pyproject.toml.
# to run app gunicorn
gunicorn --bind=0.0.0.0:5000 --timeout 600 wsgi:app
or
poetry run python wsgi.py

# uvicorn
$ poetry run uvicorn main:app --reload --host 0.0.0.0 --port 3000

# See Uvicorn settings https://www.uvicorn.org/settings/
# See Gunicorn settings - https://docs.gunicorn.org/en/develop/configure.html 

# add requirements in root
Add a requirements.txt file in the root of your project that specifies your direct dependencies. App Service then installs those dependencies automatically when you deploy your project.
The requirements.txt file must be in the project root for dependencies to be installed. Otherwise, the build process reports the error: "Could not find setup.py or requirements.txt; Not running pip install." If you encounter this error, check the location of your requirements file.

App Service automatically defines an environment variable named WEBSITE_HOSTNAME with the web app's URL, such as msdocs-hello-world.azurewebsites.net. It also defines WEBSITE_SITE_NAME with the name of your app, such as msdocs-hello-world.

# Export a requirements.txt file
poetry export -f requirements.txt > requirements.txt


# Building and Publishing
poetry build: Builds the source and wheels archives.
poetry publish: Publishes the output of the previous build to the project's external repository (likely PyPi).


# Production
For Flask, App Service looks for a file named application.py or app.py and starts Gunicorn as follows:
# If application.py
gunicorn --bind=0.0.0.0 --timeout 600 application:app

# If app.py
gunicorn --bind=0.0.0.0 --timeout 600 app:app

# Customise Flask main module
# customise start up command
gunicorn --bind=0.0.0.0:5000 --timeout 600 wsgi:app

Add this to Azure startup.sh file and run the Azure CLI command or add it via Configuration settings in https://docs.microsoft.com/en-gb/azure/app-service/configure-common#configure-general-settings 

# add startup.sh to App service via CLI
az webapp config set --resource-group <resource-group-name> --name <app-name> --startup-file "<custom-command>"
az webapp config set --resource-group PortfolioApp --name devdashapp --startup-file startup.sh

# add multiple 
git remote add origin https://github.com/emiliod90/flask_dash_app.git
git remote set-url --add --push origin https://github.com/emiliod90/flask_dash_app.git

<!-- git remote add origin https://emydesouza@dev.azure.com/emydesouza/Flask%20Dash%20App/_git/Flask%20Dash%20App -->
git remote set-url --add --push origin https://emydesouza@dev.azure.com/emydesouza/Flask%20Dash%20App/_git/Flask%20Dash%20App

git branch -M main
git push -u origin main
