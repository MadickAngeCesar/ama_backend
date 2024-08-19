import unittest
from app import create_app, db
from app.models import Routine

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('instance/config.py')
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_routine(self):
        response = self.client.post('/add', data={
            'title': 'Morning Routine',
            'description': 'Wake up, exercise, and eat breakfast.',
            'start_time': '06:00',
            'end_time': '08:00'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Morning Routine', response.data)
