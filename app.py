#!/usr/bin/python

from flask import Flask
application = Flask(__name__)


@application.route('/beverage/', methods=['POST'])
def create_beverage():
    # create a beverage
    return 'created a beverage'


@application.route('/beverage/<beverage_id>')
def get_beverage(beverage_id):
    # get a beverage
    return '{} beverage number'.format(beverage_id)


@application.route('/beverage/')
def list_beverages():
    # get all beverages
    return 'All beverages'


@application.route('/compare/')
def get_beverage_comparison():
    # Combination of beverages
    return 'Comparison of some beverages'

if __name__ == '__main__':
    application.run()
