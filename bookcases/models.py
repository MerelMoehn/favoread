from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# This status is used to reflect if the,
# bookcase owner has read the book already
READ_STATUS = ((0, "Not started"), (1, "Reading"), (2, "Read"))


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=1000, unique=True)
    author = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=50)
    featured_image = CloudinaryField('image', default='book_preview')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # Display books in descending order
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} by {self.author}"

    # auto generate slug based on title. Based on Youtube video Django World
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Bookcase_book(models.Model):
    bookcase_owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name="bookcase_owner")
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name="books")
    status = models.IntegerField(choices=READ_STATUS, default=0)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Display books in descending order
        ordering = ["-added_on"]

    def __str__(self):
        return f"{self.book} in {self.bookcase_owner}'s bookcase"
