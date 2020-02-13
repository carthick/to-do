from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<item_id>', views.delete_task, name='delete_task'),
    path('edit/<item_id>', views.edit_task, name='edit_task'),
    path('status/<item_id>/<status_flag>', views.update_status, name='update_status'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
