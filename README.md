# excel-student-parser
Higher abstraction of operating on excel files, based on openpyxl.  
Ultimate goal is to allow simple implementation of "first come, first served" group assignments, with collision detection.  

**Explanations of all scripts and their functions can be found on the [wiki](https://github.com/jkbSeven/excel-student-parser/wiki)**

## Installation guide
Firstly clone the repo `git clone https://github.com/jkbSeven/excel-student-parser.git`

Now change directory `cd excel-student-parser`, create python virtual env and source it:
- on Windows: `python3 -m venv .venv` (in some cases `py -m venv .venv`) and then `.venv\Scripts\activate`
- on Linux: `python3 -m venv .venv` and then `source .venv/bin/activate`

Get all required packages with `pip3 install -r requirements.txt`

## How to use
Firstly create a JSON file with all the subjects that students will be assinged to with `python3 xlparser/scripts/subjectsGenerator.py`  
If you're finished with creating subjects, then in `excelparser.py` replace `xlparser/data/WORKBOOK_NAME.xlsx` in ESP() with an actual workbook name.  
You need to check if the excel subject headers match the subject names you provided to the JSON file.  
Afterwards you are ready to move on to executing main script with `python3 excelparser.py`

## How to modify
Some functions in excelparser.py and student.py are based on the template below:
![excel template](https://github.com/jkbSeven/excel-student-parser/assets/107893402/5abd11e9-e3d1-4c87-9731-1bff73e7a749)
Everything before "Imię i nazwisko" gets deleted.

#### If you use different template:  

These are the things you need to change in `excelparser.py`, so the script works properly for you:
1. the strings according to your workbook, for example in `handleNames()` change from `.findValue("Imię i nazwisko", 1)` to `.findValue("FirstName and LastName", 1)`
2. replacement patterns in `shortenGroups()` according to your template
3. the way that groups are being parsed, for example you may have different delimiter than `;` for groups order

In `student.py` you might need to change the way groups are being assigned.




