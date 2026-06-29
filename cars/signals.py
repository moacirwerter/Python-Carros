#from django.db.models.signals import pre_save,pre_delete,post_save,post_delete # São funções prontas 
# que o django tem para ser usado no signals,todos os pre foram desativados,resolvi excluir e posta uma nova abaixo.
from django.db.models.signals import pre_save, post_save,post_delete # Foi adicionado pre_save para,tendo como objetivo adicionar uma bio automatica.
from django.db.models import Sum # Sum, usado para somar.
from django.dispatch import receiver # Receiver escuta a mensagem
#O despachante (dispatch) é quem dispara o aviso de que o evento ocorreu
from cars.models import Car, CarInventory # Adicionado CarInventory,devido o invetario
# CarInventoryUpdate, usado para simplificar POST_SAVE E DELETE_SAVE
#pre_save: Disparado antes de um registro ser salvo no banco de dados.
#post_save: Disparado depois de um registro ser salvo. Muito útil para criar um perfil automaticamente quando um novo usuário se cadastra
#pre_delete: Disparado antes de um registro ser apagado
#post_delete: Disparado depois que um registro é excluído
#----------------
from openai_api.client import get_car_ai_bio 

#OBS: PARA FUNCIONAR O OPENAI_API, EU PRECISO MUDAR PARA PASTA RAIZ, ANTES EU TINHA COLOCADO DE MANEIRA ERRADA,DENTRO DE CARROS, ESTAVA DANDO UM ERRO.
# pasta openai_api não é obrigada a ficar na pasta raiz para o projeto funcionar, mas colocá-la lá traz grandes vantagens de organização e evita erros.
#Se ela ficar na raiz, qualquer parte do projeto pode acessá-la facilmente usando o mesmo caminho simples: from openai_api.client import
#------------------------------------
# OBS: PRE_SAVE  e PRE_DELETE foram desativados, pois vai ser feita uma configuração, relacionada ao inventario.
# Quando o carro novo for cadastrado, vai ser calculado 2 valores e vai ser salvo na tabela de inventario.
# vai ser calculado cars_count e cars_value, ou seja, vai contar quantos carros tem no estoque e vai calcular o valor total, baseado no campo value.
# calcula o valor e salva no banco de dados. ESSES DOIS EVENTOS, FICAM DENTRO DA FUNCAO SIGNALS.
#------------------------------------

def car_inventory_update():# Define a função responsável por atualizar a tabela de inventário.
    #print('## POS DELETE')
    #print(instance)
    cars_count = Car.objects.all().count() # Conta quantos carros existem no banco de dados. Nota: usar apenas .count() é mais rápido.
    cars_value = Car.objects.aggregate( #Inicia a agregação no banco de dados para calcular uma métrica sobre os carros.
        total_value=Sum('value') ## Soma o valor de todos os carros usando a função Sum do Django.
    )['total_value'] or 0 # Extrai o número somado do dicionário retornado pelo método aggregate. 
               # 0(ZERO) inserido suporte ia curso em 19/06, Sum('value') com or 0 caso não exista carro no banco

    CarInventory.objects.create( # Cria e salva um novo registro na tabela de histórico de inventário.
        cars_count=cars_count, # Salva a quantidade total de carros calculada no campo correspondente.

        cars_value=cars_value # Salva o valor financeiro total acumulado no campo correspondente.
    )
@receiver(pre_save, sender=Car) # Decorador que conecta a função ao sinal pre_save; dispara o código antes de um objeto Car ser salvo.
def car_pre_save(sender, instance, **Kwargs): # Define a função que recebe o modelo (sender) e a cópia do objeto prestes a ser salvo (instance).
    if not instance.bio: # Verifica se o campo de biografia (bio) do carro está vazio ou não foi preenchido.
            # Se não esta alimentada,adiciona a instancia.bio, com o respectivo texto(logo abaixo)
            #-------------
            #A linha ai_bio = get_car_ai_bio() chama uma função externa 
            # para gerar automaticamente uma biografia descritiva para o carro utilizando Inteligência Artificial
             
        ai_bio = get_car_ai_bio(
                #A linha ai_bio = get_car_ai_bio( inicia a chamada da função get_car_aipython _bio para passar os dados do carro 
                # (como modelo, marca e ano) e armazena o texto gerado por Inteligência Artificial dentro da variável ai_bio
            #---------
              instance.model,
              instance.brand, 
              instance.model_year
            
         )
            #--------
        instance.bio = ai_bio #'Bio gerada automaticamente'     # Define um texto padrão para a biografia caso o campo estivesse em branco.
        #'Bio gerada automaticamente'  DESATIVADA, VIA SUPORTE 19/06


#----
#O decorador @receiver diz: "Fique escutando o sinal post_save enviado pelo modelo User", ou seja, 
# ele vai ficar ouvindo tudo que acontece na tabela de carros, no evento pre_save
#@receiver(pre_save, sender=Car)
#def car_pre_save(sender,instance, **kwargs): # o nome car incluso, eu quis colocar
    # def: Palavra usada para criar (definir) uma nova função.
    #car_pre_save: É o nome da função. Você pode escolher qualquer nome, 
    # mas este indica que ela roda "antes de salvar" (pre) um carro (car)
    #sender: Significa o remetente. É a classe do modelo (o próprio modelo Carro) que está enviando o aviso, enviando um evento.
    #instance: É o objeto específico que está sendo salvo. Por exemplo, se você salvou um Fusca, a instance contém todos os dados daquele Fusca específico
    #**kwargs: Um dicionário que coleta parâmetros nomeados adicionais enviados pelo Django. 
    # Isso garante que a função continue funcionando mesmo se novas variáveis forem adicionadas ao sinal no futuro
    #print('## PRE SAVE')
    #print(instance)
@receiver(post_save, sender=Car)
def car_post_save(sender,instance, **Kwargs):# #post_save: Disparado depois de um registro ser salvo. 
    #Muito útil para criar um perfil automaticamente quando um novo usuário se cadastra
    #print('## POST_SAVE')
    #print(instance)
    #cars_count = Car.objects.all().count() FUI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
    car_inventory_update() # ADIONADO PARA SIMPLIFICAR POST_SAVE E POST_DELETE.
    
    # Cria uma variável no Python chamada cars_count que vai armazenar o número inteiro resultante dessa contagem (por exemplo: 15, 150, 0)
    #Car.objects.all() ele fala para selecionar todos os registros de carros do banco de dados .
    #count() em vezes de contar 1,2,3,4, ele ja conta 4 registros.
    # É a função que executa a contagem. Em vez de trazer todos os dados dos carros para a memória do Python, 
    # ela faz o banco de dados executar um comando de contagem muito rápido (equivalente ao SQL SELECT COUNT(*) FROM tabela_car
    #cars_value = Car.objects.aggregate( #FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
    #Faz parte do ORM do Django (Python) e serve 
    # para calcular valores resumidos (estatísticas) sobre todo o conjunto de dados da tabela Car no banco de dados
    # o método aggregate() realiza uma operação matemática global (como soma, média, valor máximo ou mínimo)
    #  e retorna um dicionário Python com o resultado
    #Aggregate Funções padrão como SUM (soma) ou AVG (média) pegam vários valores e os condensam em um único resultado
       #total_value= Sum('value')  #FUI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
       # O nome total_value,poderia ser qualquer nome que eu queira.
      # sum =somar, lembrando de fazer a importacao la em cima.
    #)['total_value'] # FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
    #  foi adicionado no final para extrair o valor exato do dicionário gerado pelo método aggregate()
      # Ele vai informar o valor total do estoque, ex: ['total_value=100000']
    #CarInventory.objects.create( # create, cria um registro na tabela.) #FOI SIMPLIFICADO 
    # EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
        #cars_count=cars_count, #FUI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
        #cars_count = cars_count: O sistema está pegando o valor atual armazenado na variável cars_count 
        #(que provavelmente guarda a quantidade total de carros,
          #como um número inteiro) e definindo-o em uma propriedade interna também chamada cars_count
          
        #cars_value=cars_value, # FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
        #cars_value = cars_value: O sistema está pegando o valor da variável cars_value (que provavelmente guarda o
        #valor financeiro somado de todos os carros, como um número decimal ou float) e aplicando-o à propriedade cars_value

        # OBS: sEMPRE QUE CHEGAR UM CARRO NOVO, O INVENTARIO SERÁ ATUALIZADO, QUANDO O CARRO É CADASTRADO, A FUNCAO ACIMA.

    #)


#@receiver(pre_delete, sender=Car)
#def car_pre_delete(sender,instance, **Kwargs):
    #print('## PRE DELETE ')
    #print(instance)

@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance, **Kwargs):
    car_inventory_update() 
    #print('## POS DELETE')
    #print(instance)
    #cars_count = Car.objects.all().count() #FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
    #cars_value = Car.objects.aggregate( # FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE  é a mesma coisa, em relacao a configuracao
        #total_value=Sum('value') # FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
    #)['total_value'] #FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
    #CarInventory.objects.create( #FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
    #cars_count=cars_count,#FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
    #cars_value=cars_value #FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
#) # FOI SIMPLIFICADO EM UPDATE,POIS, POS_DELETE E POST_SAVE  é a mesma coisa, em relacao a configuracao
