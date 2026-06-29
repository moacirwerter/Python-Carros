#Ele esta interagindo com o app
# o UserCreationForm faz essa funcao de autenticacao , é um form que já esta  pronta do django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login # internet

#UserCreationForm: Você está usando o formulário padrão do Django, que já lida com toda a 
# lógica pesada (criação de usuário, hashing de senha e validações de segurança) [1, 2].
# Fluxo POST vs GET:POST: Ocorre quando o usuário clica em "enviar". 
# O código valida os dados com is_valid() e, 
# se estiver tudo certo, salva no banco de dados com user_form.save() 
# GET (else): Quando o usuário entra na página pela primeira vez, ele apenas carrega um formulário vazio 
# Redirecionamento: Após o sucesso, ele envia o usuário para a página de login, o que é uma boa prática de UX 
## Login_view, que foi criado em urls, deve ser criado também na views, porque ele necessita de autenticacao
#O AuthenticationForm é o formulário nativo do Django para autenticação de usuários. Ele valida credenciais (geralmente nome de usuário/email e senha), 
# autentica o usuário no sistema e bloqueia contas inativas, tudo de forma automática e segura
def register_view(request):
    if request.method =='POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:   
        user_form = UserCreationForm()
    return render(request,'register.html',{'user_form':user_form})
    # a view abaixo, precisa de um templet para funcionar
    #Ela sera criada,dentro accounts/templates
def login_view(request):
    if request.method == 'POST':# INTERNET 
        # As funcoes username e password , recebem as informações passadas pelos usuários, ou seja, captura usuario e senha
        # que foi digitado no formulario
        # e validar, se os usuários e senhas estao corretos.
        # estao certos.
        #username = request.POST.get['username'] # INTERNET
        #password = request.POST.get['password'] # INTERNET
        username = request.POST['username']  #AULA
        password = request.POST['password'] #AULA
        login_form = AuthenticationForm()
        #A função authenticate() no Django serve para verificar as credenciais (como nome de usuário e senha) de um usuário.
        #  Ela compara os dados informados com o banco de dados e, 
        # se estiverem corretos, retorna o objeto User; caso contrário, retorna None
        user = authenticate(request, username=username,password=password)# internet
        # If user is not None: se o usuário nao retornar nulo, é sinal que o usuario é valido
        #Quando o código diz if user is not None:, significa que ele primeiro verifica se o usuário foi encontrado no banco de dados. 
        # Se a resposta for positiva, a função login() é chamada para iniciar a sessão 
        # (criar o "cookie" ou "token" de autenticação), permitindo que 
        # ele acesse áreas restritas do site ou aplicativo.
        if user is not None:
            #login(request, user): Inicia oficialmente a sessão do usuário no sistema.
            #  Ele salva o ID do usuário nos cookies/sessão do navegador para que o site lembre dele nas próximas páginas
            login(request,user)
            # A função de return redirect('car_list') é enviar o usuário para uma página diferente dentro do seu sistema web, 
            # saindo da página atual e carregando a rota nomeada como car_list.
            # É muito usada após uma ação (como criar ou editar um carro) para 
            # evitar que o usuário envie o mesmo formulário duas vezes ao atualizar a tela
            #return redirect('car_list') # AULA
            return redirect('cars_list') # INTERNET
        
        else:
            login_form = AuthenticationForm()
    else:
        #A instrução login_form = AuthenticationForm instancia o formulário padrão do Django usado para autenticar usuários. 
        # Ele cria os campos de usuário e senha, e valida as credenciais contra o banco de dados.
        login_form= AuthenticationForm()
        #  return render(request,'login.html',{'login_form' :login_form})  Essa linha é usada no Django para processar 
        # e responder a uma requisição web.
        #  Ela renderiza a página HTML de login e envia o formulário correspondente para ser exibido ao usuário
        return render(request,'login.html',{'login_form' :login_form}) 
        #login_form = AuthenticationForm(request,data=request.POST) # Internet

        #if login_form.is_valid():# internet
            #usarname = login_form.cleaned_data.get('username') # internet
            #password = login_form.cleaned_data.get('password') # internet

            #user= authenticate(username=username,password=password)# internet

            #if user is not None: # internet
                #auth_login(request,user)# internet
                #return redirect('car_list')# internet
    #else: # internet

        #login_form= AuthenticationForm()# internet
    #return render(request,'login.html',{'login_form':login_form})# internet


