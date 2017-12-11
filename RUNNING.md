# Running

This file will contain info regarding the process of getting this up and
running.

You will need `python` 2.7.x and `pip`. 

Run `pip install virtualenv --user`. In this repo, you can now run `virtualenv
env && source env/bin/activate`. Then run `pip install -r requirements.txt` to
pull in the python packages that we require.

To run the webserver for the frontend, run `FLASK_APP=hello.py flash run`.
