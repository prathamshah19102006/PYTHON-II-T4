from django.contrib import admin
from django.urls import path,include
from app1.views import home,id,add,edit,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('id/<int:id>',id,name='id'),
    path('add',add,name='fac'),
    path('edit/<int:id>',edit,name='edit'),
    path('delete/<int:id>',delete,name='delete'),
]