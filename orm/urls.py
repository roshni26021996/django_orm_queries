from django.urls import path
from .views import all_orm_queries, insert_create_queries, update_queries, delete_queries

urlpatterns = [ 
    path('queries/', all_orm_queries, name='orm'),
    path('queries/create/', insert_create_queries, name='orm_create'),
    path('queries/update/', update_queries, name='orm_update'),
    path('queries/delete/', delete_queries, name='orm_delete')
]
