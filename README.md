# reddit_time_machine
A Python package for traveling back to a historical date and extracting reddit channel contents.

To install:

`pip install reddit_time_machine`


Usage:

`from reddit_time_machine.model import TimeMachine`

and then, process it by calling:

```python
# remember to init the class first:
TM = TimeMachine()
# then process:
TM.process()
```


Parameters includes:

```python
        :param startdate: start date of time machine, must be used together with enddate.
        :param enddate: end date / main date for time machine, can be used without startdate.
        :param channel: reddit channel
        :param filename: where to save data
        :param sort: ways to sort daily reddit headlines
        :param count: number of headlines returned per day
        :param filter: keyword filtering
        :return: success or not
```

Note:

I'm still trying to make this package nicer and more functional either as a time machine for multiple platforms or as a reddit easy-to-use package.
 
If you have any questions, please contact me directly through GitHub.

Also, you are very welcome to donate your codes~

