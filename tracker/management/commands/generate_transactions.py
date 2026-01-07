import random
# from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import Category, Transaction, User
from datetime import date, datetime, timedelta

class Command(BaseCommand):
    help = "Generates transactions fro testing"

    def generate_random_date(self, start_date, end_date):
            """
            Generates a random date between start_date and end_date (inclusive).
            """
            if start_date > end_date:
                raise ValueError("Start date cannot be after end date.")

            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days

            random_number_of_days = random.randrange(days_between_dates + 1) # +1 to include end_date

            random_date = start_date + timedelta(days=random_number_of_days)
            return random_date

             
             
    def handle(self, *arg, **options):
        # fake = Faker()
        # create categories
        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation"
        ]
        
        for category in categories:
            Category.objects.get_or_create(name=category)

        user = User.objects.filter(username="tshepiso").first()
        
        if not user:
            user = User.objects.create_superuser(username="tshepiso", password="****************")
            
        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
         # Example usage:
        start_dt = date(2024, 12, 1)
        end_dt = date(2025, 12, 10)

        
        for i in range(20):
            Transaction.objects.create(
                category = random.choice(categories),
                user = user,
                amount = random.uniform(1, 2500),
                date =  self.generate_random_date(start_dt, end_dt) ,
                type = random.choice(types)
            )
            
    