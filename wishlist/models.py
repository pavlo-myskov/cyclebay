from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from products.models import Product


class Wishlist(models.Model):
    """
    A Wishlist model for maintaining a list of favorite products
    """
    # ensures that each user can only have one wishlist
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    # User can add many products to their wishlist,
    # and each product can be added to many wishlists
    products = models.ManyToManyField(
        Product,
        related_name='wishlists',
    )

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=get_user_model())
def create_wishlist(sender, instance, created, raw=False, **kwargs):
    """
    Create a wishlist for each new user using the post_save signal
    """
    if raw:
        return
    if created:
        Wishlist.objects.create(user=instance)
