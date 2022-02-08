# CSV Dataset Generator
 Simple 🐍 python program for quickly generating datasets and writing them to a csv file.

#### Installing Dependencies 
💡 Run these commands in order, assuming you have installed python from [python-download](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe)
``` bash

$ py -m venv venv 

$ venv/scripts/activate

$ pip3 install -r requirements.txt
```

#### Usage
``` python 

table = DataTable([
    Column('name', NameGenerator(full_name=False)),
    Column('email', EmailGenerator()),
    Column('subscription_status', CategoryGenerator(['subscribed', 'unsubscribed', 'unknown'])),
    Column('amount_spent', CurrencyGenerator('$', amount_range=(0,250000))),
    Column('date', DateGenerator('1/1/2022 1:30 pm', '1/22/2022 1:30 pm')),
])

# define number of rows in table
table.set_rows(5)

# create row data 
table.generate_rows()

# display table data (uses prettytable to print)
table.print_rows(pretty=True)

# write to csv
CSVWriter.write_to('whatever_name.csv', table)

'''
outputs: 
+----------+-----------------------------+---------------------+--------------+---------------------+
|   name   |            email            | subscription_status | amount_spent |         date        |
+----------+-----------------------------+---------------------+--------------+---------------------+
| Michael  |    pluckyJerky6@yahoo.com   |       unknown       |  $76854.89   | 01/22/2022 06:40 AM |
| Benjamin |  humorousJerky7@outlook.com |     unsubscribed    |  $120075.98  | 01/16/2022 07:05 PM |
| Patrick  |    zestyOwl9@outlook.com    |     unsubscribed    |  $246514.66  | 01/19/2022 06:26 AM |
|   Ana    | finickyTortoise2@icloud.com |     unsubscribed    |  $138574.19  | 01/12/2022 05:09 PM |
|  Ronald  |   bubblySeafowl9@gmail.com  |      subscribed     |  $60869.17   | 01/12/2022 10:07 AM |
+----------+-----------------------------+---------------------+--------------+---------------------+

Completed writing data to: whatever_name.csv
'''

```

### Using Json Schemas 
``` python 

table = DataTable(schema_path="schema_file_name.json")

# define number of rows in table
table.set_rows(5)

# create row data 
table.generate_rows()

# display table data (uses prettytable to print)
table.print_rows(pretty=True)

# write to csv
CSVWriter.write_to('whatever_name.csv', table)

'''
outputs: 
+-----------+---------------------+------+
|    name   | subscription_status | rank |
+-----------+---------------------+------+
| Marquetta |     unsubscribed    |  40  |
|   Karen   |      subscribed     |  38  |
|   Janine  |     unsubscribed    |  13  |
|   Kevin   |      subscribed     |  28  |
|  Latrina  |       unknown       |  3   |
+-----------+---------------------+------+

Completed writing data to: whatever_name.csv
'''

```