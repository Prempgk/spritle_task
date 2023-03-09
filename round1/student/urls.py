from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
                  path('student/signin', signin),
                  path('student/signup', signup),
                  path('student/dashboard', dashboard),
                  path('student/logout', signout),
                  path('student/tasks', tasks),
                  path('student/tasks/solved', solved_tasks),
                  path('student/profile', profile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
