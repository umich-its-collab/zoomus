import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DeleteSSOTokenV2TestCase))
    return suite


class DeleteSSOTokenV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.user.UserComponentV2(
            base_uri="http://foo.com",
            config={
                "api_key": "KEY",
                "api_secret": "SECRET",
                "version": util.API_VERSION_2,
            },
        )

    @responses.activate
    def test_can_delete_sso_token(self):
        responses.add(responses.DELETE, "http://foo.com/users/42/token")
        response = self.component.delete_sso_token(id="42")
        self.assertEqual(response.request.body, None)

    def test_requires_id(self):
        with self.assertRaisesRegexp(ValueError, "'id' must be set"):
            self.component.delete_sso_token()


if __name__ == "__main__":
    unittest.main()
