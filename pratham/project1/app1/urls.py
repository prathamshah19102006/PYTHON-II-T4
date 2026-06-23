from django.contrib import admin
from django.urls import path,include
from app1.views import home,id,add
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('id/<int:id>',id,name='id'),
    path('add',add,name='fac'),
]