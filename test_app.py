import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Actors, Movies
from app import create_app


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.db_path = os.environ['DATABASE_URL']
        self.token = os.environ['TOKEN_TEST']
        setup_db(self.app, self.db_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = {
            "name": "Brad Pitt",
            "age": 55,
            "gender": "Male"
        }

        self.new_movie = {
            "title": "Once upon a time in Hollywood",
            "releasedate": "26-07-2019"
        }

        self.update_actor = {
            "age": 56
        }

        self.update_movie = {
            "title": "Ad Astra"
        }

        # Valid Token passed from environment
        self.authorization = {
            "Authorization": self.token
        }

        # Invalid Token
        self.authorization_exp = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpFcTdCSUhnaURSXzliZUNJS3JoayJ9.eyJpc3MiOiJodHRwczovL3NhaW5hdGgtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5ZDVmOGZkZTQzMWEwYzhkNjhhYzFlIiwiYXVkIjoiQ2Fwc3RvbmVBUEkiLCJpYXQiOjE1OTAzMTc5MzksImV4cCI6MTU5MDQwNDMzOSwiYXpwIjoiYm1teWtTMHdRNzJwMkZUNXloZlZTQVRyYnRTaXVONDgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.k9x-c2QlWG-AKJCuN8cOuhjZaP4K3yAkS3PDHjB5Z-XSGGtycA9RLRbL8AKZ8airARRt6DsmnUFkoRQoyhYM4JPhj1Jpl4HIbZwuYDsvASrSPQX7HB9Nl1XQDlW9PnZMYjV-fyPMxRSt_Muxr250iJrCsleL5WTbhErnjJoHKO9UBobWeGG1EDmOZ9t7Q664nSWyEjHY6r3K7of8dvrlbYAmqSs0bDdCoNcp29KQfSZP5xXfplgh4czgLmZoZmBB8xhjZ_CWU2KVXrEJk_OybNZG8w-KrkOFHTRrOUtASy5bb8RTAITjJig6AVGuPByWPK5F8wpBiLoxSI3jtHm6rA"
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_a_get_api_request(self):

        res = self.client.get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['Message']))

    def test_b_create_actors(self):

        res = self.client.post('/actors', json=self.new_actor, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_c_create_movies(self):

        res = self.client.post('/movies', json=self.new_movie, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_d_get_actors(self):

        res = self.client.get('/actors', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_e_get_movies(self):

        res = self.client.get('/movies', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_f_get_actors_by_id(self):

        res = self.client.get('/actors/1', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_g_get_movies_by_id(self):

        res = self.client.get('/movies/1', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_h_update_actors(self):

        res = self.client.patch('/actors/1', json=self.update_actor, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_i_update_movies(self):

        res = self.client.patch('/movies/1', json=self.update_movie, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_j_404_get_actors_by_id(self):

        res = self.client.get('/actors/100', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_k_404_get_movies_by_id(self):

        res = self.client.get('/movies/100', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_l_404_delete_actors_not_exist(self):

        res = self.client.delete('/actors/;;;', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_m_404_delete_movies_not_exist(self):

        res = self.client.delete('/movies/;;;', headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_n_404_update_actors(self):

        res = self.client.patch('/actors/100', json=self.update_actor, headers=self.authorization,)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_o_404_update_movies(self):

        res = self.client.patch('/movies/100', json=self.update_movie, headers=self.authorization, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_p_delete_actors(self):

        res = self.client.delete('/actors/1', headers=self.authorization, )
        data = json.loads(res.data)

        actors = Actors.query.filter(Actors.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actors, None)

    def test_q_delete_movies(self):

        res = self.client.delete('/movies/1', headers=self.authorization, )
        data = json.loads(res.data)

        movies = Movies.query.filter(Movies.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movies, None)

    def test_r_401_auth_missing(self):

        res = self.client.get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_s_403_unauthorized(self):

        res = self.client.get('/actors', headers=self.authorization_exp, )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')


if __name__ == "__main__":
    unittest.main()
