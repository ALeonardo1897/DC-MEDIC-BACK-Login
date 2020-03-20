from django.db import models

class MedicBaseClass(models.Model):

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        'modified_at',
        auto_now=True
    )

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created','-modified']