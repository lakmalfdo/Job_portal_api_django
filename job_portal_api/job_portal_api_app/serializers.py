from rest_framework import serializers
from .models import User, Employer, JobSeeker, JobListing, Application, Skill, JobSeekerSkill, EmployersJobListing, Category, JobCategoryMapping, Message, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class JobSeekerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerSkill
        fields = '__all__'

class EmployersJobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployersJobListing
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class JobCategoryMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategoryMapping
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
