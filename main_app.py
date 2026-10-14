# Author: OWETHU KGATITSOE


import random
import datetime
import data_utils


def main():

    transaction_1 = (random.randint(50, 500))
    transaction_2 = (random.randint(50, 500))
    transaction_3 = (random.randint(50, 500))
    transaction_4 = (random.randint(50, 500))
    transaction_5 = (random.randint(50, 500))

    today_date = datetime.date.today()

    average_amount = data_utils.calculate_average(transaction_1, transaction_2, transaction_3, transaction_4, transaction_5)

    formatted_average = data_utils.format_currency(average_amount)
    print("=== transaction summary ===")
    print(today_date)
    print(average_amount)
    print(formatted_average)
    print("===========================")


if __name__ == "__main__":
    main()
