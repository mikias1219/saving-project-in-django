from django.contrib.auth.models import User
from django.db import models

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_admin = models.BooleanField(default=False)
    def total_savings(self):
        return sum(s.amount for s in self.saving_set.filter(is_paid=True))

class Saving(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    is_paid = models.BooleanField(default=False)
