class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        return len([review for review in Review.all_reviews() if review.get_customer() == self])

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.get_given_name() == given_name]

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        return review


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.all_reviews() if review.get_restaurant() == self]

    def customers(self):
        return list(set([review.get_customer() for review in self.reviews()]))

    def average_star_rating(self):
        ratings = [review.get_rating() for review in self.reviews()]
        return sum(ratings) / len(ratings) if len(ratings) > 0 else 0


class Review:
    all_reviews_list = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews_list.append(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all_reviews(cls):
        return cls.all_reviews_list

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant


# Example Usage:
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
customer3 = Customer("Jane", "Sally")

restaurant1 = Restaurant("Awesome Burger Place")
restaurant2 = Restaurant("Fantastic Pizza Joint")

review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant2, 5)
review3 = customer3.add_review(restaurant1, 9)
print("All Customers:")
for customer in Customer.all():
    print(f"{customer.full_name()}")

print("\nAll Restaurants:")

for restaurant in Restaurant.all_restaurants:
    print(f"{restaurant.get_name()}")

print("\nReviews:")
for review in Review.all_reviews():
    print(f"Customer: {review.get_customer().full_name()}, Restaurant: {review.get_restaurant().get_name()}, Rating: {review.get_rating()}")


print(f"\nCustomer's full name is: {customer1.full_name()}\n")  # Output: John Doe

print(f"{customer1.full_name()} has {customer1.num_reviews()} review\n")  # Output: John Doe has 1 review


print(f"Average star rating for {restaurant1.get_name()} is: {restaurant1.average_star_rating()}\n")# Output: 6.5

found_customer = Customer.find_by_name("John Doe")
print(f"Customer found is {found_customer.full_name()}\n")  # Output: John Doe

customers_with_given_name = Customer.find_all_by_given_name("Jane")

for customer in customers_with_given_name:
    print(f"Customer with name Jane can be linked to:{customer.full_name()}\n")  # Output: Jane Smith , Jane Sally

