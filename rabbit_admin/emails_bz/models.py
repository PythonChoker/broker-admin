from django.db import models
from django.utils.translation import gettext as _


class EmailBZ(models.Model):
    project = models.ForeignKey(to='projects.Project', on_delete=models.CASCADE, verbose_name=_('Project'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'))
    email_from = models.EmailField(verbose_name=_('E-mail from'))
    email_to = models.EmailField(verbose_name=_('E-mail to'))
    api_key = models.CharField(max_length=255, verbose_name=_('API Key'))
    enabled = models.BooleanField(verbose_name=_('Enabled'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        db_table = 'emails_bz'
        verbose_name = _('SMTP BZ')
        verbose_name_plural = _('SMTP BZ')
        ordering = ['-created_at']

    def __str__(self):
        return self.email_to
