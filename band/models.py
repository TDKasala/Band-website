from django.db import models

class Album(models.Model):
    
    """
    Model representing an album.
    
    Attributes:
        title (str): The title of the album.
        release_date (DateField): The release date of the album.
    """
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

class Song(models.Model):
    
    """
    Model representing a song.
    
    Attributes:
        title (str): The title of the song.
        album (Album): The album to which the song belongs (foreign key relationship).
        duration (DurationField): The duration of the song.
    """
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Concert_list(models.Model):
    
    """
    Model representing a concert in a list.
    
    Attributes:
        title (str): The title or name of the concert.
        date (DateField): The date of the concert.
        location (str): The location where the concert will be held.
        ticket_price (DecimalField): The ticket price for the concert.
    """
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.title

    
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name


class ExclusiveContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
