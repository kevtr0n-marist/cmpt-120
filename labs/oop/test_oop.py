from oop import Review, Movie
import pytest

movie = Movie("Star Wars: A New Hope", 1977, "George Lucas")

@pytest.fixture(autouse=True)
def setup_and_teardown():
    global movie
    movie.reviews = []
    yield
    movie.reviews = []

class TestClass:

    def test_00(self):
        '''
        Test that the movie gets initialized with proper fields.
        '''
        assert movie != None
        assert type(movie.movie_id) == str
        assert type(movie.year) == int
        assert type(movie.reviews) == list

    def test_01(self):
        '''
        Test that a review gets initialized with the proper fields.
        '''
        review = Review("kevtr0n", 5, "Great movie!")
        assert review != None
        assert type(review.review_id) == str
        assert type(review.username) == str
        assert type(review.review) == str

    def test_02(self):
        '''
        Test that we can add a review.
        '''
        review = Review("kevtr0n", 5, "Great movie!")
        movie.add_review(review)
        assert len(movie.reviews) == 1
        assert type(movie.reviews[0]) == Review

    def test_03(self):
        '''
        Test that we can add/modify a score.
        '''
        review = Review("kevtr0n", 5, "Great movie!")
        movie.add_review(review)
        movie.modify_score(review.review_id, 4)

    def test_04(self):
        '''
        Test that we can add/modify a review.
        '''
        review = Review("kevtr0n", 5, "Great movie!")
        movie.add_review(review)
        movie.modify_review(review.review_id, "One of my favorites!")
        assert review.review == "One of my favorites!"

    def test_05(self):
        '''
        Test that we can delete a review.
        '''
        review = Review("kevtr0n", 5, "Great movie!!!")
        movie.add_review(review)
        for r in movie.reviews:
            print(r.review)
        movie.delete_review(review.review_id)
        assert len(movie.reviews) == 0

    def test_06(self):
        '''
        Test that an exception is thrown with empty title.
        '''
        with pytest.raises(Exception):
            Movie("", 2023, "Me")


    def test_07(self):
        '''
        Test that an exception is thrown with a null title.
        '''
        with pytest.raises(Exception):
            Movie(None, 2023, "Me")

    def test_08(self):
        '''
        Test that a null username will raise exception.
        '''
        with pytest.raises(Exception):
            Review(None, 5, "Me")

    def test_09(self):
        '''
        Test that a score too high will raise exception.
        '''
        with pytest.raises(Exception):
            Review("Me292", 6, "Me")

    def test_10(self):
        '''
        Test that a score too low will raise an exception.
        '''
        with pytest.raises(Exception):
            Review("akjhasd", -1, "Me")

    def test_11(self):
        '''
        Test that an empty director will raise an exception.
        '''
        with pytest.raises(Exception):
            Movie("Aladdin", 3, "")

    def test_12(self):
        '''
        Test that a null score will raise an exception.
        '''
        with pytest.raises(Exception):
            Movie("Aladdin", None, "Me")

    def test_13(self):
        '''
        Test an invalid type for title will raise exception.
        '''
        with pytest.raises(Exception):
            Movie(False, 2004, "Me")
    
    def test_14(self):
        '''
        Test that an invalid type for year will raise exception.
        '''
        with pytest.raises(Exception):
            Movie("aksjdhaks", False, "Me")

    def test_15(self):
        '''
        Test that an invalid type for review will raise exception.
        '''
        with pytest.raises(Exception):
            Movie("False", 2000, True)

    def test_16(self):
        '''
        Test that an invalid type for username will raise exception.
        '''
        with pytest.raises(Exception):
            Review(False, 4, "Me")

    def test_17(self):
        '''
        Test that an invalid type for score will raise exception.
        '''
        with pytest.raises(Exception):
            Review("False", True, "Me")

    def test_18(self):
        '''
        Test that an invalid type for review will raise exception.
        '''
        with pytest.raises(Exception):
            Review("False", 4, False)