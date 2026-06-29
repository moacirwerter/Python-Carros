#Tudo que estiver relacionado a app de car
# vai esta aqui
from django import forms
from cars.models import  Car
# Brand estava antes, eu removi,devido
# As alterações feitas.
# Estou criando o formulario de carros como uma classe
# E essa classe de carros esta herdando de forms.form que é algo pronto do django
#forms.form é um recurso do django, ou seja, uma serie de recursos e validação de dados
# do django, ou seja, estamos criando nosso formulario personalizado herdando de forms
# as Informacoes referente a model, esta dentro
# de models.
#Brand.objets.all estou buscando todas as marcas(brands), esta em models.py
# Da minha tabela brand do meu banco de dados
# ou seja, vai listar todas as marcas cadastradas no banco de dados
#factory_year esta pegando informações de models.py
# model_year,plate,value e photo esta pegando informações de models.py
#Atencao: mesmo pegando informacoes de models.py
# ModelChoiceField ele seleciona o modelo do carro que quer cadastrar
#Estou usando forms como base das informacoes
# Herda de um formulario
#Estou lincando forms com models
#class CarForm(forms.Form):
    #model=forms.CharField(max_length=200)
    #brand=forms.ModelChoiceField(Brand.objects.all())
    #factory_year = forms.IntegerField()
    #model_year = forms.IntegerField()
    #plate = forms.CharField(max_length=10)
    #value= forms.FloatField()
    #photo=forms.ImageField()
     #Tem ligação com save que foi configurado em views
     # Car foi adicionado em cima
     #def save(self) cria um objeto carro com os dados do form
     # Que o usuário esta mandando
     #self acessa meu proprio form acima
     #cleaned_data é um dicionário do Django que 
     # contém os dados de um formulário após passarem por validação e limpeza
    #def save(self):
        #car = Car(
           #model=self.cleaned_data['model'],
           #brand=self.cleaned_data['brand'],
           #factory_year=self.cleaned_data['factory_year'],
           #model_year = self.cleaned_data['model_year'],
           #plate = self.cleaned_data['plate'],
           #value= self.cleaned_data['value'],
           #photo=self.cleaned_data['photo'],
        #)


        # Este save não tem nada a ver com o save acima
        # Ele é objeto da tabela do banco de dados
        # Ele será cadastrado no banco de dados
        #car.save()
        #Retorna o objeto que foi criado
        
        #return car
    
    # Simplifica o codigo acima
    #ModelForm não é um formulario simples, onde ele faz um link
    # Com seu modelo da tabela do seu banco de dados
    #CarModelForm tem que ser inserido na views
class CarModelForm(forms.ModelForm):
    # vou reescrever a classe META
    # O nome Meta é obrigatório, se você quiser que o Django herde automaticamente as configurações do modelo. 
    # O Django busca especificamente por uma classe interna com esse nome exato para configurar o ModelForm
    class Meta:
        #Car esta especificado la em cima, em from
        model= Car
        # A informacao abaixo,significa que eu quero
        #todos os campos da tabela car nesse formulario
        #As alterações feitas em models, não preciso adicionar nada aqui, visto que,configurei aqui 
        # para pegar todas as informações
        fields='__all__'

       # Estamos criando uma funcao chamada clean_value, tendo como objetivo restringir um valor a ser adicionado
       # Baseado em models (value = models.FloatField(blank=True,null=True) 
       # Sempre o clean para criar sintaxe de validacao
       # Essas validacoes trabalha junto com is_valid(), que esta em views
    def clean_value( self ):
        # Estou capturando o valor que o usuario esta mandando no nosso form
        # self é uma instancia do form
        #cleaned_data é uma funcao nativa do django, que retorna os dados limpos e validados, que o usuario inserio
        # ou seja, fala, capture para mim o valor que o usuario esta inserindo com o campo especifico(value)
        value = self.cleaned_data.get('value')
        if value < 20000:
            #self é o proprio formulario com os valores que esta chegando
            self.add_error('value', 'valor minimo do carro deve ser R$20.000' )

        return value  

    #A regra abaixo,define carro só pode ser cadastrado,se for um determinado ano em diante.
    def clean_factory_year(self):
        factory_year=self.cleaned_data.get('factory_year')
        if factory_year < 2020:
            self.add_error('factory_year','So pode ser cadastrado a partir de 2020')  

        return factory_year

        