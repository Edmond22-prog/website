from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    localisation = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    background_pic = models.ImageField(blank=True, null=True, upload_to="images/background/")
    twitter_link = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)
    github_link = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.surname + " " + self.name


class Skill(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    skill_svg = models.ImageField(blank=True, null=True, upload_to="images/skills/")

    def __str__(self):
        return self.title


class Education(models.Model):
    diploma = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.IntegerField(null=False, blank=True)
    end_year = models.IntegerField(null=False, blank=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.diploma


class Experience(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True)
    experience_start = models.CharField(max_length=255, blank=True, null=True)
    experience_end = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.role


class Community(models.Model):
    community_role = models.CharField(max_length=255, blank=True, null=True)
    community_start = models.CharField(max_length=255, blank=True, null=True)
    community_end = models.CharField(max_length=255, blank=True, null=True)
    structure = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.community_role


class ItemPortfolio(models.Model):
    category = models.CharField(max_length=255, choices=[("Application", "Application"), ("Web", "Web")], null=False, default="Application")
    client = models.CharField(max_length=255, blank=True, null=True)
    project_link = models.CharField(max_length=255, blank=True, null=True)
    project_pic_1 = models.ImageField(blank=True, null=False, upload_to="images/portfolio/")
    project_pic_2 = models.ImageField(blank=True, null=True, upload_to="images/portfolio/")
    project_pic_3 = models.ImageField(blank=True, null=True, upload_to="images/portfolio/")
    detail = models.TextField()

    def __str__(self):
        return self.project_link + " || " + self.category
