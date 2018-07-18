#!/usr/bin/env python3
import os
import csv

# attempt fallback for python 2.7
# since am running in a virtual env, not testing this
try:
    import statistics
except:
    import  statistics_standin_for_py2 as statistics

from data_types import Purchase



def main():
    banner()
    datafile = get_data_file()
    data = load_data(datafile)
    query_data(data)




def banner():
    print('----------------------------------------------')
    print('              Real Estate App                 ')
    print('----------------------------------------------')
    print()

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'home_data.csv')

def load_data(datafile):

    print('Loading CSV real estate data from {} ..... '.format(datafile), end=' ')

    # python 2.7 does not support encoding
    # open would have to be updated to
    # with open(datafile, 'r') as fin:

    with open(datafile, 'r', encoding='utf-8') as fin:


        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            #print("Bed count: {}".format(row['beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        print('Done')

        return purchases

def query_data(data):# list[Purchase]):

    # data sorted by price
    # inline simple function
    data.sort(key=lambda p: p.price)

    # highest prices house now that we are sorted by price, is the last item
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(high_purchase.price, high_purchase.beds, high_purchase.baths))

    # lowest prices house now that we are sorted by price, is the first
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'.format(low_purchase.price, low_purchase.beds, low_purchase.baths))

    # what is the average price
    prices = [
        p.price  # projection or items
        for p in data # the data to process
    ]


    average_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(average_price)))

    # the average price of a 2 bedroom house is
    two_bed_homes = [
        p # projection or items
        for p in data # the data to process
        if p.beds == 2
    ]

    average_two_bed_price = statistics.mean([announce(p.price, 'price') for p in two_bed_homes[:5]])
    average_two_bed_baths = round(statistics.mean([p.baths for p in two_bed_homes]),1)
    average_two_bed_sqft = round(statistics.mean([p.sq__ft for p in two_bed_homes]),1)

    print('The average 2 bedroom home price is ${:,}, baths ={}, sq ft={}'
          .format(int(average_two_bed_price),average_two_bed_baths,average_two_bed_sqft))


def announce(item,msg):
    print('Pulling item {} for {}'.format(item,msg))
    return item


if __name__ == '__main__':
    main()