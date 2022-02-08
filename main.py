from random_username.generate import generate_username
from random_address import real_random_address
from typing import Any, List, Tuple
from datetime import timedelta
from datetime import datetime
import random
import names 
import uuid
import csv

def random_index(arr: List):
    return random.randint(0, len(arr) -1)

def string_to_date(_date_string: str):
    return datetime.strptime(_date_string, '%m/%d/%Y %I:%M %p')

def date_to_string(_datetime):
    return datetime.strftime(_datetime, '%m/%d/%Y %I:%M %p')

class DataGenerator:
    
    def __init__(self, amount: int = 25, from_list = None):
        self.data: List[Any] = []
        self.amount = amount
        self.from_list = from_list
        return 
    
    def generate(self):
        for i in range(0, self.amount):
            self.data.append(self.from_list[random_index(self.from_list)])
        return self
    
    def set_amount(self, amount: int):
        self.amount = amount
    
    def getData(self):
        return self.data

class BooleanGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, from_list=None):
        super().__init__(amount, from_list)
    
    def generate(self):
        for i in range(0, self.amount):
            self.data.append(bool(random.getrandbits(1)))
        return self
    
class NameGenerator(DataGenerator):

    def __init__(self, amount: int = 25, full_name: bool = True, from_list=None):
        super().__init__(amount, from_list)
        self.full_name = full_name
        return

    def generate(self):
        '''
        Generates a number of unique names based on the amount provided.  
        '''
        if self.from_list:
            super().generate()
            return self
        name_pool = self.__gen_names(self.full_name, self.amount)
        for i in range(0,self.amount):
            self.data.append(name_pool[i])
        return self
    
    def __gen_names(self, full_name: bool, name_pool_count: int):
        return [names.get_full_name() for i in range(0,name_pool_count)] if full_name else [names.get_first_name() for i in range(0,name_pool_count)]
        
class EmailGenerator(DataGenerator):
    
    def __init__(self, providers=['gmail', 'hotmail', 'outlook', 'yahoo', 'icloud'], amount: int = 25, from_list=None):
        super().__init__(amount, from_list)
        self.providers = list(map(lambda provider: f'@{provider}.com', providers))
        
    def generate(self):
        usernames = generate_username(self.amount)
        for i in range(0, self.amount):
            self.data.append(f'{usernames[i]}{self.providers[random_index(self.providers)]}')
        return self
    
class NumberGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, num_range: Tuple=(0,10), use_floats: bool = False, decimal_cutoff: int =2, from_list=None):
        super().__init__(amount, from_list)
        self.range: Tuple = num_range 
        self.use_floats = use_floats
        self.decimal_cutoff = decimal_cutoff
        return 
    
    def generate(self):
        '''
        Generates a list of random numbers (ints of floats) based on the amount provided.
        '''
        if self.from_list:
            super().generate(self.amount, self.from_list)
            return self
        for i in range(0, self.amount):
            self.data.append(round(random.uniform(self.range[0], self.range[1]), self.decimal_cutoff)) if self.use_floats else self.data.append(random.randint(self.range[0], self.range[1]))
        return self
    
class IDGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, max_length: float = 3, from_list=None):
        super().__init__(amount, from_list)
        self.max_length = max_length
    
    def generate(self):
        '''
        Generates unique ids based on the amount provided
        '''
        if self.from_list:
            super().generate(self.amount, self.from_list)
            return self
        id_pool = self.__gen_ids(self.amount, self.max_length)
        for i in range(0, self.amount):
            self.data.append(id_pool[i])
        return self
            
    def __gen_ids(self, id_pool_count: int, maxLength: int):
        return [str(uuid.uuid4())[0:maxLength] for i in range(0, id_pool_count)]
    
class PercentageGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, from_list=None):
        super().__init__(amount, from_list)
    
    def generate(self):
        '''
        Generates a list of percentages, with possible duplicates.
        '''
        if self.from_list:
            super().generate(self.amount, self.from_list)
            return self
        for i in range(0, self.amount):
            self.data.appen(random.uniform(0.01,99.9))
        return self
    
class CategoryGenerator(DataGenerator):
    
    def __init__(self, categories: List, amount: int = 25):
        super().__init__(amount, categories)
    
    def generate(self):
        '''
        Generates a list of categories, with duplicates.
        '''
        super().generate()
        return self
    

class DateGenerator(DataGenerator):
    
    def __init__(self, start_date, end_date, amount: int = 25, from_list=None):
        super().__init__(amount, from_list)
        self.start_date = string_to_date(start_date)
        self.end_date = string_to_date(end_date)
    
    def generate(self):
        if self.from_list:
            super().generate(self.amount, self.from_list)
            return self
        for i in range(0, self.amount):
            self.data.append(self.__get_date(self.start_date, self.end_date))
        return self
    
    def __get_date(self, start_date, end_date):
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        date_time = start_date + timedelta(seconds=random_second) 
        return date_to_string(date_time)

class AddressGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, with_zips: bool = True, from_list=None):
        super().__init__(amount, from_list)
        self.with_zips = with_zips
    
    def generate(self):
        '''
        Generates unique addresses based on the amount provided.
        '''
        if self.from_list:
            super().generate(self.amount, self.from_list)
            return self
        address_pool = self.__gen_addresses(self.amount, self.with_zips)
        for i in range(0, self.amount):
            self.data.append(address_pool[i])
        return self
        
    def __gen_addresses(self, address_pool_count: int, with_zips: bool):
        addresses = []
        for i in range(0, address_pool_count):
            address_obj = real_random_address()
            addresses.append({ 'address': address_obj['address1'], 'zip': address_obj['postalCode']}) if with_zips else addresses.append(address_obj['address1'])
        return addresses
    
class ZipCodeGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, from_list=None):
        super().__init__(amount, from_list)
    
    def generate(self):
        '''
        Generates unique zip codes based on the amount provided
        '''
        if self.from_list:
            super().generate(self.amount, self.from_list)
            return self
        zipcodes_pool = self.__gen_zipcodes(self.amount)
        for i in range(0, self.amount):
            self.data.append(zipcodes_pool[i])
        return self
        
    def __gen_zipcodes(self, zip_pool_count: int):
        return [real_random_address()['postalCode'] for i in range(0, zip_pool_count)]

class CurrencyGenerator(DataGenerator):
    
    def __init__(self, currency_symbol: str, amount_range = (0,100000), amount: int = 25, from_list=None):
        super().__init__(amount, from_list)
        self.currency_symbol: str = currency_symbol
        self.amount_range = amount_range
        
    def generate(self):
        currencies = NumberGenerator(self.amount, self.amount_range, True, 2).generate().getData()
        for curr in currencies:
            self.data.append(f'{self.currency_symbol}{str(curr)}')
        return self
        
class UserGenerator(DataGenerator):
    
    def __init__(self, amount: int = 25, full_names: bool = False, id_length: int = 4, from_list=None):
        super().__init__(amount, from_list)
        self.full_names = full_names
        self.id_length = id_length
    
    def generate(self):
        '''
        Generates a list of user objects based on the amount provided.
        '''
        if (self.from_list):
            super().generate(self.amount, self.from_list)
            return self
        ''' 
            user = {
                name: '',
                address: '',
                zip: '',
                id: ''
            }
        '''
        name_pool = NameGenerator().generate(self.amount, self.full_names).getData()
        address_pool = AddressGenerator().generate(self.amount).getData()
        id_pool = IDGenerator().generate(self.amount, self.id_length).getData()
        for i in range(0, self.amount):
            self.data.append({
                'name': name_pool[i],
                'address': address_pool[i]['address'],
                'zip': address_pool[i]['zip'],
                'id': id_pool[i]
            })
        return self      
 
class Column:
    
    def __init__(self, name: str, data_generator: DataGenerator) -> None:
        self.name = name
        self.generator = data_generator
        pass
 
class DataTable:
    
    def __init__(self, cols: List[Column] = [], row_count: int = 25):
        self.cols: List[Column] = []
        if cols:
            for col in cols:
                self.add_col(col)
        self.row_count: int = row_count
        self.rows: List[List[Any]] = []
        self.__set_headers()
        return 
    
    def __set_headers(self):
        self.headers = [col.name for col in self.cols]
    
    def add_col(self, column: Column):
        self.cols.append(column)
        self.__set_headers()
        return
    
    def del_col(self, name: str):
        self.cols = list(filter(lambda col: col.name != name, self.cols))
        self.__set_headers()
        return 
    
    def set_rows(self, row_count: int):
        self.row_count = row_count
        
    def generate_rows(self, reuse_anchor_col: str = None, anchor_count: int = None):
        '''
        Generates row data based on the columns specified 
        and the number of rows defined. If reuse_anchor_col 
        is provided, multiple rows will be attributed 
        to anchor points e.g., ['john', 'asdf', 'asdfasd
        ', '12/12/23'], ... ['john', ..., '02/10/24']
        '''
        if (reuse_anchor_col):
            # create a pool from anchors 
            return 
        for i in range(0,self.row_count):
            row_data = []
            for col in self.cols:
                col.generator.set_amount(self.row_count)
                row_data.append(col.generator.generate().getData()[i])
            self.rows.append(row_data)
        return 
    
    def print_rows(self):
        for i in range(0, self.row_count):
            print(self.rows[i])

class CSVWriter:
    
    def write_to(file_name: str, table: DataTable):
       with open(file_name, 'w') as csvfile:
           fwriter = csv.writer(
               csvfile, 
               delimiter=',',
               quotechar='|', 
               quoting=csv.QUOTE_MINIMAL
               )
           # write the column header first 
           fwriter.writerow(table.headers)
           #fwriter.writerows(table.rows)
           for row in table.rows:
               fwriter.writerow(row)
           print(f'Completed writing data to: ${file_name}')
           return
    
def main():
    # users = UserGenerator().generate(full_names=True, amount=5).getData()
    table = DataTable([
        Column('name', NameGenerator(full_name=False)),
        Column('email', EmailGenerator()),
        Column('subscription_status', CategoryGenerator(['subscribed', 'unsubscribed', 'unknown'])),
        Column('amount_spent', CurrencyGenerator('$', amount_range=(0,250000))),
        Column('date', DateGenerator('1/1/2022 1:30 pm', '1/22/2022 1:30 pm')),
    ])
    # table = DataTable([
    #     Column('age', NumberGenerator(num_range=(13,85))),
    #     Column('income', CurrencyGenerator('$', amount_range=(0,250000))),
    #     Column('product_line', CategoryGenerator(['office_suite'])),
    #     Column('prev_purchase', CategoryGenerator(['yes', 'no'])),
    #     Column('region', CategoryGenerator(['northeast', 'midwest', 'south', 'west'])),
    #     Column('tos(m)', NumberGenerator(num_range=(1,500))),
    #     Column('day', CategoryGenerator(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']))
    # ])
    
    # defines the number or rows (data points) you'd like
    table.set_rows(5)
    # fills the table's the row/coumn data
    table.generate_rows()
    # display the table data in the console
    table.print_rows()
    
    # write table to csv - change name to write to different file
    # CSVWriter.write_to('msft_gen_data.csv', table)
    return 

main()