from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job_portal_api_app.views import UserViewSet, EmployerViewSet, JobSeekerViewSet, JobListingViewSet, ApplicationViewSet, SkillViewSet, JobSeekerSkillViewSet, EmployersJobListingViewSet, CategoryViewSet, JobCategoryMappingViewSet, MessageViewSet, NotificationViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'jobseekers', JobSeekerViewSet)
router.register(r'joblistings', JobListingViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'jobseekerskills', JobSeekerSkillViewSet)
router.register(r'employersjoblistings', EmployersJobListingViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'jobcategorymappings', JobCategoryMappingViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'notifications', NotificationViewSet)

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
]

# Optionally, add a custom authentication URL pattern or other URL patterns as needed
# For example, you can add authentication endpoints using Django Rest Framework's default authentication views
# from rest_framework.authtoken import views
# urlpatterns += [
#     path('api-token-auth/', views.obtain_auth_token)
# ]
