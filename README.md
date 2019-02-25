# Dawson Coffee \'n Code

Welcome to a starter project for the Dawson Coffee 'n Code club

## Setup

 ### Install python, git, and virtualenv

  - Our programming language:
      - [Python 3.6](https://www.python.org/downloads/)
      - ships with our package manager/installer (no need to download)
        [pip](https://pypi.org/project/pip/)

  - Our Version Control Tool: [Git](https://git-scm.com/)

  - Our tool for isolated environments: [Virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
    `$pip install virtualenv`

  ### Setup an isolated virtualenv

  #### Mac/Linux

 ```
 $ mkdir coffee_n_code_project
 $ cd coffee_n_code_project
 $ virtualenv -p /usr/bin/python3.6 venv_cnc
 $ source venv_cnc/bin/activate
 (venv_cnc)$ git clone https://github.com/sameerbhatnagar/dawson-coffee-n-code.git
 (venv_cnc)$ cd dawson-coffee_n_code
 (venv_cnc)$ pip install -r requirements.txt
 ```

  #### Windows
   - http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

## Jupyter Notebooks

[Jupyter](https://jupyter.org/) is a python package that enables reproducible research via their *notebooks*.

  ```
  $ jupyter notebook notebooks/Scikit-Learn Demo.ipynb
  ```

This will open a notebook file in the browser, with some code chunks from the Machine Learning library we will be working with, [SciKit Learn](https://scikit-learn.org/stable/index.html)

Simply hit `Shift + Enter` on each code cell, and the code will be executed.
  
