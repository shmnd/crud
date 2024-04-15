from django.urls import path
from .  import views

urlpatterns = [
  path('',views.StudentsList.as_view(),name='stud_list'),
  # path('view/<int:pk>/',views.StudentsView.as_view(),name='stud_view'),
  path('add/',views.StudentCreate.as_view(),name='stud_new'),
  # path('view/<int:pk>/',views.StudentsView.as_view(),name='stud_view'),
  path('update/<int:pk>/',views.StudentUpdate.as_view(),name='stud_upd'),
  path('delete/<int:pk>/',views.StudentsDelete.as_view(),name='stud_del'), 
]


# urlpatterns = [
#   path('',views.show,name='show'),
#   path('add/',views.add,name='add'),
#   path('addrec/',views.addrec,name='addrec'),
#   path('delrec/<int:id>/',views.delrec,name='delrec'),
  
#   path('update/<int:id>',views.update,name='update'),
#   path('uprec/<int:id>/',views.uprec,name='uprec'),
# ]