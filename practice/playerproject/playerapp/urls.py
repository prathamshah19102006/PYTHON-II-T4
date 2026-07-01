from django.contrib import admin
from django.urls import path,include
from playerapp.views import home,welcome,addplayer,id,edit,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('playerapp.urls'))
path('home/',home,name='home'),
path('welcome/',welcome,name='welcome'),
path('add/',addplayer,name='add'),
path('id/<int:id>',id,name='id'),
path('edit/<int:id>',edit,name='edit'),
path('delete/<int:id>',delete,name='delete')
]