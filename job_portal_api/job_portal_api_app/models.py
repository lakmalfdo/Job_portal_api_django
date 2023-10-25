from django.db import models

class User(models.Model):
    UserRoleChoices = (
        ('Employer', 'Employer'),
        ('Job Seeker', 'Job Seeker'),
    )

    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    UserRole = models.CharField(max_length=50, choices=UserRoleChoices)
    ProfilePicture = models.CharField(max_length=255, blank=True, null=True)
    AuthenticationToken = models.CharField(max_length=255, blank=True, null=True)

class Employer(models.Model):
    EmployerID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    CompanyDescription = models.TextField(blank=True, null=True)
    CompanyLogo = models.CharField(max_length=255, blank=True, null=True)

class JobSeeker(models.Model):
    JobSeekerID = models.AutoField(primary_key=True)
    Resume = models.CharField(max_length=255)
    CoverLetter = models.CharField(max_length=255)

class JobListing(models.Model):
    ApplicationStatusChoices = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Filled', 'Filled'),
        ('Other', 'Other'),
    )

    JobID = models.AutoField(primary_key=True)
    EmployerID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=255)
    JobDescription = models.TextField()
    JobRequirements = models.TextField(blank=True, null=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Location = models.CharField(max_length=255)
    ApplicationDeadline = models.DateField()
    ApplicationStatus = models.CharField(max_length=50, choices=ApplicationStatusChoices)

class Application(models.Model):
    ApplicationStatusChoices = (
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
        ('Other', 'Other'),
    )

    ApplicationID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    JobSeekerID = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    ApplicationStatus = models.CharField(max_length=50, choices=ApplicationStatusChoices)
    ApplicationDate = models.DateField()
    AttachedDocuments = models.CharField(max_length=255)
    Comments = models.TextField()

class Skill(models.Model):
    SkillID = models.AutoField(primary_key=True)
    SkillName = models.CharField(max_length=255)
    SkillDescription = models.TextField(blank=True, null=True)

class JobSeekerSkill(models.Model):
    ProficiencyLevelChoices = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    JobSeekerSkillID = models.AutoField(primary_key=True)
    JobSeekerID = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    SkillID = models.ForeignKey(Skill, on_delete=models.CASCADE)
    ProficiencyLevel = models.CharField(max_length=50, choices=ProficiencyLevelChoices)
    
class EmployersJobListing(models.Model):
    EmployersJobListingID = models.AutoField(primary_key=True)
    EmployerID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    JobID = models.ForeignKey(JobListing, on_delete=models.CASCADE)

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)
    CategoryDescription = models.TextField(blank=True, null=True)

class JobCategoryMapping(models.Model):
    JobCategoryMappingID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)

class Message(models.Model):
    MessageID = models.AutoField(primary_key=True)
    SenderID = models.ForeignKey(User, on_delete=models.CASCADE)
    ReceiverID = models.ForeignKey(User, on_delete=models.CASCADE)
    MessageContent = models.TextField()
    Timestamp = models.DateTimeField()

class Notification(models.Model):
    NotificationID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    NotificationContent = models.TextField()
    NotificationType = models.CharField(max_length=255)
    Timestamp = models.DateTimeField()
