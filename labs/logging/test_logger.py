import re
from pathlib import Path
from logger import *
from datetime import datetime

today = datetime.today()
log_file_regex = re.compile(r'log-file-[0-9]{4}-[0-9]{2}-[0-9]{2}.log')


class TestClass:

    def test_1(self):
        '''
        Ensure log file is in correct format.
        '''
        log_file_name = self.get_log_file()
        mo = log_file_regex.search(log_file_name)
        assert mo.group() in log_file_name

    def test_2(self):
        '''
        Ensure logs write to file.
        '''
        log("Hello, world!")
        f = open(self.get_log_file(), "r")
        assert "Hello, world!" in f.read()

    def test_3(self):
        '''
        Ensure log file is in correct location.
        '''
        filepath = self.get_log_file()
        assert Path(filepath).is_file()

    def get_log_file(self):
        date = "{0}-{1:02d}-{2:02d}".format(today.year, today.month, today.day)
        filename = "log-file-{0}.log".format(date)
        return filename

