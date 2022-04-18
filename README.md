# pythonApiDevelopment

course python api development

# course

link of the course [Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA)

## setting virtual environment

1. on cmd digit : `py -3 -m venv venv`

2. on visual studio code go on:

   1. view
   2. command pallette
   3. search for _Python: select Interpreter_
   4. select the path of _python.exe_ inside the folder _venv/scrips_

3. set the terminal (cmd/bash) for using the virtual environment

   1. in cmd digit: `venv\Scripts\activate.bat`

   2. on bash digit `source venv/Scripts/activate`

   3. check on terminal that now is visibile `venv`

## fastapi

1. go to site [fastapi](https://fastapi.tiangolo.com/tutorial/) and follow the istruction to setting the project
2. for running the project digit:
   `uvicorn app.main:app --reload`

# POSTGRESS

## SQL COMMANDS

| ACTION | SQL COMMAND                                                |
| ------ | ---------------------------------------------------------- |
| INSERT | `INSERT INTO products (name, price) VALUES ('bike', 200);` |
| DELETE | `DELETE FROM products WHERE id = 22;`                      |
| UPDATE | `UPDATE products SET name = 'car' WHERE id = 11;`          |

## POSTGRESS DRIVER

We use [Psycopg 3](https://www.psycopg.org/psycopg3/docs/) as a driver for postgress.
To install the driver on bash digit `pip install psycopg[binary]`
