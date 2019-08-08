from django.db import models

# Create your models here.

OUTGO_OR_INCOME = ((True, 'outgo'), (False, 'income'))
GENRES = (('food', 'food'), ('other', 'other'))


class ExpenseModel(models.Model):
    datetime = models.DateTimeField()
    name = models.CharField(max_length=20)
    is_outgo = models.BooleanField(
        choices=OUTGO_OR_INCOME
    )
    amount = models.PositiveIntegerField()
    genre = models.CharField(
        max_length=50,
        choices=GENRES
    )
    memo = models.TextField()

    def __str__(self):
        return self.name
