from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
ITEM_LABEL = (
    ('on-sale', 'new'),
    ('pr-label1', 'hot'),
    ('pr-label2', 'sale'),
)

GENDER = (
    (0, 'Women'),
    (1, 'Men'),
)


class Item(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(choices=ITEM_LABEL, max_length=20)
    gender = models.IntegerField(choices=GENDER, max_length=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    image = models.ImageField(upload_to='pics')
    slug = models.SlugField()
    # colors
    # category
    description = models.TextField()
    stock = models.IntegerField(default=1)
    count_sold = models.IntegerField(default=0)
    # sizes
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on', '-added_on']

    def __str__(self):
        return self.name

    @property
    def get_price_percentage(self):
        if self.discount_price:
            return round((self.discount_price - self.price) / self.price * 100, 0)


class Review(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]
