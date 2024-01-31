
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class GrandScrapperInvest():

	def valor_investe(self):

		html = BeautifulSoup(
		 requests.get('https://valorinveste.globo.com/').content, 'html.parser')

		l = [i for i in html.find_all('a')]
		
		d = [{
		 'title': i['title'],
		 'link': i['href'],
		} for i in l if 'title' in i.attrs.keys()]

		for i in d:

			i['title'] = i['title'].strip()
		
		return([i for i in d if len(i['title']) > 24])

	def infomoney(self):

		html = BeautifulSoup(
		 requests.get('https://www.infomoney.com.br/ultimas-noticias/').content,
		 'html.parser')

		l = [i.attrs for i in html.find_all('a')]

		d = [{
		 'title': i['title'],
		 'link': i['href']
		} for i in l if 'title' in i.keys() and len(i['title']) > 24]

		for i in d:

			i['title'] = i['title'].strip()

		d = [dict(t) for t in {tuple(i.items()) for i in d}]
		
		return(d)

	def suno(self):

		html = BeautifulSoup(
		 requests.get(
		  'https://www.suno.com.br/noticias/',
		  headers={
		   'User-Agent':
		   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
		  }).content, 'html.parser')

		l = [i for i in html.find_all('a')]

		d = [{
		 'title': i.string,
		 'link': i['href']
		} for i in l if 'href' in i.attrs.keys() and i.string != None]

		for i in d:

			i['title'] = i['title'].strip()

		return([i for i in d if len(i['title']) > 27])

	def inteligencia_financeira(self):

		html = BeautifulSoup(
		 requests.get('https://inteligenciafinanceira.com.br/saiba/').content,
		 'html.parser')

		l = [i for i in html.find_all('a')]

		d = [{
		 'title': i.string,
		 'link': i['href']
		} for i in l if 'href' in i.attrs.keys()]

		d = [i for i in d if i['title'] != None]

		for i in d:

			i['title'] = i['title'].strip()

		return([i for i in d if len(i['title']) > 40])

	def invest_news(self):

		html = BeautifulSoup(
		 requests.get('https://investnews.com.br/ultimas/').content, 'html.parser')

		l = [i for i in html.find_all('a')]

		d = [{
		 'link': i['href']
		} for i in l if 'rel' in i.attrs.keys() and len(i['href']) > 35]

		for i in d:

			i['title'] = i['link'].split('/')[4].replace('-', ' ').title().strip()

		return(d)

	def seu_dinheiro(self):

		html = BeautifulSoup(
		 requests.get('https://www.seudinheiro.com/ultimas/').content, 'html.parser')

		l = [i for i in html.find_all('a')]

		d = [{
		 'title': i.string,
		 'link': i['href']
		} for i in l]  # if 'href' in i.attrs.keys()]

		d = [i for i in d if i['title'] != None]

		for i in d:

			i['title'] = i['title'].strip()

		return ([i for i in d if len(i['title']) > 40])

	def money_times(self):

		html = BeautifulSoup(
		 requests.get('https://www.moneytimes.com.br/ultimas-noticias/').content,
		 'html.parser')

		l = [i for i in html.find_all('a')]

		d = [{
		 'title': i.string,
		 'link': i['href']
		} for i in l]  # if 'href' in i.attrs.keys()]

		d = [i for i in d if i['title'] != None]

		for i in d:

			i['title'] = i['title'].strip()

		return ([i for i in d if len(i['title']) > 35])

	def trademap(self):

		html = BeautifulSoup(
		 requests.get('https://trademap.com.br/agencia').content, 'html.parser')

		l = [i for i in html.find_all('a')]

		d = [{
		 'title': i.string,
		 'link': i['href']
		} for i in l]  # if 'href' in i.attrs.keys()]

		d = [i for i in d if i['title'] != None]

		for i in d:

			i['title'] = i['title'].strip()
		
		return([i for i in d if len(i['title']) > 40])

class GsiMessage(GrandScrapperInvest):

	def create_message(self):

		veicules = {
			'Invest News': self.invest_news(),
			'TradeMap': self.trademap(),
			'Inteligência Financeira': self.inteligencia_financeira(),
			'Suno': self.suno(),
			'Seu Dinheiro': self.seu_dinheiro(),
			'Valor Investe': self.valor_investe(),
			'Money Times': self.money_times(),
			'InfoMoney': self.infomoney()
		}

		l = []
		
		for i in veicules.keys():

			body = '\n\n'.join([i['title'] + '\n' + '_' + i['link'] + '_' for i in veicules.get(i)])

			body = f'\n\n*{i}*\n\n' + body

			l.append(body)
				
		f = open(f'data/{str(int(datetime.now().timestamp()))}.txt', 'w', encoding = 'utf-8')

		f.write(''.join(l))

		f.close()
					
GsiMessage().create_message()
