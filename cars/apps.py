from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field ='django.db.models.BigAutoField' # Já vem quando eu criou o signals, não foi criado por mim.
    name = 'cars'

# ready() é servir como um gancho de inicialização (startup hook).
#  Ele é executado automaticamente pelo framework assim que o registro de aplicativos é totalmente carregado e está pronto
#Registrar Signals: O uso mais comum é conectar funções receptoras a Signals do Django (como post_save ou pre_delete).
#  Importar os sinais dentro do ready() evita problemas de importação cíclica de arquivos
#Configurações Iniciais e Verificações: Executar códigos de validação de ambiente, 
# checar chaves de APIs externas ou registrar customizações no painel administrativo

    def ready(self): #ready(): Chama o método .ready() dessa classe base
        import cars.signals
        #return: Devolve o que quer que a classe base retorne após ser executada
        return super().ready() #super(): Busca a classe base da qual a sua classe está herdando
    
    # OBS: CRIACAO DO INVENTARIO VAI SER FEITA EM MODELS,ESTA DENTRO DE CARS.
