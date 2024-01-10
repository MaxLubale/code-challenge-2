 ## Restaurant Review System

## Overview
  This project implements a simple Restaurant Review System using Python classes. The system comprises three main classes: Customer, Restaurant, and Review. These classes model the relationships between customers, restaurants, and reviews, providing a foundation for a basic review platform.

## Classes
1. Customer Class
  The Customer class represents a customer and includes the following key methods:

    __init__(self, given_name, family_name): Initializes a customer with given and family names and adds them to the list of all customers.
    get_given_name(self): Returns the given name of the customer.
    get_family_name(self): Returns the family name of the customer.
    full_name(self): Combines the given and family names to get the full name.
    all(cls): Class method to retrieve all customers.
    num_reviews(self): Returns the number of reviews written by the customer.
    find_by_name(cls, name): Class method to find a customer by their full name.
    find_all_by_given_name(cls, given_name): Class method to find all customers with a given name.
    add_review(self, restaurant, rating): Adds a review for a restaurant by the customer.
2. Restaurant Class
  The Restaurant class represents a restaurant and includes the following key methods:

    __init__(self, name): Initializes a restaurant with a name and adds it to the list of all restaurants.
    get_name(self): Returns the name of the restaurant.
    reviews(self): Returns all reviews for the restaurant.
    customers(self): Returns all customers who have reviewed the restaurant.
    average_star_rating(self): Calculates the average star rating for the restaurant.
3. Review Class
  The Review class represents a review and includes the following key methods:

    __init__(self, customer, restaurant, rating): Initializes a review with a customer, restaurant, and rating, and adds it to the list of all reviews.
    get_rating(self): Returns the rating of the review.
    all_reviews(cls): Class method to retrieve all reviews.
    get_customer(self): Returns the associated customer of the review.
    get_restaurant(self): Returns the associated restaurant of the review.

## Example Usage
The project includes an example usage section that demonstrates how to create instances of customers, restaurants, and reviews. It showcases methods like num_reviews, average_star_rating, find_by_name, and find_all_by_given_name.

## Getting Started
 To get started with this project, follow these steps:

- Clone the repository to your local machine.
- Run the provided example usage code to understand how the classes work together.
- Customize the classes and methods according to your specific requirements for a restaurant review system.
- Contributions
- Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a  pull request.

## Author
  - Name : MAXWELL CLIFF LUBALE
  - Github : https://github.com/MaxLubale

## License
This project is licensed under the MIT License - see the LICENSE file for details.