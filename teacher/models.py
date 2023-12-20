from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class teacher_model(User):
    teacher_id = models.PositiveIntegerField()
    phone_number = models.PositiveBigIntegerField()
    year_of_experience = models.PositiveSmallIntegerField()
    payment = models.PositiveSmallIntegerField(null=True, default=0)
    gender = models.CharField(
        max_length=10,
        choices=[["Male", "Male"], ["Female", "Female"], ["Others", "Others"]],
    )


class domain_model(models.Model):
    did = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.domain_name


class course_model(models.Model):
    did = models.ForeignKey(domain_model, on_delete=models.CASCADE)
    cid = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField(default=11)
    course_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    price = models.BigIntegerField(default=1000)
    image = models.ImageField()

    def __str__(self):
        return self.course_name


class course_video_model(models.Model):
    cid = models.ForeignKey(course_model, on_delete=models.CASCADE)
    vid = models.AutoField(primary_key=True)
    tid = models.PositiveSmallIntegerField(default=11)
    v_title = models.CharField(max_length=20)
    v_text = models.CharField(max_length=300)


class chat_model(models.Model):
    sid = models.PositiveBigIntegerField()
    tid = models.PositiveBigIntegerField()
    course_id = models.PositiveBigIntegerField(default=0)
    schat = models.CharField(max_length=512)
    tchat = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now=True)
    simage = models.ImageField(upload_to="chat_images/", null=True)
    timage = models.ImageField(upload_to="chat_images/", null=True)
    sfile = models.FileField(upload_to="chat_Docs/", null=True)
    tfile = models.FileField(upload_to="chat_Docs/", null=True)
