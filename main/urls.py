from django.urls import path

from main.views import main_page_view, admin_page

urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('admin-page/', admin_page, name='admin_page'),
]
