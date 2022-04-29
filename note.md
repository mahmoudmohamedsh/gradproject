[JWT](#jwt-token)
    






# user model
[Learn Django - Build a Custom User Model with Extended Fields](https://www.youtube.com/watch?v=Ae7nc1EGv-A)

    - make the custom user model
    - make good design for manage screen after login as admin

-------------
## img upload

[Image File Upload to User Profile Model | Django (3.0) Crash Course Tutorials (pt 17)](https://www.youtube.com/watch?v=aNk2CAkHvlE)



```bash
pip install django
pip install djangorestframework
django-admin startproject studentsapp 
cd studentsapp
django-admin startapp userapp
```

in main app go to settings.py file add to the list

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```bash
python manage.py migrate
# We'll also create an initial user named admin with a password of password123
# that if use the default user login not the custom you create
python manage.py createsuperuser --email admin@example.com --username admin
```

# start of the video which handle upload image

```python
## define media file path
import os
MEDIA_ROOT  = os.path.join(BASE_DIR,'media') 
MEDIA_URL   = '/media/'
```


```python
## in url 
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns =[
    path('/create/',)
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )

## in model
# save the img functions
def uploat_to(instance , filename):
    return 'users/{filename}'.format(filename=filename)


```




# JWT Token

#### video
[Django Rest Framework Series - JWT Token Authentication with React - Part-3](https://www.youtube.com/watch?v=AfYfvjP1hK8&list=PLOLrQ9Pn6caw0PjVwymNc64NkUNbZlhFw&index=8)


