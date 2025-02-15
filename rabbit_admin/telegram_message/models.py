from django.db import models
from django.utils.translation import gettext as _


class TelegramMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    project = models.ForeignKey(to='projects.Project', on_delete=models.CASCADE, verbose_name=_('Project'))
    enabled = models.BooleanField(verbose_name=_('Enabled'))
    bot_token = models.CharField(max_length=255, verbose_name=_('Bot API Token'))
    chat_id = models.CharField(max_length=255, verbose_name=_('Chat ID'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        db_table = 'telegram_messages'
        verbose_name = _('Telegram Message')
        verbose_name_plural = _('Telegram Messages')
        unique_together = 'name', 'project'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'
