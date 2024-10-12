from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # creates 'videos' folder in S3 where all videos will be uploaded
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    # when a Video object is printed it will return the 'title' of the video
    def __str__(self):
        return self.title