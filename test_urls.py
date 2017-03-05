from django.test import TestCase


class SimpleTests(TestCase):
    def test_abc(self):
        x = 10 + 20

    def test_not_found(self):
        url = "/foobar/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_add(self):
        x, y = 100, 200
        url = "/add/{}/{}/".format(x, y)
        expected = "{} + {} = <b>{}</b>".format(
            x, y, x + y
        )

        resp = self.client.get(url)
        self.assertContains(resp, expected)
