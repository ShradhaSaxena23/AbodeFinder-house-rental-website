

from django.db import models
from django.utils.text import slugify

class AddRentalHome(models.Model):
    # Max lengths based on typical form field sizes
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Street1 = models.CharField(max_length=30)
    Street2 = models.CharField(max_length=30, blank=True)  # Street2 can be optional
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Pincode = models.CharField(max_length=6)  # Assuming a 6-digit postal code
    Contact = models.CharField(max_length=13)  # To accommodate country codes and varying lengths
    Visiting_Start = models.TimeField()
    Visiting_End = models.TimeField()
    Gate_closing_time=models.TimeField(blank=True,null=True)
    Feature1=models.CharField(max_length=40 ,blank=True,null=True)
    Feature2=models.CharField(max_length=40,blank=True,null=True)
    # Define choices for days of the week
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'
    EVERYDAY = 'Everyday'

    DAY_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        (EVERYDAY, 'Everyday'),
    ]

    Visiting_day = models.CharField(max_length=9, choices=DAY_CHOICES, default=EVERYDAY)
    Rent = models.IntegerField()
    Number_Of_People_Allowed = models.IntegerField()
    Description = models.TextField(max_length=1000)  # Increased length for detailed descriptions
    Image = models.ImageField(null=True , upload_to='images/')  # Specify the upload directory
    slug = models.SlugField(unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.First_Name} {self.Last_Name} {self.City}")
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} - {self.City}"

# Make sure to add the following settings in your settings.py for media file handling
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
