# Dawson Coffee \'n Code

Welcome to a starter project for the Dawson Coffee 'n Code club

## Setup

 ### Install python, git, and virtualenv

  - Our programming language:
      - https://www.python.org/downloads/
      - ships with our package manager/installer (no need to douwload)
        https://pypi.org/project/pip/

  - Our Version Control Tool
      https://git-scm.com/

  - Our tool for isolated environments
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
