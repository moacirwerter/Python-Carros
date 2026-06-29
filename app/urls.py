
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #Internet 04/06 Forma mais segura de importar views de autenticação
#from cars.views import cars_view, new_car_view , CarsView # Corrigindo erro de retorno do logon
from accounts.views import register_view,login_view #CarsView eu importo a simplificacao feita em views, na pasta cars.
from django.contrib.auth.views import LogoutView # internet 23/06
#from cars.views import new_car_view, CarsView, home_view # Remocao d via solicitacao suporte IA
#from django.contrib.auth.views import logout_view # Suporte curso IA
#from cars.views import cars_view, new_car_view, CarsView => removido cars_view devido a simplificacao
#from cars.views import new_car_view, CarsView ,home_view, NewCarView # NewCarView, usado,devido a simplificacao,feita em views

#NEWCarView usada,devido a simplificacao do codigo
#from cars.views import  CarsView ,home_view, NewCarView # INTERNET. Foi desativada a linha que tem CarsView,pois vai ser usada a CarListView. 
# CarListView usada por ter sido adicionado em views, tendo como objetivo, ser mais especifica na sua funcao.
#from cars.views import NewCarView, CarsListView # Tirei o home_view, 27/05, nao interferiu em nada. NewcarView foi retirada,devido a 
#simplificacao NewcarCreateView,conforme imagem abaixo.
from cars.views import  CarsListView,NewCarCreateView,CarDetailView, CarUpdateView, CarDeleteView
#from django.urls import reverse_lazy # Suporte curso IA
#from django.contrib.auth import views as auth_views # INTERNET
#from django.contrib.auth.views import LogoutView # suporte do curso IA
#from cars import views # internet
# O car list foi usado para se comunicar com
#cars.html
# Login_view deve ser criado também na views, porque ele necessita de autenticacao
#from cars.views import cars_view, new_car_view ,retirado da internet
urlpatterns = [
    #path('', home_view, name='home'), # SUPORTE IA, desativado,devido um erro 27/05
    #path('', CarsView.as_view, name='home'), # INTERNET , não interferiu em nada
    path('admin/', admin.site.urls),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    #path('cars/',cars_view,name='cars_list'),# AULA, desativada,devido a simplificaçao.
    # Quando eu chamei CarsView, ele chama uma classe, neste caso preciso informar que uma view, eu preciso
    # informar que é uma view, usando=> .as_view()
    #path('cars/', CarsView.as_view(),name='cars_list'), #Foi desativada, pois foi trocada para CarListView. Foi usada anteriormente ,devido a simplificacao feita em views, na pasta cars.
    #path('cars/',cars_view,name='car_list'),# INTERNET
    path('cars/', CarsListView.as_view(),name='cars_list'),

    #path('carros/', views.car_list_view, name='car_list'),#internet
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),# INTERNET
    #path('logout/', CustomLogoutView.as_view(), name='logout'), # Suporte curso IA
    #path('logout/', LogoutView.as_view(), name='logout') # Suporte do curso IA
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),# Suporte curso IA
    #path('logout/', logout_view, name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),# internet 23/05, deu certo, porem volta para o logon
    #path('logout/', LogoutView.as_view(next_page='cars_list'), name='logout') # Suporte IA
    #path('', home_view, name='home') # Suporte IA
    #path('new_car/',new_car_view, name='new_car'),# new_car_view ,desativado,devido a simplificacao feita em new_car_view, na aba views
    #Sempre que for uma classe,vai usar .as_view
    #path('new_car/',NewCarView.as_view(), name='new_car') # NewCarView.as_view(), usado devido a simplificacao,feita na pasta cars.
    #Foi retirada a linha acima, NewCarView,devido mais uma vez a simplificação e objetividade, foi substituido por NewCarCreateView
    path('new_car/',NewCarCreateView.as_view(), name='new_car'),
    
    path('car/<int:pk>/',CarDetailView.as_view(),name='car_detail'), # Usado devido a a criacao de DEtail
    #  car/<int:pk>/': Define o padrão da URL. A tag <int:pk> captura um número inteiro na URL e o armazena na variável pk
    #  (PK-Primary Key - Chave Primária). Ex: /car/5/ fará com que pk = 5
    #------
    #CarDetailView.as_view(): Converte a classe baseada em view (DetailView) em uma função executável, pronta para lidar com a requisição HTTP. 
    # A view usará a variável pk fornecida para buscar o carro no banco de dados
    #---
    #name='car_detail': Atribui um nome à rota. Isso é essencial para referenciar a URL em arquivos HTML ou redirecionamentos em Python usando {% url 'car_detail' car.pk %}, 
    # mantendo o código flexível
    #------
    path('car/<int:pk>/update/',CarUpdateView.as_view(),name='car_update'), #car/<int:pk>/update/': É o padrão da URL. 
    #Ela captura um número inteiro (int) e o atribui à variável pk (Primary Key). 
    #Por exemplo: /car/5/update/ abrirá a página de edição do carro com ID
    #CarUpdateView.as_view(): Converte a classe baseada em view (UpdateView) em uma função que o Django pode executar quando a URL é acessada. 
    #Essa view cuida de renderizar o formulário e salvar as alterações no banco de dados.
    #name='car_detail': Atenção aqui! O nome está como car_detail, mas o padrão da URL (/update/) indica que é para edição. 
    # Geralmente, este nome deveria ser algo como 'car_update' ou 'car_edit'.
    #. Nomear a rota é útil para referenciá-la nos templates, mas manter um nome descritivo 
    # (como name='car_update') evita confusões futuras.

    path('car/<int:pk>/delete/',CarDeleteView.as_view(),name='car_delete'),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
if settings.DEBUG: # INTERNET 04/06 #if settings.DEBUG:: Verifica se o seu projeto está em modo de desenvolvimento (DEBUG = True).
     #Isso é uma medida de segurança para garantir que arquivos locais só 
    #sejam expostos na sua máquina e nunca em produção (quando o site estiver online para o público).
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  #urlpatterns += ...: Adiciona uma nova rota à lista de URLs do seu projeto
  #static(...): Uma função auxiliar do Django que mapeia uma URL na web para uma pasta física no seu computador
  #settings.MEDIA_URL: É a URL pública que será usada no navegador (ex: /media/uploads/foto.jpg)
  #settings.MEDIA_ROOT: É o caminho absoluto da 
  # pasta no seu computador onde os arquivos estão realmente salvos (ex: /home/usuario/projeto/media/uploads/foto.jpg).

#OBS: path('new car/'): É uma URL estática. Ela serve para uma ação específica, como carregar um formulário para criar um novo carro
# path('car/<int:pk>/'): É uma URL dinâmica. O <int:pk> captura um número inteiro da URL e o repassa para a view com o nome pk 
# (geralmente usado como Primary Key para exibir, editar ou deletar um carro específico).

#pRIMARY KEY(CHAVE PRIMARIA) é um identificador único para cada linha ou registro em uma tabela de banco de dados. 
# Ela funciona de forma semelhante ao número do CPF de uma pessoa: garante que
#  nenhum registro seja duplicado e permite encontrar informações específicas de maneira rápida e precisa