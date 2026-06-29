
import openai 

def get_car_ai_bio(model, brand,year): # Define uma função que aceita o modelo, a marca e o ano do carro como argumentos
    # O prompet abaixo, ele passa as informações que a IA vai passar , ficando exposto na pagina do veciulo.
    # O meu deu um erro, pois devo adicionar um valor na IA, mas esta certo.
   prompt='''' 
    #Me mostre uma descricao de venda para o carro {} {} {} em apenas 250 caracteres.Fale coisas especificas desse modelo de carro.
    '''
    #openai.api_key='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'
   prompt = prompt.format(brand, model, year) 
   # DESATIVEI RESPONSE,DEVIDO A FALTA DE CREDITO NO OPEANAI
   #response = openai.completions.create( #Aciona o endpoint de Completions da biblioteca atualizada (OpenAI v1.0.0+)
        #model='text-davinc-003' # O modelo demonstrado, esta desatuazalido.
        #model='gpt-3.5-turbo-instruct', # DESATIVADO,DEVIDO A FALTA DE CREDITO NO OPEANAI
        #prompt=prompt, # DESATIVADO,DEVIDO A FALTA DE CREDITO NO OPEANAI
       # max_tokens=1000, # Define o limite máximo de tamanho da resposta gerada pela inteligência artificial #NAO TENHO SALDO DISPONIVEL,DESATIVADO
   texto_simulado =f" Ótima oportunidade! Conheça o {brand}{model}{year}. Um excelente desempenho para toda sua familia"  # ADICIONADO, VIA SUPORTE INTERNET 22/06
   return texto_simulado[:250]
    #) # Fecha os parâmetros da requisição enviada para a API .DESATIVADO,DEVIDO A FALTA DE CREDITO NO OPEANAI

# choices :A OpenAI foi desenhada assim porque você pode pedir para ela gerar mais de uma opção de resposta para a mesma pergunta (usando o parâmetro n).
#[0] seleciona a primeira opção de resposta da lista (que é a padrão e única gerada, a menos que você configure o contrário).
#Depois de entrar na primeira opção ([0]), você acessa a propriedade .text, que contém estritamente a string de texto com a resposta, 
# descrição ou bio do carro gerada pelo modelo.