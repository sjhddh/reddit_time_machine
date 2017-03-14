from apis.redditAPI import runbytime
from apis.redditAPI import runbytitle


class TimeMachine:
    """
    Main class.
    """

    def __init__(self):
        """
        Init.
        ahh.. we do not need to do anything here
        I'll leave it blank for future.
        """
        pass

    def process(self, enddate, startdate=None, channel='/r/worldnews', filename='RedditEcoNews.csv',
                sort='top', count=25, filter=None):
        """
        Main process method to run time machine

        :param startdate: start date of time machine, must be used together with enddate.
        :param enddate: end date / main date for time machine, can be used without startdate.
        :param channel: reddit channel
        :param filename: where to save data
        :param sort: ways to sort daily reddit headlines
        :param count: number of headlines returned per day
        :param filter: keyword filtering
        :return: success or not
        """
        if filter is None:
            runbytime(enddate=enddate, startdate=startdate, channel=channel, filename=filename, sort=sort, count=count)
        else:
            runbytitle(title=filter, enddate=enddate, startdate=startdate, channel=channel, filename=filename,
                       sort=sort, count=count)

        return "Ding...Dong..."
