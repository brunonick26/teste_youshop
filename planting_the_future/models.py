from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    # Model representing an account which can have multiple users
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='accounts')

class Profile(models.Model):
    # Model representing a profile with additional information for a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)

class Tree(models.Model):
    # Model representing a tree
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

class PlantedTree(models.Model):
    # Model representing a tree planted by a user
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planted_trees')
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='planted_trees')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='planted_trees')
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6)

    @property
    def location(self):
        # Returns the location of the planted tree as a tuple (latitude, longitude)
        return (self.location_lat, self.location_lon)

    @location.setter
    def location(self, value):
        # Sets the location of the planted tree using a tuple (latitude, longitude)
        self.location_lat, self.location_lon = value
