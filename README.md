HW 3: This project runs a server that adds Cherry to Basket_a and displays unique fruits in basket_a and basket_b

## Quick Start
### Local Test Setup

First, open main.py and change the username and password to the apporiate user

install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

###uses

To add Cherry to basket_a navigate to 
'''
localhost:5000/api/update_basket_a
'''

to display unique fruits in basket_a and basket_b navigate to
'''
localhost:5000/api/unique
'''
