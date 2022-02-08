from abstractions import DataTable


def main():
    # users = UserGenerator().generate(full_names=True, amount=5).getData()
    # table = DataTable([
    #     Column('name', NameGenerator(full_name=False)),
    #     Column('email', EmailGenerator()),
    #     Column('subscription_status', CategoryGenerator(
    #         ['subscribed', 'unsubscribed', 'unknown'])),
    #     Column('amount_spent', CurrencyGenerator(
    #         '$', amount_range=(0, 250000))),
    #     Column('date', DateGenerator('1/1/2022 1:30 pm', '1/22/2022 1:30 pm')),
    # ])

    table = DataTable(schema_path='schema_2.json')

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
