from django.db import models

#É uma tabela nova no banco de dados
#Brand marca do carro
# Foi criado para pode alterar brand, que esta abaixo
#O objetivo é ter marcas já cadastradas
# Nao sendo possivel inserir o que quiser
#Evitando adicionar nomes incorretos
# a classe abaixo esta ligada a brand=models.Foreignkey(Brand,on_delete=models.PROTECT,related_name='car_brand')
# name é o nome da marca
class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    # Configura a estetica do site, quando for apagar
    def __str__(self):
        return self.name

# Eu crei a classe chamada car, que vai ser o nome da tabela do banco de dados.
# Ela tem uma herança da classe Model, que já esta pronta no jango,criada pelo desenvolvedor django.
class Car(models.Model):
#id= campo,AutoField ele se autoincrementa
# se voce for incluir alguma coisa, ele segue uma sequencia
# se for removido também.Ex:Id1,id2, etc
# O banco de dado faz uma sequencia, ele não se repete
    id = models.AutoField(primary_key=True)
    #O campo model não tem nada a ver com 
    #campo acima,foi o nome que foi dado modelo
    #charfield é um campo do tipo texto
    #Charfield aceita todo tipo de caractere
    #max_length=200,define a quantidade maxima
    #De caractere
    model = models.CharField(max_length=200)
    #brand= marca
    #brand = models.CharField(max_length=200)
    #Comentei o campo acima para desativar,pois não usaremos, já que, ele permiti que seja incluido qualquer palavra
    # brand=models usando Foreignkey(chave estrangeira, ou seja, esse campo é uma ligação com outra tabela, a tabela brand)
    #on_delete=models.PROTECT é quando eu tenho um carro ligado a uma determinada marca, caso alguem apague brand fiat, posso
    #perder tudo que esta ligado a marca fiat
    # Se tivesse CASCADE por exemplo,se alguem apaguasse o brand fiat,tudo que estivesse ligado a essa marca,seria apagado
    # related_name é o nome dessa relação, ou seja, relacao entre car e brand
    # No final da linha, tem o nome car_brand, poderia ser qualquer nome
    brand=models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='car_brand')
    #factory_year= ano de fabricao
    #IntegerField= armazena ano ex:2022
    factory_year = models.IntegerField(blank=True,null=True)
    #model_year=modelo de fabricao
    
    model_year = models.IntegerField(blank=True,null=True)
    
    plate = models.CharField(max_length=10,blank=True,null=True) 
    #float = campo flutaunte
    # blank true e null true quer dizer
    #que eu posso preencher tudo e deixar esse campo
    # em branco ou nulo, não preciso informar nada
    #class Car(models.Model):
    # Outros campos (ex: model, brand)
    value = models.FloatField(blank=True,null=True)

    photo = models.ImageField(upload_to='cars/',blank=True,null=True)
    #A informaçao abaixo, eu mudo algumas questoes esteticas do site
    #É uma função do Model, ou seja,ela pega de lá
    # Eu quero que ele retorne o modelo do carro
    #------
    bio = models.TextField(blank=True, null=True) # Vou adicionar um resumo do carro.
    #bio: É o nome da variável (e da coluna no banco de dados) que vai guardar a informação.
    #models.TextField(): É o tipo de campo. O TextField aceita textos grandes e sem limite fixo de caracteres, diferente de campos de texto curto.
    #blank=True (Validação na Interface):  Permite que o campo fique vazio em formulários.O usuário pode deixar o espaço da biografia em branco 
    # no site ou no painel de administração do Django sem receber um erro de "campo obrigatório".
    #null=True (Armazenamento no Banco de Dados)Permite que o banco de dados salve o valor como NULL (vazio).
    #Informa ao seu banco de dados (como PostgreSQL, MySQL ou SQLite) que aquela coluna não é obrigatória para criar um novo registro.
    #OBS: QUERO DEIXAR UM ACESSO PARA O USUÁRIO COMUM, EU VOU EM TEMPLATE E FAÇO A CONFIGURACAO DE ACESSO
    # vOU EM car_detail.html
    #---
    def __str__(self):
        return self.model
    #Toda alteracao feita,devo executar o comando 1º) makemigrations pe 2º migrate, pois informa ao banco as alterações que foram feitas
    #Obs: Tambem devo ir no admin.py e configurar para aparecer no site
class CarInventory(models.Model):      # Inventario dos carros
    #class: É a palavra que avisa o computador que você vai criar um molde (uma nova estrutura de dados)
    #CarInventory: É o nome do seu molde. Na programação, isso vira o nome da sua tabela.
    #(models.Model): É a herança. Isso ensina o Python que esse molde é, na verdade, uma tabela especial. 
    # Ela ganha "poderes" para salvar e buscar informações no banco de dados.
    cars_count = models.IntegerField()
    #cars_count: É o nome da variável (e o nome da coluna que será criada na tabela do banco de dados). Ela vai armazenar a quantidade de carros 
    #models.IntegerField(): É o tipo de dado do Django. Ele avisa ao framework que essa coluna só pode aceitar números inteiros (como 0, 5, 42 ou -10), 
    # gerando um campo correspondente no banco de dados (como o tipo INTEGER no SQL)
    cars_value= models.FloatField(default=0)
    # cars_value: É o nome da variável e da coluna na tabela do seu banco de dados.
    #models.FloatField(): Define o tipo do campo como float, adequado para números fracionários (ex: 1.5, 10.0, 99.9)
    created_at = models.DateTimeField(auto_now_add=True)
    #A linha created_at = models.DateField(auto_now_add=True) é usada no Django para preencher automaticamente uma coluna de banco de dados 
    # com a data exata em que um novo registro (linha) é criado.
    #O argumento auto_now_add=True define que o campo receberá a data atual automaticamente apenas uma vez, 
    # no momento exato em que o registro for criado no banco de dados.
    # models.DateTimeField: Diz ao banco de dados que este campo armazena apenas uma data (Ano, Mês e Dia),incluindo segundos.
    #default=datetime.now: Permite definir uma data e hora padrão, mas o valor pode ser alterado manualmente pelo usuário depois.
    #auto_now_add=True: Ativa a mágica da automação. Quando você salva um dado novo pela primeira vez, 
    # o Django grava a data do dia, i automaticamente
    class Meta:
        ordering = ['-created_at']
        #Sem o menos ['created_at']: Ordena de forma crescente (do mais antigo para o mais recente)
        #Com o menos ['-created_at']: Ordena de forma decrescente (do mais recente para o mais antigo)
        #class Meta:: É um espaço especial dentro da sua classe de modelo onde você guarda as configurações extras, também chamadas de metadados. 
        # O termo "Meta" serve para organizar os dados sem misturar as informações com os campos criados (como nome, preço, etc)
        #ordering = ['created_at']: Determina a ordem de exibição. O created_at geralmente é o nome do campo de data de criação.
    def __str__(self):
       return f'{self.cars_count} - {self.cars_value}'
#return: Finaliza a execução da função ou método e envia o resultado de volta para quem o chamou.
#f'...': Indica uma f-string (Formatted String Literal). É uma forma rápida e legível de colocar variáveis e expressões 
# diretamente dentro de um texto em Python.
#self: Refere-se à instância atual da própria classe (o objeto que está executando o método).
#{self.cars_count}: Uma tag de substituição. O Python vai ler o valor armazenado no atributo cars_count desse objeto e colocá-lo aqui.
#-: Um texto fixo (um hífen com espaços) que vai separar os dois valores na string final.
#{self.cars_value}: Outra tag de substituição, que será trocada pelo valor do atributo cars_value
        
        #OBS: SEMPRE QUE ACONTECER ALTERAÇÃO EM MODELS, QUALQUER ALTERACAO, DEVE SER EXECUTADO OS COMANDO : MAKEMIGRATIONS E MIGRATE
        # python manage.py makemigrations e python manage.py migrate
