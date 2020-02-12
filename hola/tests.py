from django.test import TestCase

class TestSmoke(TestCase):

    def test_smoke_test(self):
        self.assertEquals(2+2,4)
