from django.urls import path
from . import views

app_name = 'lab'

urlpatterns = [
    path('labs/', views.LabListView.as_view(), name='lab-list'),
    path('labs/create/', views.LabCreateView.as_view(), name='lab-create'),
    path('labs/<int:pk>/update/', views.UpdateLabView.as_view(), name='lab-update'),
    path('labs/<int:pk>/delete/', views.DeleteLabView.as_view(), name='lab-delete'),
    
    path('labs/<int:pk>/items/add-item/', views.CreateItemView.as_view(), name='add-item'),
    path('labs/<int:pk>/items/', views.ItemListView.as_view(), name='item-list'),
    path('labs/<int:pk>/items/<int:item_id>/update/', views.ItemUpdateView.as_view(), name='item-update'),
    path('labs/<int:pk>/items/<int:item_id>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    
    path('labs/<int:pk>/groups/create/', views.GroupCreateView.as_view(), name='create-group'),
    path('labs/<int:pk>/groups/', views.GroupListView.as_view(), name='group-list'),
    path('labs/<int:pk>/groups/<int:group>/', views.GroupDetailView.as_view(), name='group-detail'),
    path('labs/<int:pk>/groups/<int:group>/delete/', views.GroupDeleteView.as_view(), name='group-delete'),
    
    path('labs/<int:pk>/groups/<int:group>/add-item/', views.GroupItemCreateView.as_view(), name='add-group-item'),
    path('labs/<int:pk>/groups/<int:group>/delete-item/<int:group_item>/', views.GroupItemDeleteView.as_view(), name='delete-group-item'),
    path('labs/<int:pk>/groups/<int:group>/update-item/<int:group_item>/', views.GroupItemUpdateView.as_view(), name='update-group-item'),
    
    path('labs/<int:pk>/categories/', views.CategoryListView.as_view(), name='category-list'),
    path('labs/<int:pk>/categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('labs/<int:pk>/categories/delete/<int:category>/', views.CategoryDeleteView.as_view(), name='category-delete'),
]

