import unittest
import mock

open_name = "cshare.controller.google_adapter.open"

from uuid import uuid4

from cshare.controller import GoogleAdapter

FAKE_ACCESS_URL = "https://localhost:63000/request_url"


class TestAdapter(unittest.TestCase):
    def setUp(self):
        self._access_token = str(uuid4())
        self._mock_authenticator = mock.MagicMock()
        self._mock_authenticator.next.side_effect = [FAKE_ACCESS_URL,
                                                     self._access_token]
        self._mock_accessor = mock.MagicMock()
        self._mock_accessor.create_auth.return_value = self._mock_authenticator


    def isolation(self, mocked_file, mocked_pickle, mocked_os):
        assert isinstance(mocked_os, object)
        mocked_os.path.join.return_value = "STRING"
        mocked_os.path.exists.return_value = False
        mocked_file.return_value = mock.MagicMock(spec=file)

    @mock.patch(open_name, create=True)
    @mock.patch('cshare.controller.google_adapter.os')
    @mock.patch('cshare.controller.google_adapter.pickle')
    def test_get_url(self, mocked_os, mocked_pickle, mocked_file):
        adapter = GoogleAdapter(self._mock_accessor)
        url = adapter.get_access_url()
        self.assertEqual(url, FAKE_ACCESS_URL)
        self.assertTrue(self._mock_authenticator.next.called)
        self.assertTrue(self._mock_accessor.create_auth.called)

    @mock.patch(open_name, create=True)
    @mock.patch('cshare.controller.google_adapter.os')
    @mock.patch('cshare.controller.google_adapter.pickle')
    def test_access_credentials(self, mocked_os, mocked_pickle,
                                mocked_file):
        self.isolation(mocked_file, mocked_os, mocked_pickle)
        adapter = GoogleAdapter(self._mock_accessor)
        url = adapter.get_access_url()
        auth_token = adapter.get_access_credentials()
        self.assertEqual(url, FAKE_ACCESS_URL)
        self.assertEqual(auth_token, self._access_token)

    @mock.patch(open_name, create=True)
    @mock.patch('cshare.controller.google_adapter.os')
    @mock.patch('cshare.controller.google_adapter.pickle')
    def test_login(self, mocked_os, mocked_pickle, mocked_file):
        self.isolation(mocked_file, mocked_os, mocked_pickle)
        adapter = GoogleAdapter(self._mock_accessor)
        adapter.login()
