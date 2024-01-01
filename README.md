# python-poetry

# Setup 

## Setup for ML 

- Install pandas and scikit-lear 

```
kaunjovi@devbook python-poetry % poetry add pandas
...
kaunjovi@devbook python-poetry % poetry add scikit-learn
...
```

- This should give you the following entries in the pyproject.toml 

```
[tool.poetry.dependencies]
python = "3.12.1"
pandas = "^2.1.4"
scikit-learn = "^1.3.2"
```



# Python functions 

- [Python Functions, lambda, filter, map, reduce](https://pynative.com/python-functions/)


## Install poetry

- https://python-poetry.org/docs/

```
kaunjovi@devbook python-poetry % pip install poetry

kaunjovi@devbook python-poetry % poetry --version 
Poetry (version 1.7.1)
```    

## Get started with the project 

- Install the latest python. 3.12.1 at the moment. 
- Where is python installed on mac. 

```
kaunjovi@devbook python-poetry % where python3
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
/usr/local/bin/python3
/usr/bin/python3
```

- Configure Poetry to use the local Python of choice. 

```
kaunjovi@devbook python-poetry % poetry env use /usr/local/bin/python3
```

- Configure Poetry to use the local directory for .venv
- Where does this setting stay ? 
- Which file ? 

```
kaunjovi@devbook python-poetry % poetry config virtualenvs.in-project true

```

- Create pyproject.toml file 

```
kaunjovi@devbook python-poetry % poetry init
```




- The word “poetry” itself comes from the Greek word poieo meaning “I create,”

poetry --version

Start a new Python Project. 
TOML files (What are TOML format??)
poetry new [package-name] poetry new phone-number-validator


Which Python is poetry using? 
Poetry by default just uses the system Python, even if that is not supported by the version specifier in pyproject. toml. 
Oops. Check this out propoerly.



The virtualenv will be created inside the project path and vscode will recognize. 
poetry config virtualenvs.in-project true

- Name of the current environment

```
kaunjovi@devbook python-poetry % poetry env list
.venv (Activated)
```

remove poetry env

will create a new environment using your updated configuration Install the packages inside the pyproject.toml file. poetry install

Create a pyproject.toml file interactively. poetry init

Adding dependencies 
poetry add pendulum poetry 
add pendulum coo

Adding Dev dependencies 
poetry add -D flake8 mypy

Add dependencies that are not available for prime time yet. There are no stable versions yet.
poetry add -D black --allow-prereleases

Update the dependencies once in a while To ensure you are not working with an old version 
poetry update

Removing dependencies 
poetry remove coo 
poetry remove -D mypy

CHECK THE STATE OF YOUR DEPENDENCIES 
poetry show --tree 
poetry show --latest

Easily build and package your projects with a single command. Supports source distribution and wheels. (wheels ??) poetry build

Make your work known by publishing it to PyPI. 
poetry publish

Update poetry to the latest stable version. 
poetry self:update

Integrate with vscode $ poetry shell $ code . 
and follow https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2 
https://marketplace.visualstudio.com/items?itemName=zeshuaro.vscode-python-poetry

virtual environment If not set explicitly, poetry by default will create a virtual environment under {cache-dir}/virtualenvs or use the {project-dir}/. venv directory if one already exists. If set to true , the virtualenv will be created and expected in a folder named . venv within the root directory of the project.

The poetry.lock file The file poetry.lock serves as a record of all the exact versions of the dependencies used in a project during installation, removal, or updating of any dependency. It ensures that your project uses the correct versions of dependencies by listing all the packages, their exact versions, and the hashes of their source files. It's important to commit the poetry.lock file to your version control

