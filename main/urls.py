from django.urls import path
from .views import check_auth, signin, signup, create_loan_application, get_loan_application, get_loan_applications, update_loan_application

urlpatterns = [
    path('check-auth/', check_auth, name='check-auth'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('create-loan-application/', create_loan_application, name='create-loan-application'),
    path('get-loan-application/<str:pk>/', get_loan_application, name='get-loan-application'),
    path('get-loan-applications/', get_loan_applications, name='get-loan-applications'),
    path('update-loan-application/<str:pk>/', update_loan_application, name='update-loan-application'),
]
