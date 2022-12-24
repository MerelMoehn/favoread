from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

READ_STATUS = ((0, "Still to Read"), (1, "Reading"), (2, "Read"))


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=1000, unique=True)
    author = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=50)
    featured_image = CloudinaryField('image', default='book_preview')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    # auto generate slug based on title. Based on Youtube video Django World
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Bookcase(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookcase")
    slug = models.SlugField(max_length=200, unique=True)
    likes = models.ManyToManyField(User, related_name="bookcase_like", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}'s bookcase"

    def number_of_likes(self):
        return self.likes.count()

    # auto generate slug based on title. Based on Youtube video Django World
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.owner)
        return super().save(*args, **kwargs)


class Bookcase_book(models.Model):
    bookcase_id = models.ForeignKey(Bookcase, on_delete=models.CASCADE, related_name="bookcase_books")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    status = models.IntegerField(choices=READ_STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.book_id} in {self.bookcase_id}"
