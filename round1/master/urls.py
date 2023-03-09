from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
                  path('', home),
                  path('master/signin', signin),
                  path('master/signup', signup),
                  path('master/dashboard', dashboard),
                  path('master/profile', profile),
                  path('master/logout', signout),
                  path('master/task/create', create_task),
                  path('master/task/submitted', submitted_tasks),
                  path('master/task/evaluated', evaluated_task)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
