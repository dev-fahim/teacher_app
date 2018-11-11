from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class UserTeacherModel(models.Model):
    B_DEGREE_CHOICES = (
        ('bsc', 'BSC'),
        ('bba', 'BBA'),
        ('ba', 'BA')
    )
    M_DEGREE_CHOICES = (
        ('msc', 'MSC'),
        ('mba', 'MBA'),
        ('ma', 'MA')
    )
    GROUP_CHOICES = (
        ('science', 'Science'),
        ('business_studies', 'Business Studies'),
        ('arts', 'Arts')
    )
    SUBJECT_CHOICES = (
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('gen_math', 'General Mathematics'),
        ('higher_math', 'Higher Mathematics'),
    )
    """
    Personal information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_teacher')
    birth_date = models.DateField(blank=True)
    present_address = models.TextField(blank=False, default='Not provided')
    permanent_address = models.TextField(blank=False, default='Not provided')

    """
    Education status
    """
    b_year = models.IntegerField()
    b_institute = models.CharField(max_length=100)
    b_degree = models.CharField(choices=B_DEGREE_CHOICES, max_length=100)
    b_degree_sub = models.CharField(max_length=100)
    m_year = models.IntegerField()
    m_institute = models.CharField(max_length=100)
    m_degree = models.CharField(choices=M_DEGREE_CHOICES, max_length=100)
    m_degree_sub = models.CharField(max_length=100)
    is_phd = models.BooleanField(default=False)
    phd_year = models.IntegerField()
    phd_institute = models.CharField(max_length=100)
    phd_sub = models.CharField(max_length=100)

    """
    Subject
    """
    group = models.CharField(choices=GROUP_CHOICES)
    subject = models.CharField(choices=SUBJECT_CHOICES)


