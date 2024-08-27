from django.urls import path 
from.import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('save', views.save,name='save'),
    path('atualiza/<int:id>',views.atualiza,name='atualiza'),
    path('update',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]