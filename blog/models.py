from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# WEIGHT_CHOICES = {
#     ('Choose Weight', '---'),
#     ('101 lbs', '101'),
#     ('109 lbs', '109'),
#     ('116 lbs', '116'),
#     ('123 lbs', '123'),
#     ('125 lbs', '125'),
#     ('130 lbs', '130'),
#     ('133 lbs', '133'),
#     ('136 lbs', '136'),
#     ('141 lbs', '141'),
#     ('143 lbs', '143'),
#     ('149 lbs', '149'),
#     ('155 lbs', '155'),
#     ('157 lbs', '157'),
#     ('165 lbs', '165'),
#     ('170 lbs', '170'),
#     ('174 lbs', '174'),
#     ('184 lbs', '184'),
#     ('191 lbs', '191'),
#     ('197 lbs', '197'),
#     ('285 lbs', '285'),
# }


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # weight = models.CharField(
    #     max_length=20, choices=WEIGHT_CHOICES, default='---')

    def __str__(self):
        return self.title
