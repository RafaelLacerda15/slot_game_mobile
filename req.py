import requests
from bs4 import BeautifulSoup
from time import sleep


# Fazer um FOR com um RANGE() para buscar os slots das provedoras e fazer uma função para puxar de acordo com o que foi selecionado.

class Slot:
    def __init__(self,):
        self.url = "https://ssspaga.com"
        self.info = {}

    # Função PGSoft
    async def pg(self):
        print('Iniciando')
        while True:
            resultado_pg = []
            try:
                # Enviar solicitação GET para o site
                response = requests.get(self.url)
                # Verificar se a solicitação foi bem-sucedida (código de status 200)
                if response.status_code == 200:
                    # Criar objeto BeautifulSoup para analisar o conteúdo HTML
                    soup = BeautifulSoup(response.text, "html.parser")

                    # Encontrar todos os elementos que contêm as informações desejadas
                    provedora = soup.find("div", id="pgsoft")
                    contador = 0
                    if provedora:
                        produtos = provedora.find_all("div", class_="game__item")
                        # Iterar sobre os elementos encontrados e extrair as informações
                        for produto in produtos:
                            # Nome do produto
                            nome = produto.find("div", class_="game__name")
                            self.nomeF = nome.text
                            # URL da imagem do produto
                            imagem_url = produto.find("div", class_="game__img")
                            self.imagem_certa = imagem_url.find('img')['src']
                            
                            # Porcentagem do produto (se aplicável)
                            porcentagem = produto.find("div", class_="game__percent--number")
                            self.porcentagemF = porcentagem.text

                            if self.porcentagemF in ['98%', '99%']:

                                if self.nomeF not in self.info:
                                    self.info[self.nomeF] = self.porcentagemF
                                    resultado_pg.append((self.imagem_certa, self.nomeF, self.porcentagemF))
                                    contador += 1

                                    # Imprimir as informações extraídas
                                    print("URL da imagem:", self.imagem_certa)
                                    print("Nome:", self.nomeF)
                                    print("Porcentagem:", self.porcentagemF)
                                    print("-" * 30)

                    return resultado_pg
                else:
                    print("Falha ao acessar o site:", response.status_code)
            except requests.RequestException as e:
                print("Falha ao acessar o site:", e)
          
    # Função PragmaticPlay
    async def pragmatic(self):
        print('Iniciando')
        while True:
            resultado_prag= []
            try:
                # Enviar solicitação GET para o site
                response = requests.get(self.url)
                # Verificar se a solicitação foi bem-sucedida (código de status 200)
                if response.status_code == 200:
                    # Criar objeto BeautifulSoup para analisar o conteúdo HTML
                    soup = BeautifulSoup(response.text, "html.parser")

                    # Encontrar todos os elementos que contêm as informações desejadas
                    provedora = soup.find("div", id="pragmatic")
                    contador = 0
                    if provedora:
                        produtos = provedora.find_all("div", class_="game__item")
                        # Iterar sobre os elementos encontrados e extrair as informações
                        for produto in produtos:
                            # Nome do produto
                            nome = produto.find("div", class_="game__name")
                            self.nomeF = nome.text
                            # URL da imagem do produto
                            imagem_url = produto.find("div", class_="game__img")
                            self.imagem_certa = imagem_url.find('img')['src']
                            
                            # Porcentagem do produto (se aplicável)
                            porcentagem = produto.find("div", class_="game__percent--number")
                            self.porcentagemF = porcentagem.text

                            if self.porcentagemF in ['97%', '98%', '99%']:

                                if self.nomeF not in self.info:
                                    self.info[self.nomeF] = self.porcentagemF
                                    resultado_prag.append((self.imagem_certa, self.nomeF, self.porcentagemF))
                                    contador += 1

                                    # Imprimir as informações extraídas
                                    print("URL da imagem:", self.imagem_certa)
                                    print("Nome:", self.nomeF)
                                    print("Porcentagem:", self.porcentagemF)
                                    print("-" * 30)

                    return resultado_prag
                else:
                    print("Falha ao acessar o site:", response.status_code)
            except requests.RequestException as e:
                print("Falha ao acessar o site:", e)
        
    # Iniciar a função
    async def iniciar(self):
        print('Iniciando')
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
                            print("URL da imagem:", f"{self.imagem_url}")
                            print("Nome:", self.nomeF)
                            print("Porcentagem:", self.porcentagemF)
                            print("-" * 30)
                            
                return resultado
            else:
                print("Falha ao acessar o site:", response.status_code)

# bot = Slot()
# bot.pragmatic()