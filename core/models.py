from django.db import models


class HealthCheck(models.Model):
    """Placeholder model to exercise migrations in Day 3."""

    checked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-checked_at"]
