from django.db import models

# Does not matter what database you use, the code here will be the same.

# Always makemigrations and migrate when making changes to the database

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    earning_date = models.DateField()  # Stores the date of earning (No time needed, only the date)
    cash_sale = models.DecimalField(max_digits=10, decimal_places=2)  # For handling cash sale amounts, with two decimal places
    NMS_num = models.IntegerField()  # For numerical values of NMS numbers (Assumed to be integer values)
    NMS_earning = models.DecimalField(max_digits=10, decimal_places=2)  # For NMS earnings, with two decimal places
    flu_vacc_num = models.IntegerField()  # For numerical values of flu vaccine numbers (Assumed to be integer values)
    flu_earning = models.DecimalField(max_digits=10, decimal_places=2)  # For flu earnings, with two decimal places
    covid_vacc_num = models.IntegerField()  # For numerical values of COVID vaccine numbers (Assumed to be integer values)
    covid_earning = models.DecimalField(max_digits=10, decimal_places=2)

    # This method defines how instances of the Record model are displayed in the django
    # admin panel
    def __str__(self):
        return (f"Record on {self.earning_date}")

