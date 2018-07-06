# Python Object Relations Assessment

For this assignment, we'll be working with a Yelp-style domain. We have three models - `Restaurant`, `Customer`, and `Review`.  For our purposes, a `Restaurant` is connected to a `Customer` only if that customer writes a review about the restaurant.  

If you are not sketching out your domain, and thinking about single source of truth, you are doing it wrong :(

You can read about how to submit the assignment at the end.  

## Topics

* Classes vs Instances
* Object Relationships
* Lists and List Methods
* Class Methods

## Notes

Your goal is to build out all of the methods listed in the deliverables.

Remember that to run your code, you can run `python -i environment.rb`.  You'll be able to test out the methods that you write from there. Take a look at that file to see how you can pre-define variables and create object instances, rather than manually doing it each time.

**To Submit** - once you've completed all the deliverables, please copy/paste your three class definitions into the `solution.rb` file. Please don't submit the lab until we give you the signal.

## Deliverables

Build the following methods on the `Customer` class

* Customer.all()
  * should return **all** of the customer instances
* Customer.find_by_name(name)
  * given a string of a **full name**, returns the **first customer** whose full name matches
* Customer.find_all_by_first_name(name)
  * given a string of a first name, returns an **list** containing all customers with that first name
* Customer.all_names()
  * should return a **list** of all of the customer full names
* Customer#add_review(restaurant, content)
  * given a **restaurant object** and some review content (as a string), creates a new review and associates it with that customer and restaurant. A `Review` belongs to a `Customer` and belongs to a `Restaurant`

Build out the following methods on the `Review` class

* Review.all()
  * returns all of the reviews
* Review#customer
  * returns the customer object for that given review
* Review#restaurant
  * returns the restaurant object for that given review

Build out the following methods on the `Restaurant` class

* Restaurant.all()
  * returns a list of all restaurants
* Restaurant.find_by_name(name)
  * given a string of restaurant name, returns the first restaurant that matches
* Restaurant#reviews
  * returns an array of all reviews for that restaurant
* Restaurant#customers
  * returns all of customers who have written reviews of that restaurant. A `Restaurant` has many `Customers` and a `Customer` has many `Restaurants`

### Submitting your code challenge

We'll be submitting the form using the gist gem.  The gist gem allows you to quickly make and get a link to a short github repository. 

1. Place all of your code in `solution.py`
2. Install gist, by going to your terminal and typing `gem install gist` or `brew install gist`.
3. From the folder of your assessment, type into the terminal `gist solution.py`
4. (Optional) If you need to login with your credentials, simply run `gist --login`, and then when logged in type `gist solution.py` into your terminal again.
5. Running `gist solution` will return a link to your gist.  
6. Go to [this google form](https://goo.gl/forms/0N1QJpzqrHtOGo462), and enter your name and a link to the gist.
