import urllib.request
from bs4 import BeautifulSoup
import wget

def downloand_file(download_url):
    wget.download(download_url)

def buscarLink(url, parametro1, parametro2):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    all_links = soup.find_all('a')
    count = 0
    link2 = ""
    for link in all_links:
        #print(link.get('href'))

        if parametro1 in str(link.get('href')):
            if parametro2 in str(link.get('href')):
                while count < 1:
                    link2 = str(link.get('href'))
                    count = count + 1
    return link2

linkPaginaTiss = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
parametroBusca1 = "padrao-tiss-"
parametroBusca2 = "2021"

linkPaginaPadraoTiss = buscarLink(linkPaginaTiss, parametroBusca1, parametroBusca2)

linkPaginaPadraoTiss = linkPaginaTiss[0:21] + linkPaginaPadraoTiss
print(linkPaginaPadraoTiss)
print("_______________________________")

parametroBusca1 = "Padrão_TISS_Componente_Organizacional"
parametroBusca2 = ".pdf"

linkPadraoTissPdf = buscarLink(linkPaginaPadraoTiss, parametroBusca1, parametroBusca2)

linkPadraoTissPdf = linkPaginaTiss[0:21] + linkPadraoTissPdf
print(linkPadraoTissPdf)

downloand_file(linkPadraoTissPdf)