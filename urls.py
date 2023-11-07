from django.contrib import admin
from django.urls import path

from DjangoApplication import views

urlpatterns = [
    path('ZeroERR/',views.goZero,name='Zero'),
    path('admin/', admin.site.urls),
    path('',views.goHomePage,name='Form1'),
    path('CourseDescription/',views.goCourseTab,name='courseTable'),
    path('Visible/<int:user_ID>',views.errFunc,name='Err404')
]