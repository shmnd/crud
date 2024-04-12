from django.urls import path
from .  import views
urlpatterns = [
  path('',views.show,name='show'),
  path('add/',views.add,name='add'),
  path('addrec/',views.addrec,name='addrec'),
  path('delrec/<int:id>/',views.delrec,name='delrec'),
  path('update/<int:id>',views.update,name='update'),
  path('uprec/<int:id>/',views.uprec,name='uprec'),
]

# hiii