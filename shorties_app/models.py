from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')  # Stored in S3
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title