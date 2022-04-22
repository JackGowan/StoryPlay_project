from . import views
from django.urls import path, include

app_name = "plates"
urlpatterns = [
    path('', views.home_page, name='homepage'),

    # Read Stories (published)
    path('finalplates', views.final_plates_title_show, name='final_plates_title_show'),
    path('finalplates/<int:pk>/', views.final_plates_content_show, name='final_plates_content_show'),

    # Long play
    path('longplay', views.longplay_page, name='longplaypage'),

    # Long_play-submenus:
    path('createplates', views.create_plates, name='create_plates'),

    path('draftplates', views.draft_plates_title_show, name='draft_plates_title_show'),
    path('draftplates/<int:pk>/', views.draft_plates_content_show, name='draft_plates_content_show'),
    path('draftplates/<int:pk>/adjustplates', views.draft_plates_add_text, name='draft_plates_add_text'),
    path('draftplates/<int:pk>/publishplates', views.draft_plates_publish, name='draft_plates_publish'),

    # Solo Play
    path('soloplay', views.soloplay_page, name='soloplaypage'),
    ]