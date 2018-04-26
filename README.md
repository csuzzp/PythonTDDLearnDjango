#Learn Python django with TDD method

THE STARTUP PROCCESS IS AS FOLLOWS:

First install Python3.6

Then Install django: 

```$ pip install django```

Install Selenium:

```$ pip install selenium```

Downlode GeckoDriver.exe from :http://www.seleniumhq.org/download/  [use firefox, u can use other depends on u explore]

Copy GeckoDriver.exe to Python Path  or add the path of GeckoDriver.exe to enviroment PATH value.

----------------------------Using demo-----------------------------
function_tests.py

----Run it 

```$ python function_tests.py````

will open firefox explore, told fail message.

Build django project

```$ django-admin.py startproject superlists```

It will create a directory named spuerlists and some subdirectory

like this 

.
├─ functional_tests.py

└─ superlists

    ├─ manage.py

    └─ superlists

        ├─ __init__.py

        ├─ settings.py

        ├─ urls.py

        └─ wsgi.py


go to superlists directory

cd superlists

Run manager.py

$ python3 manage.py runserver

Validating models...

0 errors found

Django version 1.7, using settings 'superlists.settings'

Development server is running at http://127.0.0.1:8000/

Quit the server with CONTROL-C.

open another cmd.exe and run function_tests.py it will success. 
