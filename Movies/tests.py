from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movies, Reviews

# Create your tests here.

class ReviewsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Create a movie
        self.movie = Movies.objects.create(name='Test Movie', price=10, description='Test Description')
        
        # Create a review
        self.review = Reviews.objects.create(
            movie=self.movie,
            user=self.user,
            review='Great movie!',
            rating=5
        )

    def test_review_creation(self):
        self.assertEqual(self.review.movie.name, 'Test Movie')
        self.assertEqual(self.review.user.username, 'testuser')
        self.assertEqual(self.review.review, 'Great movie!')
        self.assertEqual(self.review.rating, 5)