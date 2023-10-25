# Lab 7 - Object Oriented Programming

# Step 1 - Setup

First create a new folder inside our `cmpt-120/labs` folder called `oop` and inside that folder create a file called `oop.py`. Create another file in that folder called `test_oop.py` and copy the contents of my live version on GitHub into yours. __Be sure to save your file(s).__

## Step 2 - Defining the Review class.

The next piece of code we are going to want to define is a class to represent a movie review. Define a class called `Review` that has the following schema.

__review_id__: an `str` variable that represents the individual review's id.\
__username__: a `str` variable that represents the username of the person providing the review; must be between 1-64 characters.\
__score__: an `int` variable that represents a score between 0-5.\
__review__: a `str` variable that represents the actual user review; must be between 0-1024 characters.

> ___Schema__ - a representation of a plan or theory in the form of an outline or model. The overall structure of our class/object._

## Step 3 - Defining the Movie class

The first piece of code we are going to want to define is a class to represent a movie. Define a class called `Movie` that has the following __schema__.

__movie_id__: a `str` variable that represents the individual movie's id.\
__title__: a `str` variable that represents the title of the movie; must be a str between 1-64 characters. \
__year__: an `int` variable that represents the year the movie was released; must be a positive integer. \
__director__: a `str` variable that represents the name of the person who directed the file; must be between 1-64 characters.\
__reviews__: a `list` variable that we will default to empty for now.

Define the class and a constructor method that takes the following arguments and sets them in the constructor method. Keep in mind that the `movie_id` property should be unique across all other movies. So you should programmatically generate a new id. I suggest using the `uuid` library. You can generate new ids like so:

```py
import uuid
movie_id = str(uuid.uuid4())
# This will generate a unique id like '8cb64b3b-fc64-4199-b642-a71587b9bcc9'
```

> __Note__: None of the properties in either the `Review` or `Movie` class may be `None`. So be sure to check it prior to setting the instance variable. My unit tests are testing this!

## Step 4 - Define some Movie class methods

Next, I want you to add 4 methods to the `Movie` class: `add_review`, `modify_score`, `modify_review`, and `delete_review`.

### Add review

The sole purpose of this method is to add a new `Review` object to an instance's list of reviews. Keep in mind that the `review_id` property should be unique across all other reviews in the list. So you should programmatically generate a new id. I suggest using the `uuid` library. You can generate new ids like so:

```py
import uuid
review_id = str(uuid.uuid4())
# This will generate a unique id like '8cb64b3b-fc64-4199-b642-a71587b9bcc9'
```


### Modify score

The sole purpose of this method is to update the score property of an existing `Review` object in a `Movie` object's list of reviews. Your method signature should have __2__ additional arguments: `review_id` and `score`. Your method should iterate through the list of review objects until the review's `review_id` property matches the argument passed into the method. Once you found a match, update the score property. 

> The same conditions still apply; it must be between 1-5.

### Modify review

The sole purpose of this method is to update the review property of an existing `Review` object in a `Movie` object's list of reviews. Your method signature should have __2__ additional arguments: `review_id` and `review`. Your method should iterate through the list of review objects until the review's `review_id` property matches the argument passed into the method. Once you found a match, update the review property.

> The same conditions still apply; it must be between 0-1024 characters.

### Delete review

The sole purpose of this method is delete a `Review` object from a `Movie` object's list of `Reviews`. Your method should have __1__ additional argument: `review_id`. Iterate through the list of reviews until the review's `review_id` property matches the argument passed into the method. Once you found a match, remove it from the list either by invoking the list's `remove` method with the review element.

## Step 5 - Unit testing

Run `pytest` against the `test_oop.py` file and take a screenshot of the output. All of your tests should pass, any failing tests will cause points to be taken off. Submit the screenshot on Brightspace when everything is in working order.