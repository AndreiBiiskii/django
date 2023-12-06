from django.urls import path

from school.views import students_list, teacher_list

urlpatterns = [
    path('', students_list, name='students'),
    path('teachers/', teacher_list, name='teachers'),
]
