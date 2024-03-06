from django.db import models

# Create your models here.

# class Group(models.Model):
#     name = models.CharField(max_length=100)

# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     client_type = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
# class CompanyType(models.Model):
#     name = models.CharField(max_length=50)

class Administrator(models.Model):
    name = models.CharField(max_length=100)
    username =models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Telecaller(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Lead(models.Model):
    telecaller = models.ForeignKey(Telecaller, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=50)
    lead_status = models.CharField(max_length=50, default='pending')
    source = models.CharField(max_length=50)
    country = models.CharField(max_length=100) 
    name = models.CharField(max_length=100)  # From company or people based on the choice of type
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return f"{self.type} - {self.name}"

class Status(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default='default_color_value')

# class Offers(models.Model):
#     lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
#     number = models.CharField(max_length=100, unique=True)
#     year = models.PositiveIntegerField()
#     status = models.CharField(max_length=50)
#     note = models.TextField()
#     current_date = models.DateField()
#     expire_date = models.DateField()

#     def __str__(self):
#         return f"Offer {self.number}"


    
