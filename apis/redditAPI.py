"""
This is a Reddit time machine that returns the "top news of the day" in reddit.

tested on channel /r/News
"""

import requests
import datetime
import time
import csv
import json
from tools.ascii_saver import ascii_saver
from random import randint


# sample: 'http://www.reddit.com/r/all/search.json?q=timestamp:1119484800..1119571200&sort=top&restrict_sr=on&syntax=cloudsearch'

def runbytime(enddate, startdate=None, channel='/r/worldnews', sort='top', count=25, filename = 'RedditNews.csv'):
    """
    :param enddate: YYYYMMDD
    :param startdate: YYYYMMDD
    :param channel: reddit channel
    :param sort: sorting method
    :return:
    """

    def timeconverter(datestring):
        YYYY = datestring[:4]
        MM = datestring[4:6]
        DD = datestring[6:]
        current = datetime.datetime(int(YYYY), int(MM), int(DD))
        return int(time.mktime(current.timetuple()))

    def generate_a_day(timestp):
        s = 'timestamp:'
        s = s + str(timestp) + '..' + str(timestp + 86400)
        return s

    def previous_day(timestp):
        return int(timestp - 86400)

    def timestampconverter(timestp):
        return datetime.datetime.fromtimestamp(int(timestp)).strftime('%Y-%m-%d')

    url = 'http://www.reddit.com' + channel + '/search.json'

    param = {
        'sort': sort,
        'restrict_sr': 'on',
        'syntax': 'cloudsearch',
        'count': count,
    }

    endpoint = timeconverter(enddate)
    if startdate != None:
        startpoint = timeconverter(startdate)
    else:
        startpoint = endpoint

    current = endpoint

    while current >= startpoint:
        try:
            param['q'] = generate_a_day(current)
            r = requests.get(url, params=param)
            data = json.loads(r.text)

            with open('./data/'+filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"')
                for d in data['data']['children']:
                    writer.writerow([timestampconverter(current), ascii_saver(d['data']['title'])])
        except:
            print('error: ', data)
            time.sleep(randint(3, 5))
            continue

        print('Done: ', timestampconverter(current))
        current = previous_day(current)
        time.sleep(randint(3, 5))


def runbytitle(title, enddate, startdate=None, channel='/r/worldnews', sort='top', count=25, filename = 'RedditNews.csv'):
    """
    :param: title: list of titles
    :param enddate: YYYYMMDD
    :param startdate: YYYYMMDD
    :param channel: reddit channel
    :param sort: sorting method
    :return:
    """

    def timeconverter(datestring):
        YYYY = datestring[:4]
        MM = datestring[4:6]
        DD = datestring[6:]
        current = datetime.datetime(int(YYYY), int(MM), int(DD))
        return int(time.mktime(current.timetuple()))

    def generate_a_query(timestp):
        s = '(and timestamp:'
        s = s + str(timestp) + '..' + str(timestp + 86400)

        q = ' (or'
        for i in title:
            q += " title:'"+i+"'"
        q += ')'

        s += q + ')'
        return s

    def previous_day(timestp):
        return int(timestp - 86400)

    def timestampconverter(timestp):
        return datetime.datetime.fromtimestamp(int(timestp)).strftime('%Y-%m-%d')

    url = 'http://www.reddit.com' + channel + '/search.json'

    param = {
        'sort': sort,
        'restrict_sr': 'on',
        'syntax': 'cloudsearch',
        'count': count,
    }

    endpoint = timeconverter(enddate)
    if startdate != None:
        startpoint = timeconverter(startdate)
    else:
        startpoint = endpoint

    current = endpoint

    while current >= startpoint:
        try:
            param['q'] = generate_a_query(current)
            r = requests.get(url, params=param)
            data = json.loads(r.text)

            with open('./data/'+filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"')
                for d in data['data']['children']:
                    writer.writerow([timestampconverter(current), ascii_saver(d['data']['title'])])
        except:
            print('error: ', data)
            time.sleep(randint(3, 5))
            continue

        print('Done: ', timestampconverter(current))
        current = previous_day(current)
        time.sleep(randint(3, 5))



if __name__ == '__main__':
    runbytime('20100821', startdate='20080808', channel='/r/economics', filename='RedditEcoNews.csv')
    # runbytitle(['bankruptcy', 'failure to pay', 'obligation default', 'obligation acceleration', 'repudiation', 'moratorium', 'restructuring', 'credit rating'], '20160701', startdate='20080808', count=50, channel='/r/business')