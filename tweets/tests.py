from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestTweets(APITestCase):

    
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(
                username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    # GET test of "/api/v1/tweets"
    def test_all_tweets(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200."
        )
        self.assertIsInstance(
            data,
            list,
        )

    
    def test_create_tweet(self):

        self.client.force_login(
                self.user,
        )

        # Post test of "/api/v1/tweets"
        response = self.client.post(
            self.URL,
            data={
                "payload": "test tweet"
            }
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["payload"],
            "test tweet",
        )

        # GET test of "/api/v1/tweets/<int:pk>"
        response = self.client.get(
            self.URL + str(data["id"])
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["payload"],
            "test tweet",
        )

        # PUT test of "/api/v1/tweets/<int:pk>"
        response = self.client.put(
            self.URL + str(data["id"]),
            data = {
              "payload" : "put test"  
            }
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["payload"],
            "put test",
        )

        # DELETE test of "/api/v1/tweets/<int:pk>"
        response = self.client.delete(
            self.URL + str(data["id"]),
        )
        self.assertEqual(
            response.status_code,
            204,
            "Not 204 status code",
        )

