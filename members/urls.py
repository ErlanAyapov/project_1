from django.urls import path
from .views import UserList, authentication, progress_save, logout, register, user_customer, UserProfile, UserUpdate, picture_update

urlpatterns = [
	path('', authentication, name = 'members'),
	path('шығу/', logout, name = 'logout'),
	path('тіркеу/', register, name = 'register'),
	path('тіркеу/<int:pk>/', user_customer, name = 'user_customer'),
	path('профиль/<int:pk>/', UserProfile.as_view(), name = 'user_profile'),
	path('өзгерту/<int:pk>/', UserUpdate.as_view(), name = 'user_update'),
	path('сурет/<int:pk>/', picture_update, name = 'picture_update'),
	path('прогресс-сақтау/<int:pk>', progress_save, name = 'progress_save'),
	path('қолданушылар/', UserList.as_view(), name = 'users'),

]