# CSV Dataset Generator
 Simple python program for quickly generating datasets and writing them to a csv


## Usage
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

# display table data 
table.print_rows()

'''
outputs: 
['Johnny', 'joyfulIcecream8@icloud.com', 'subscribed', '$230956.95', '01/17/2022 07:24 AM']
['Sandra', 'relievedWasp8@outlook.com', 'unknown', '$140249.2', '01/04/2022 08:23 AM']       
['Matthew', 'sincereCheetah0@yahoo.com', 'subscribed', '$218325.14', '01/03/2022 10:01 PM']  
['Alicia', 'madDoughnut9@gmail.com', 'unsubscribed', '$106352.42', '01/05/2022 05:03 PM']    
['Robert', 'puzzledCardinal3@yahoo.com', 'unsubscribed', '$109170.01', '01/10/2022 04:06 PM']
'''

```