# python-poetry

## Start 

```
kaunjovi@devbook code % git clone git@github.com:kaunjovi/python-poetry.git
Cloning into 'python-poetry'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
kaunjovi@devbook code % cd python-poetry 
kaunjovi@devbook python-poetry % codium . 
kaunjovi@devbook python-poetry %
```

## Opening status 

```
kaunjovi@devbook python-poetry % python --version 
Python 3.10.2
kaunjovi@devbook python-poetry % pip --version 
pip 23.3.2 from /Users/kaunjovi/.pyenv/versions/3.10.2/lib/python3.10/site-packages/pip (python 3.10)
kaunjovi@devbook python-poetry % pipx --version 
1.3.3
```

## Install poetry

```
kaunjovi@devbook python-poetry % pip install poetry
...
kaunjovi@devbook python-poetry % poetry --version 
Poetry (version 1.7.1)
```    


The word “poetry” itself comes from the Greek word poieo meaning “I create,”

poetry --version

Start a new Python Project. poetry new [package-name] poetry new phone-number-validator

TOML files (What are TOML format??)

Which Python is poetry using? Poetry by default just uses the system Python, even if that is not supported by the version specifier in pyproject. toml. Oops. Check this out propoerly.

Which python to use poetry env use /full/path/to/python poetry env use /usr/local/bin/python3.11

The virtualenv will be created inside the project path and vscode will recognize. poetry config virtualenvs.in-project true

Shows the name of the current environment poetry env list

remove poetry env

will create a new environment using your updated configuration Install the packages inside the pyproject.toml file. poetry install

Create a pyproject.toml file interactively. poetry init

Adding dependencies poetry add pendulum poetry add pendulum coo

Adding Dev dependencies poetry add -D flake8 mypy

Add dependencies that are not available for prime time yet. There are no stable versions yet.

poetry add -D black --allow-prereleases

Update the dependencies once in a while To ensure you are not working with an old version poetry update

Removing dependencies poetry remove coo poetry remove -D mypy

CHECK THE STATE OF YOUR DEPENDENCIES poetry show --tree poetry show --latest

Easily build and package your projects with a single command. Supports source distribution and wheels. (wheels ??) poetry build

Make your work known by publishing it to PyPI. poetry publish

Update poetry to the latest stable version. poetry self:update

Integrate with vscode $ poetry shell $ code . and follow https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2 https://marketplace.visualstudio.com/items?itemName=zeshuaro.vscode-python-poetry

virtual environment If not set explicitly, poetry by default will create a virtual environment under {cache-dir}/virtualenvs or use the {project-dir}/. venv directory if one already exists. If set to true , the virtualenv will be created and expected in a folder named . venv within the root directory of the project.

The poetry.lock file The file poetry.lock serves as a record of all the exact versions of the dependencies used in a project during installation, removal, or updating of any dependency. It ensures that your project uses the correct versions of dependencies by listing all the packages, their exact versions, and the hashes of their source files. It's important to commit the poetry.lock file to your version control

## Resources
- https://python-poetry.org/
- https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1
- https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2
- https://www.freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry/
