from django.urls import path
from . import views
from .views import MemberListView,MemberCreateView,MemberUpdateView,MemberDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.main,name='main'),
    # path('members/', views.members, name='members'),
    path('members/details/<int:id>',views.details,name='details'),
    path('testing/',views.testing, name='testing'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('register/', views.register, name='register'),
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/create/', MemberCreateView.as_view(), name='create_member'),
    path('members/<int:pk>/update/', MemberUpdateView.as_view(), name='update_member'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='delete_member'),
    path('send-email/', views.send_email_view, name='send_email_view'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # scores path
    path('score_form/', views.score_form, name='score_form'),
    path('score_results/', views.score_results, name='score_results'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
