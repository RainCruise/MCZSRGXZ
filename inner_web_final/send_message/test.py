import unittest
from django.test import TestCase, Client
def division_funtion(x, y):
    return round(float(x) / y, 6)

class MyTestCase(TestCase):
    def test_about(self):
        response = self.client.get('/about.html/')
        self.assertEqual(response.status_code, 200)

    def test_history(self):
        response = self.client.get('/history.html/')
        self.assertEqual(response.status_code, 200)

    def test_sendmessage(self):
        response = self.client.get('/send_message.html/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('//')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)


    def test_sendmessage_request(self):
        c = Client()
        rep = c.post("/send_message.html/", {"'message'": "'/TITLE:kjiyu:TITLE//CONTENTS:xsabnmkjw:CONTENTS//FILE:log.txt:FILE//UUID:dcb76773-6e1f-480b-bb88-af542cc33e01:UUID/'"})
        self.assertEqual(rep.status_code, 200)

    def test_history_request(self):
        c = Client()
        rep = c.post("/history.html/", {'uuid': 'dcb76773-6e1f-480b-bb88-af542cc33e01'})
        self.assertEqual(rep.status_code, 200)

    def test_about_request(self):
        c = Client()
        rep = c.post("/about.html/")
        self.assertEqual(rep.status_code, 200)


    def test_register(self):
        c = Client()
        rep = c.post("/register/", {'username': 'Rain', 'password': 'rain1996abc'})
        self.assertEqual(rep.status_code, 200)

    def test_login(self):
        c = Client()
        rep = c.post("//", {'username': 'Rain', 'password': 'rain1996abc'})
        self.assertEqual(rep.status_code, 200)

if __name__ == '__main__':
    unittest.main()
