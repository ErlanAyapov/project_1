from django.urls import path
from .views import authentication, logout, register, user_customer, UserProfile, UserUpdate

urlpatterns = [
	path('', authentication, name = 'members'),
	path('шығу/', logout, name = 'logout'),
	path('тіркеу/', register, name = 'register'),
	path('тіркеу/<int:pk>/', user_customer, name = 'user_customer'),
	path('профиль/<int:pk>/', UserProfile.as_view(), name = 'user_profile'),
	path('өзгерту/<int:pk>/', UserUpdate.as_view(), name = 'user_update'),
]