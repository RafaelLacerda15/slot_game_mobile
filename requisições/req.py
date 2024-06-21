import requests
from bs4 import BeautifulSoup
from time import sleep


class Slot:
    def __init__(self,):
        self.url = "https://ssspaga.com"
        self.info = {}

    # Iniciar a função
    async def iniciar(self):
        while True:
            resultado = []
            # Enviar solicitação GET para o site
            response = requests.get(self.url)
            # Verificar se a solicitação foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                # Criar objeto BeautifulSoup para analisar o conteúdo HTML
                soup = BeautifulSoup(response.text, "html.parser")

                # Encontrar todos os elementos que contêm as informações desejadas
                produtos = soup.find_all("div", class_="game__item")
                contador = 0
                # Iterar sobre os elementos encontrados e extrair as informações
                for produto in produtos:
                    # Nome do produto
                    nome = produto.find("div", class_="game__name")
                    self.nomeF = nome.text
                    # URL da imagem do produto
                    self.imagem_url = produto.find("img")["src"]

                    # Porcentagem do produto (se aplicável)
                    porcentagem = produto.find("div", class_="game__percent--number")
                    self.porcentagemF = porcentagem.text

                    if self.porcentagemF in ['97%', '98%', '99%']:

                        if self.nomeF not in self.info:
                            self.info[self.nomeF] = self.porcentagemF
                            resultado.append((self.imagem_url, self.nomeF, self.porcentagemF))
                            contador += 1

                            # Imprimir as informações extraídas
                            # print("URL da imagem:", f"{self.imagem_url}")
                            # print("Nome:", nomeF)
                            # print("Porcentagem:", self.porcentagemF)
                            # print("-" * 30)
                            
                            

                            if contador % 6 == 0:
                                print('Aguarde 2 minutos')
                                print('--' * 60)
                                sleep(160)
                return resultado
            else:
                print("Falha ao acessar o site:", response.status_code)


bot = Slot()
bot.iniciar()
