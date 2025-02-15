from django.db import models
from django.utils.translation import gettext as _

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), unique=True)
    enabled = models.BooleanField(verbose_name=_('Enabled'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        db_table = 'projects'
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ['-created_at']

    def __str__(self):
        return self.name
