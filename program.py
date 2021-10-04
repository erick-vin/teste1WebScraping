import urllib.request #importa a biblioteca usada para consultar uma URL
from bs4 import BeautifulSoup #importa as funções BeautifulSoup para analisar os dados retornados do site
import wget #importa a biblioteca usada para realizar o download do pdf através do link

def downloand_file(download_url):

    # Função para baixar o arquivo
    # Padrão Tiss em pdf através do url

    wget.download(download_url)

def searchLink(url, parameter1, parameter2):

    # Função que faz a busca de todas os links na
    # pagina e me retorna o link que preciso de acordo
    # com os paramentros definidos

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    all_links = soup.find_all('a')
    count = 0
    linkComplement = ""
    for link in all_links:

        #Procura link por link dentro da página
        #e realiza o filtro abaixo para captura o link desejado

        if parameter1 in str(link.get('href')):
            if parameter2 in str(link.get('href')):
                while count < 1:
                    linkComplement = str(link.get('href'))
                    count = count + 1
    return linkComplement

#link inicial passando no edital do text, apartir
# desse link faremos a busca
linkPageTiss = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'

#Os dois parametros abaixo são os que filtram e definem o link
# para direcionar para a página onde se encontra o link do pdf
parameterSearch1 = "padrao-tiss-"
parameterSearch2 = "2021"

linkDefaultPageTiss = searchLink(linkPageTiss, parameterSearch1, parameterSearch2)

linkDefaultPageTiss = linkPageTiss[0:21] + linkDefaultPageTiss
print(linkDefaultPageTiss)
print("_______________________________")

#Os dois parametros abaixo são os que filtram e definem o link
# para direcionar para a página onde se encontra o pdf
parameterSearch1 = "Padrão_TISS_Componente_Organizacional"
parameterSearch2 = ".pdf"

defaultLinkTissPdf = searchLink(linkDefaultPageTiss, parameterSearch1, parameterSearch2)

defaultLinkTissPdf = linkPageTiss[0:21] + defaultLinkTissPdf
print(defaultLinkTissPdf)

downloand_file(defaultLinkTissPdf)