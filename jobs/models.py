from django.db import models

from companies.models import Company


# Create your models here.
class Job(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('IN', 'Internship'),
    ]

    EXPERIENCE_LEVEL_CHOICES = [
        ('JR', 'Junior'),
        ('MD', 'Mid'),
        ('SR', 'Senior'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField(blank=True)

    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    employment_type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPE_CHOICES
    )

    working_hours = models.CharField(max_length=100, blank=True)
    weekly_hours = models.PositiveIntegerField(null=True, blank=True)
    remote_option = models.CharField(max_length=20, default='on-site')

    experience_level = models.CharField(
        max_length=2,
        choices=EXPERIENCE_LEVEL_CHOICES
    )
    years_of_experience = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    posted_date = models.DateField(auto_now_add=True)
    closing_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title
