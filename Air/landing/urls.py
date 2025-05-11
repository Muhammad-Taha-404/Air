from . import views
from django.urls import path

urlpatterns = [
    
    path("",views.landing1,name="landing1"),
    path('booking/',views.Booking_,name="booking"),
    path('book/',views.Book,name='book'),
    path('404/',views.pg_404,name="404"),
    path('mybookings/',views.mybookings,name="mybookings"),
    path('success/',views.success,name='success'),
    path('nobooks/',views.nobooks,name="nobooks")

]