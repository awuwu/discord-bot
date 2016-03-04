from django.db import models
from django.utils.translation import ugettext_lazy as _


class LoggedMessage(models.Model):

    discord_id = models.CharField(max_length=50, unique=True)

    member = models.ForeignKey('users.Member', related_name='messages_authored')
    member_username = models.CharField(max_length=255)  # this can change, only the member.discord_id is a constant

    channel = models.ForeignKey('channels.Channel')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited_timestamp = models.DateTimeField(null=True, blank=True)

    mentions = models.ManyToManyField('users.Member', related_name='messages_mentioned_in', blank=True)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ['-timestamp']

    def __str__(self):
        return self.discord_id
