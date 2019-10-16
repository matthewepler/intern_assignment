import os
import pytest

import intern_assignment.dbtool as dbtool


class TestDbtool():

    def test_open_file(self, tmpdir):
        # file fixture 
        csv_fixture = tmpdir.mkdir('tmp').join('test.csv')
        csv_fixture.write('header1,header2\nrow1a,row1b')

        result = dbtool.open_file(csv_fixture)

        assert result[0][0] == 'header1'
        assert result[1][1] == 'row1b'

