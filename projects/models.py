from django.db import models

# Create your models here.

class MemberActive(models.Manager):
    def active(self):
        return self.filter(active=True)


class Member(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    SPECIALITY_CHOICES = (
        ('GIT/GITHUB', 'Git/Github'),
        ('SHELL', 'Shell'),
        ('EMACS', 'Emacs'),
        ('VI', 'Vi'),
        ('C', 'C'),
        ('PYTHON', 'Python'),

    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    speciality = models.CharField(choices=SPECIALITY_CHOICES, max_length=10)
    active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = MemberActive()
class ProfileImage(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="profile_images")
    image = models.ImageField(upload_to="profile-images")

class SpecialityTags(models.Model):
    member = models.ManyToManyField(Member, blank=True)
    name = models.CharField(max_length=100)