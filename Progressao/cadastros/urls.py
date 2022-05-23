from django.urls import path

from .views import AtividadeList, CampoCreate, AtividadeCreate, CampoList, CampoUpdate, AtividadeUpdate, CampoDelete, AtividadeDelete

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name='nome_da_url'),
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('atualizar/campo/<int:pk>/', CampoUpdate.as_view(), name="atualizar-campo"),
    path('atualizar/atividade/<int:pk>', AtividadeUpdate.as_view(), name="atualizar-atividade"),
    path('excluir/campo/<int:pk>', CampoDelete.as_view(), name='deletar-campo'),
    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name="deletar-atividade"),
    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),
]