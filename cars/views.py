#Usado no retorno das views
# from cars.forms import Carform, importo os dados de forms

#from django.shortcuts import render, redirect  # Desabilitado,devido a simplificacao feita CreateView
#from django.views import View # Usado para fazer a simplificacao do codigo, DESABILITADO,DEVIDO A SIMPLIFICACAO FEITA, CREATEVIEW
from django.contrib.auth.mixins import LoginRequiredMixin # Internet
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required # Tem a função limitar o acesso dos usuários,apenas só quem esta logado,pode fazer as coisas.
# Porque atraves da url, eu conseguia, fazer varias coisas, só colocava o ip e o que eu queria fazer.
# Decorators  ele Verifica e autentica se o usuário tem permissão para executar uma ação (muito comum em APIs)
#1- Bloqueia usuários anonimos,2-Views Baseados em funcao(FBvs),3-A sessao/autenticacao dp usuário
#---
from django.utils.decorators import method_decorator
#1-Adaptar decorators para classes,2-Views baseadas em classe (CBvs),3- Ele apenas envelopa outro decorator
#----
# Detail usado para direcionar para dentro da imagem clicada.
# UpdateView foi acrescentado, devido a informacao la em baixo.
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView # Neste caso,estamos sendo mais especialista, do que, quando usamos views.
#from django.views import View # Usado para fazer a simplificacao do codigo

# Direciona dentro do site para onde direcionado, 
# determinada informacao.
#Meus_carros_1 aparece a mensagem no navedador
#127.0.0.1/cars
# Lembrando que essas informações esta relacionado
# A urls, esta no lado esquerdo
# <h1>Meus Carros</h1> retorna HTML5
# Todos os retornos usado aqui na views,estão
# dentro da pasta templates\car
# A funcao render, renderiza uma resposta http
# e devolve uma resposta ao usuário
#É o templete de carros que eu quero responder ao usuário
# ou seja, ele pega os templets que estão 
# em (cars.html)
#context é um dicionario, ou seja, uma lista de dados dos carros
#oBS: cars.html trabalha direto com views
#Car.objects.all() quer dizer do meu modelo Car
# la em cima na importação(from cars.models import Car)
# Quer dizer que os objetos dele, eu quero todos
# Traz o registro do banco de dados da tabela de carro
#cars=Car.objects.all() pega informações do banco de dados
#all traz todos os registros da tabela
#Query-faz uma consulta ao banco de dados
# Filtra uma marca especifica
# Não esquecer do _ _ brand__name
# O _ _ significa que estou navegando de uma tabela para outra
# cars= Car.objects.filter(model='Virtus')
# Filtro o modelo do carro,lembrando que devo escrever
# o nome do carro, conforme foi cadastrado(Virtus)
#request tem todos os dados da requisição que o usuário faz
#def cars_view(request): # Desativada,devido a simplificacao abaixo
     # busca todos os carros os carros que estão na tabela do
     #banco de dados
     # Depois verifico se ele esta chamando uma busca especifica
     # usando search
     #Caso eu coloque -model, ele faz a ordenacao de forma contraria
     # de z para a
     #Caso eu coloque model,ele faz a ordenacao de
     # a para z
     #cars=Car.objects.all().order_by('model') # Desativada,devido a simplificacao abaixo
     #search = request.GET.get('search') # Desativada,devido a simplificacao abaixo
     #if search:# Desativada,devido a simplificacao abaixo
     #cars = Car.objects.all()
     # Eu capturo a requisicao feita pelo usuário   
     #print (request.GET)
     #cars = Car.objects.filter(brand__name='volkswagem')
     #cars= Car.objects.filter(model='Virtus')
     # cars= Car.objects.filter(model__contains='Virtus')
     #Filtra qualquer carro que contem a string solicitada
     # Seach é a busca que o usuário esta passando
     #contains faz busca igual foi adicionado
     # Nao procura de outra forma,se foi adicionado minusculo,so acha minusculo
     # Se adicionado maisculo procura só maisculo
     # icontains o django ignora se a busca é feita em maisculo ou minusculo
     #oder_by ordena na hora de pesquisar
          #cars= Car.objects.filter(model__icontains=search) # Desativada,devido a simplificacao abaixo
    
     #return render(  # Desativada,devido a simplificacao abaixo
        #request,# Desativada,devido a simplificacao abaixo
       # 'cars.html',# Desativada,devido a simplificacao abaixo
        #{'cars': cars}# Desativada,devido a simplificacao abaixo
        #)# Desativada,devido a simplificacao abaixo

#Aqui estou simplificando o codigo acima
#class CarsView(View) esta importando de view, la de cima
# Neste momento, ele esta herdando todos os recursos que tem pronto no
#Django
# Ele simplifica e executa muita coisa, ou seja, importa muitas funções que estão ocultas.
#O parâmetro request carrega todos os dados da solicitação HTTP que o cliente (como um navegador ou aplicativo) enviou para o servidor. 
# Ele atua como uma ponte entre quem está acessando a página e o seu código back-end
# OBS: A view é generica, posso usar em vários contextos diferentes
# Get lista coisas, ou seja,, o método .get() é usado para recuperar o valor de um parâmetro específico enviado em uma requisição HTTP (geralmente via URL). 
#OBS: class Carsview da linha abaixo foi desativada, devido a criação e configuração da da CarListView
#class CarsView(View):
     #def get(self,request):
          #cars= Car.objects.all().order_by('model')
          #search = request.GET.get('search')
          #if search:
               #cars = cars.filter(model__icontains=search) # Aleterado _ em model_icontains=search
          #return render(
               #request,
               #'cars.html',
               #{'cars': cars}
          #)
     
     # a ListView é usada de forma especifica, objetiva. View é mais simples.
     # CarListView, o nome poderia ser o que eu quisesse,desde que esteja no formato padrao de classe.
class CarsListView(ListView): # Cria uma classe para listar carros usando uma página pronta do Django.
     model= Car # Diz ao Django para buscar os dados da tabela de carros no banco de dados
     template_name = 'cars.html'  # Define o arquivo HTML que vai mostrar a lista de carros na tela  
     context_object_name = 'cars' # Cria o nome da variável que você vai usar dentro do HTML para listar os carros.
     def get_queryset(self):# A linha def get_queryset(self): define um método no framework Django (ou Django REST Framework) usado para retornar e customizar 
          #a lista de dados (o QuerySet) que uma View vai buscar no banco de dados
          #return super().get_queryset() #super().get_queryset() busca todos os itens do banco de
          #dados definidos para aquela View (ex: todos os Produtos ou Usuários)
          # Foi retirado
          # cars => Recebe todos os carros, ordenados por model
           cars=super().get_queryset().order_by('model') #Essa linha é comumente usada em views baseadas em classes (CBVs) do Django. 
           #Ela define o conjunto de dados que a view vai manipular, ordenando todos os itens alfabeticamente com base no campo model. 
           # super é uma funcao orientada a objetos do python. Eu uso quando quero acessar a classe pai.
           # self.queryset=super().get_queryset().order_by('model') = cars= Car.objects.all().order_by('model')
           #get_queryset() é usado nos frameworks Django e Django REST Framework (DRF) para definir e personalizar a lista de dados (objetos) que o seu sistema irá 
           # buscar no banco de dados.
           #O comando order_by('model') ordena os resultados de uma consulta (QuerySet) em ordem alfabética com base no campo ou coluna chamada model (modelo). 
           # Ele é comumente usado em frameworks ORM como o Django ou em bancos de dados baseados em documentos
             
     #OBS: return super().get_queryset(): Retorna a consulta padrão de forma limpa. Modifica os dados apenas para a requisição atual.
     #self.queryset = super().get_queryset().order_by('model'): Sobrescreve permanentemente o atributo da classe. 
     # Altera o comportamento de todas as requisições seguintes de forma global.
     #----------------
     # cars=super().get_queryset().order_by('model') e search = self.request.GET.get('search') é um escopo mais fechado, mais especifico
     # search recebe uma instancia do proprio objeto
           search = self.request.GET.get('search') #Essa linha de código em Python (usada no framework web Django) 
           #captura um termo de busca enviado pelo usuário através da URL do navegador
           #self.request: Representa a requisição HTTP atual que o servidor recebeu do navegador
           #.GET: Acessa os parâmetros enviados via método GET, que são aqueles visíveis na URL após a interrogação (ex: ?search=python).
           #.get('search'): Busca especificamente pelo valor do parâmetro chamado search
           #Diferencial do .get(): Se o usuário não tiver digitado nada na busca (ou seja, o parâmetro search não existir na URL), 
           # o código não quebra; ele apenas retorna None por padrão
           #search =: Armazena o termo encontrado (ou None) dentro de uma variável chamada search para que você possa usá-la depois (como filtrar um banco de dados).
           if search:
                cars = cars.filter(model__icontains = search)
           return cars
#def new_car_view(request): # Desativado,devido a simplificacao do codigo  abaixo
   #return 'Novo Carro!' Desativado
   #new_car_form = CarForm é um formulario vazio
   #If request.method=='POST', Quando o usuário preencheu todo o cadastro, faz a captura do cadastro
    #if request.method == 'POST': # Desativado,devido a simplificacao do codigo abaixo
          # New_carElenew_car_form = CarForm(request.POST, request.FILES)
          #  captura o que o usuário adicionou e manda para o banco de dados.
          #request.post pega os dados da requisição,feito pelo usuário quando preencheu o formulário ou cadastro de carros.
          #request.FILES isso quer dizer, que quando eu faço todo o cadastro, ele não vai mandar apenas texto, vai mandar
          # também arquivo de imagem.
          # Recebe os dados preenchidos pelo usuário.
           #new_car_form = CarModelForm(request.POST, request.FILES) # Desativado,devido a simplificacao do codigo abaixo
          # if new_car_form.is verifica se os dados preenchidos pelos usuários
          # são validos
          #is_valid é uma funçao pronta dos formularios do django
           #if new_car_form.is_valid(): # Desativado,devido a simplificacao do codigo abaixo.
              # Para o save funcionar,devo escrever também em forms
              #def save(self)
               # new_car_form.save() # Desativado,devido a simplificacao do codigo abaixo
              # return  redirect redireciona o usuário para lista de carros
              #É necessário colocar o redirect la em cima também.
                #return redirect('cars_list') # Desativado,devido a simplificacao do codigo abaixo
      # else abaixo é quando o usuário entra apenas em new_car, em branco para fazer um cadastro de um novo carro
      # ou seja, ele retorna  em branco para cadastrar o carro.
    #else: # Desativado,devido a simplificacao do codigo abaixo.
       #new_car_form = CarModelForm() # Desativado,devido a simplificacao do codigo abaixo
   # Retorna para o nosso usuário que esta acessando a tela
   # um render, volta a pagina que esta sendo criada
   #new_car.html
    #return render(request,'new_car.html',{'new_car_form':new_car_form}) # Desativado,devido a simplificacao do codigo abaixo.
#def home_view(request): # suporte ia
    #return render(request, 'home.html')# suporte ia


# O codigo abaixo, simplifica def new_car_view(request)
#O método def get(self, request) é usado em frameworks web orientados a objetos (como o Django ou Flask) para responder a requisições HTTP do tipo GET feitas pelo navegador. 
#Ele é executado quando o usuário simplesmente acessa uma página (digitando a URL ou clicando em um link) ou busca dados sem enviar um formulário.
# DESATIVADO,DEVIDO A SIMPLIFICAÇÃO FEITA ABAIXO EM NEWCARCREATEVIEW 
# class NewCarView(LoginRequiredMixin,View):#INTERNET  (LoginRequiredMixin),  para o Django saber que você está logado ao clicar nos botões!
#      login_url='login' # INTERNET, Se tentar acessar sem logar, vai para a tela de login
#      def get(self, request):
#           new_car_form= CarModelForm()
#           return render(request, 'new_car.html',{'new_car_form': new_car_form})
     
#      def post(self,request):
#           new_car_form= CarModelForm(request.POST, request.FILES)
#           if new_car_form.is_valid():
#                new_car_form.save()
#                return redirect('cars_list')
#           return render(request, 'new_car.html',{'new_car_form': new_car_form})
     
# Obs: Quando eu faço essas simplificações, eu pego da documentacao  disponibilizada no django e foi salvo em favoritos

# Aqui estou mais objetivo.
# Ele esta simplificando NewCarView,DESATIVADO ACIMA.
#@method_decorator: Transforma um decorator feito para funções comuns (como o login_required) em um formato compatível para ser usado dentro de classes.
     #login_required: É o decorator nativo do Django que verifica se o usuário está logado, não estiver, ele não da continuidade.
     # Se não estiver, ele redireciona o usuário para a página de login
     #name='dispatch': Aplica essa regra de bloqueio especificamente ao método dispatch da classe.
@method_decorator(login_required(login_url='login'), name= 'dispatch') # proteger uma View baseada em Classe (CBV) no Django, garantindo que apenas usuários logados possam acessá-la.
class NewCarCreateView(CreateView): # # Define uma classe que cria um novo carro, herdando a view genérica baseada em classe (CBV) CreateView.
     model= Car # Especifica o modelo do banco de dados (Car) que será utilizado para salvar as informações.
     form_class = CarModelForm # Define o formulário customizado (CarModelForm) que validará e renderizará os campos na tela.
     template_name = 'new_car.html' # Define o arquivo HTML (template) que será renderizado para o usuário final.
     success_url = '/cars/' # Define a URL de destino para onde o usuário será redirecionado após cadastrar o carro com sucesso.
     # Obs: Devido a essa simplificaçao, foi necessário ir em new_car.html e retirar new_car_form.as_table. Pois a simplificaçao já faz isso.
     # Se eu tivesse deixado new_car_form.as_table, eu teria que configurar aqui também.
     

# Detalhe do carro, quando clicamos na imagem, ela direciona para dentro, onde ficam as informaçoes.
# Para isso funcionar preciso criar na pasta car\templates, a funcao DetailView
class CarDetailView(DetailView):
     model= Car
     template_name = 'car_detail.html'
     #-------
     #class CarUpdateView(UpdateView):
  #O que é: Declara uma nova classe chamada CarUpdateView que herda (estende) a 
  # funcionalidade principal da classe UpdateView do Django  
  #O que ela faz: Por herdar essa CBV, a view gerencia automaticamente todo o ciclo de vida de uma
  #  atualização de dados: busca o registro existente no banco de dados usando a chave primária (pk), 
  # preenche o formulário com esses dados existentes, lida com a submissão via método POST, 
  # valida os novos dados e os salva.
@method_decorator(login_required(login_url='login'), name= 'dispatch') # Mesma funcao do acrescimo acima, proteger,restringir.
class CarUpdateView(UpdateView):  
          model = Car #O que é: Define qual tabela/modelo do banco de dados será afetado por esta view
          #O que ela faz: Aponta para o seu modelo (geralmente definido no arquivo models.py), 
          # que representa a entidade "Carro". O Django usa isso para saber 
          # qual tabela consultar e qual objeto instanciar para edição
          form_class = CarModelForm #O que é: Especifica a classe de formulário 
          #personalizado que será usada para renderizar os campos e aplicar validações.
          #O que ela faz: Em vez de listar os campos manualmente usando fields = ['nome', 'marca'], o Django usará o 
          # CarModelForm (geralmente um forms.ModelForm). Isso é ideal 
          # se você deseja estilizar o formulário com CSS, aplicar widgets personalizados ou adicionar lógicas de validação complexas
          template_name = 'car_update.html'  #O que é: Define o caminho do arquivo HTML que será renderizado para exibir o formulário na tela 
          #O que ela faz: Diz ao Django que a página de formulário de atualização do carro deve usar o arquivo car_update.html.
          #  Se esta linha fosse omitida, o Django tentaria por padrão procurar por algo como car_form.html
          #----- sucess_url='cars/' foi desativado. EXPLICAÇÃO ABAIXO
          #success_url = '/cars/' #O que é: Define a URL de redirecionamento após a atualização do carro ser salva com sucesso
          #O que ela faz: Uma vez que o usuário envia o formulário e os dados são salvos com êxito, o Django executa um redirecionamento
          #  HTTP para esta URL — que, neste caso, leva o usuário de volta à lista principal de carros.
          #OBS A CRIACAO, PRECISO CONFIGURAR NO CORACAO DO PROJETO APP\URL, TODOS AQUI!
          def get_success_url(self): # Isso foi feito, pois eu quero quando fizer alguma alteração no carro e salvar
                # Voltar para detalhes, não para pagina inicial
                return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) # PARA ISSO INSERI ESSAS 3 LINHAS DE CODIGO E DESATIVEI (success_url='/cars/')
               #return reverse_lazy  é usada para redirecionar o usuário para uma página específica após a conclusão de uma ação, como deletar um registro
               #return: Encerra a função ou método atual e envia o resultado de volta.
               #reverse_lazy: É uma ferramenta do Django que procura a URL correta no arquivo urls.py com
               #  base no nome fornecido (e não pelo caminho completo). A parte "_lazy" significa que o endereço só será 
               # calculado quando for realmente necessário (atrasando a execução para evitar erros de importação)
               #kwargs: Refere-se a keyword arguments, que são argumentos passados no formato de dicionário (chave=valor)
               #'pk': É a chave que o Django procura para identificar o parâmetro na sua URL (por exemplo: path('usuario/<int:pk>/', ...))
               #self.object.pk: Pega o ID (Primary Key) do objeto que acabou de ser criado ou alterado pela view (por exemplo, o ID 5 de um novo usuário)
@method_decorator(login_required(login_url='login'), name= 'dispatch')  # Mesma funcao acima, proteger e restringir o acesso.       
class CarDeleteView(DeleteView): #Define uma classe que herda de DeleteView para gerenciar a exclusão de um objeto
      model = Car  # Especifica qual modelo do banco de dados (tabela) será afetado (neste caso, o modelo Car)
      template_name = 'car_delete.html' # Define o arquivo HTML que será renderizado para confirmar a exclusão com o usuário
      success_url = '/cars/' # Define a URL para onde o usuário será redirecionado após o registro ser excluído com sucesso

      #OBS: A @method_decorator(login_required(login_url='login'), name= 'dispatch') , NÃO FOI COLOCADA PARA DETAIL,
      # POIS ELA PRECISA FUNCIONAR PARA todo mundo, sem restricao, ou seja, se uma pessoa que não esteja logada, quer ver os detalhes
      # dos carros,poderá acessar,sem restrições.