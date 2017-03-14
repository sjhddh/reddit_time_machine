# reddit_time_machine
A Python package for traveling back to a historical date and extracting reddit channel contents.

Usage:

`from reddit_time_machine.model import TimeMachine`

and then, process it by calling:

`TimeMachine.process()`

Parameters includes:

```
        :param startdate: start date of time machine, must be used together with enddate.
        :param enddate: end date / main date for time machine, can be used without startdate.
        :param channel: reddit channel
        :param filename: where to save data
        :param sort: ways to sort daily reddit headlines
        :param count: number of headlines returned per day
        :param filter: keyword filtering
        :return: success or not
```

