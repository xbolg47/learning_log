from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the entry."""
        if len(self.text) > 50:
            # Return the first 50 characters of the text followed by an ellipsis
            return f"{self.text[:50]}..."
        else:
            # Return the full text if it's 50 characters or less
            return self.text
