from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://news.ycombinator.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
noticias=[]

def scrapp(url,h,pagina,maxPagina=3):

    if pagina>maxPagina:
        return
    
    response=requests.get(url,headers=h)
    if response.status_code==200:
        print('La peticion fue exitosa')
        soup=BeautifulSoup(response.text,'html.parser')
        print(soup.prettify())

        titles=soup.find_all('span',class_="titleline")
        for tit in titles:
            score_tag = tit.find_next('span', class_='score')
            noticias.append({
                "title":tit.text,
                "link":tit.find('a').get('href'),
                "point":int(score_tag.text.split()[0]) if score_tag else 0
                }
            )
        more=soup.find('a',class_='morelink')
        if more:
            next_url='https://news.ycombinator.com/' + more['href']
            scrapp(next_url,h,pagina+1,maxPagina)
   

scrapp(url,headers,1,maxPagina=3)        
        
if noticias:
    df=pd.DataFrame(noticias)
    df.to_csv('noticias.csv',index=False)
    print(f'{len(noticias)} noticias guardadas en noticias.csv')

    
    print(f'\n📊 Reporte:')
    print(f'   Total de noticias: {len(noticias)}')
    print(f'   Promedio de puntos: {df["point"].mean():.1f}')
    print(f'   Noticia más popular: {df.iloc[0]["title"]}')
    print(f'   Puntos: {df.iloc[0]["point"]}')
    









  