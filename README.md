# excel-student-parser
Higher abstraction of operating on excel files, based on openpyxl.  
Ultimate goal is to allow simple implementation of "first come, first served" group assignments, with collision detection.

## Installation guide
Firstly clone the repo `git clone https://github.com/jkbSeven/excel-student-parser.git` and go inside it `cd excel-student-parser`

Now create python virtual env and source it:
- on Windows: `python3 -m venv .venv` and then `.venv\Scripts\activate`
- on Linux: `python3 -m venv .venv` and then `source .venv/bin/activate`

Get all required packages with `pip3 install -r requirements.txt`

## How to use
Firstly create a json file with all the subjects that students will be assinged to with `python3 xlparser/scripts/subjectsGenerator.py`  
If you're finished with creating subjects, then you are ready to move on to executing main script with `python3 excelparser.py`

## How to modify excelparser.py
### Explanations of all scripts and their functions can be found on the [wiki](https://github.com/jkbSeven/excel-student-parser/wiki)
Functions are pretty straight forward, the only thing you need to change are the strings.  
For example change `.findValue("Imię i nazwisko")` to `.findValue("FirstName and LastName")`
