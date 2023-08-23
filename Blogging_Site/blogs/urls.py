from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('blog',views.blogcls),
router.register('anonblog',views.bloganon)

urlpatterns = [
    path('home/',views.home),
    path('',include(router.urls)),
    path('delete/<int:pk>/',views.dltobj.as_view()),
    path('update/<int:pk>/',views.updateobj.as_view()),
    path('getblog/',views.getblog),
     path('signup',views.signup.as_view()),
    path('login',views.login.as_view()),
    path('logout',views.logout.as_view()),
]
