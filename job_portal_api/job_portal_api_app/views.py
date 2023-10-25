# job_api/views.py
from rest_framework import viewsets
from .models import User, Employer, JobSeeker, JobListing, Application, Skill, JobSeekerSkill, EmployersJobListing, Category, JobCategoryMapping, Message, Notification
from .serializers import UserSerializer, EmployerSerializer, JobSeekerSerializer, JobListingSerializer, ApplicationSerializer, SkillSerializer, JobSeekerSkillSerializer, EmployersJobListingSerializer, CategorySerializer, JobCategoryMappingSerializer, MessageSerializer, NotificationSerializer

# User viewset for CRUD operations on the User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Employer viewset for CRUD operations on the Employer model
class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

# JobSeeker viewset for CRUD operations on the JobSeeker model
class JobSeekerViewSet(viewsets.ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer

# JobListing viewset for CRUD operations on the JobListing model
class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer

# Application viewset for CRUD operations on the Application model
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# Skill viewset for CRUD operations on the Skill model
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# JobSeekerSkill viewset for CRUD operations on the JobSeekerSkill model
class JobSeekerSkillViewSet(viewsets.ModelViewSet):
    queryset = JobSeekerSkill.objects.all()
    serializer_class = JobSeekerSkillSerializer

# EmployersJobListing viewset for CRUD operations on the EmployersJobListing model
class EmployersJobListingViewSet(viewsets.ModelViewSet):
    queryset = EmployersJobListing.objects.all()
    serializer_class = EmployersJobListingSerializer

# Category viewset for CRUD operations on the Category model
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# JobCategoryMapping viewset for CRUD operations on the JobCategoryMapping model
class JobCategoryMappingViewSet(viewsets.ModelViewSet):
    queryset = JobCategoryMapping.objects.all()
    serializer_class = JobCategoryMappingSerializer

# Message viewset for CRUD operations on the Message model
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# Notification viewset for CRUD operations on the Notification model
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
