from django.db import models

# Create your models here.
#These are my models
class SpecialityTags(models.Model):
    SPECIALITY_CHOICES = (
        ('GIT/GITHUB', 'Git/Github'),
        ('SHELL', 'Shell'),
        ('EMACS', 'Emacs'),
        ('VI', 'Vi'),
        ('C', 'C'),
        ('PYTHON', 'Python'),

    )
    speciality = models.CharField(choices=SPECIALITY_CHOICES, max_length=100)

    def __str__(self):
        return self.speciality
    class Meta:
        verbose_name_plural = "Speciality Tags"

class MemberActive(models.Manager):
    def active(self):
        return self.filter(active=True)


class Member(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    speciality = models.ManyToManyField(SpecialityTags, blank=True)
    active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = MemberActive()
    
    def __str__(self):
        return self.name

class ProfileImage(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="profile_images")
    image = models.ImageField(upload_to="profile-images")

