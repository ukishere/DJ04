from django.db import models
# from django.db.models import TextChoices

# class PhoneChoices(TextChoices):
#     IPhone = 'iphone-x', 'Iphone X'
#     Samsung = 'samsung-galaxy-edge-2', 'Samsung Galaxy Edge 2'
#     Nokia = 'nokia-8', 'Nokia 8'

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    PHONE_MODEL_CHOICES=[
        ('iphone-x', 'Iphone X'),
        ('samsung-galaxy-edge-2', 'Samsung Galaxy Edge 2'),
        ('nokia-8', 'Nokia 8')
    ]
    slug = models.TextField(
        choices=PHONE_MODEL_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'Phones'