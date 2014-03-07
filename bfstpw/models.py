from django.db import models
from django.db.models import Min, Max, Count

class ThreadManager(models.Manager):
    def sortByLastPost(self):
        return self.annotate(mostrecent=Max('forumpost__date_posted')).order_by('-mostrecent')

class ForumThread(models.Model):
    thread_title = models.CharField(max_length=40)

    objects = ThreadManager()

    def getOriginalPost(self):
        return self.forumpost_set.order_by('date_posted')[0]

    def getLatestPost(self):
        return self.forumpost_set.latest('date_posted')

    def get_absolute_url(self):
        return reverse('bfstpw-thread', args=[str(self.id)])

    def __unicode__(self):
        return self.thread_title

class ForumPost(models.Model):
    forumThread = models.ForeignKey(ForumThread)
    poster = models.CharField(max_length=25)
    message_body = models.TextField()
    date_posted = models.DateTimeField()

    def __unicode__(self):
        return self.poster+': "'+self.message_body[:6]+'..." at '+self.date_posted.__str__()
