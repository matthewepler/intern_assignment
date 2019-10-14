import pytest

import intern_assignment.dbtool as dbtool

class TestDbtool():
    def test_hello(self):
        assert dbtool.hello() == 'hello'
