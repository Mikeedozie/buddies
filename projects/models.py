from django.db import models

# Create your models here.
#These are my models
class SpecialityTags(models.Model):
    SPECIALITY_CHOICES = (
        ('Git/Github', 'Git/Github'),
        ('Shell', 'Shell'),
        ('Emacs', 'Emacs'),
        ('VI', 'Vi'),
        ('C', 'C'),
        ('Python', 'Python'),
        ('Javascript', 'Javascript'),
        ('Flask', 'Flask'),
        ('MySQL', 'MySQL'),
        ('Node Js', 'Node Js'),

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
    image = models.ImageField(upload_to="profile-images", blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = MemberActive()
    
    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['date_joined']

class Topic(models.Model):
    topics = models.ForeignKey(SpecialityTags, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    subtopics = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.topics.speciality

class Quiz(models.Model):
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.topics.topics.speciality
    class Meta:
        verbose_name_plural = "Quizzes"

