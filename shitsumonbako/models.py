from django.db import models

# Create your models here.
class Question(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    toUser = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE)
    #IPアドレス
    author = models.CharField(max_length=15)
    body = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, blank=True, default='')
    countReported = models.IntegerField(default=0)
    isPinned = models.BooleanField(default=False)
    isVisible = models.BooleanField(default=True)

    class Meta:
        ordering = ['createdAt']

    def report(self):
        self.countReported += 1
        if self.countReported > 10:
            self.isVisible = False
            #self.delete()
        self.save()