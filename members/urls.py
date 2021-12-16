from django.urls import path
from .views import UserRegisterFinishView, pic_update, UserList, authentication, progress_save, logout, register, user_customer, UserProgressDetail, UserProfile, UserUpdate

urlpatterns = [
	path('', authentication, name = 'members'),
	path('logout/', logout, name = 'logout'),
	path('register/', register, name = 'register'),
	path('register/<int:pk>/', user_customer, name = 'user_customer'),
	path('profile/<int:pk>/', UserProfile.as_view(), name = 'user_profile'),
	# path('update/<int:pk>/', UpdateCustomerView.as_view(), name = 'user_update'),
	path('picture/<int:pk>/', pic_update, name = 'user_picture_update'),
	path('save-progress/<int:pk>/', progress_save, name = 'progress_save'),
	path('answers/<int:pk>/', UserProgressDetail.as_view(), name = 'user_progress'),
	path('users/', UserList.as_view(), name = 'users'),
	path('register/continue/<int:pk>', UserRegisterFinishView.as_view(), name = 'register_continu'),
]