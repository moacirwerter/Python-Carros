from django.contrib import admin
from cars.models import Car,Brand
#obs: Quando foi criado a linha  (em models) brand=models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='car_brand')
#Foi necessário incluir o  Brand, conforme imagem acima

# Preciso criar uma classe car admin
#Herdo coisa do ModelAdmin
#list_display esta puxando de ModelAdmin
# Esta tudo pronto em Modeladmin,criado pelo django
#search_fields tambem esta dentro ModelAdmin
#Model é o tipo do carro:fusca, gol, etc
# Model uso quando quero fazer a pesquisa
#Dentro do servidor,caso eu queira melhorar,onde devo encontrar
# Adicionei brand, para melhorar a busca 
#-------
#list_display = ('model','brand','factory_year','model_year','value'): Controla quais colunas são exibidas na 
# listagem de carros no painel do Django Admin. Cada nome entre aspas corresponde a um campo no seu banco de dados.
#search_fields=('model','brand'): Adiciona uma barra de pesquisa no topo da página. Você poderá buscar carros digitando partes do modelo ou da marca.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value')
    search_fields=('model','brand')
    #A configuração search_fields = ('model', 'brand') define quais campos 
    # de um banco de dados serão consultados quando um usuário fizer uma busca por texto livre
# Devido a criação da linha brand=models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='car_brand')
# Em models.py, foi necessário criar uma nova class chamada BrandAdmin  abaixo
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)    
#Registra o admin que foi criado
#Ele precisa do from cars.models import car
admin.site.register(Car,CarAdmin) #A linha de código admin.site.register
#(Car, CarAdmin) serve para vincular e registrar o seu modelo no painel de administração do Django.

#Foi incluido essa linha abaixo,devido as alterações feitas em models
admin.site.register(Brand,BrandAdmin)
