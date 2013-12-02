import unittest
import mock

from uuid import uuid4

from cshare.backend import GData

class TestGData(unittest.TestCase):
    @mock.patch('cshare.backend.gdata_accessor.gdata.calendar.service.CalendarService')
    def test_create_auth(self, mocked_gdata):
        accessor = GData()
        a = accessor.create_auth()
        a.next()
        self.assertTrue(mocked_gdata.called)
        a.next()

    @mock.patch('cshare.backend.gdata_accessor.gdata.calendar.service.CalendarService')
    def test_login(self, mocked_gdata):
        accessor = GData()
        accessor.login(str(uuid4()))
        self.assertTrue(mocked_gdata.called)
