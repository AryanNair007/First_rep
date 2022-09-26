from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt
import urllib.request


print('''Choose from what you want to see:-
	1.quotes
	2.top 45 english songs by elle
	3.malayalam songs
	4.hindi songs
	5.english songs by jio savan
	6.pic of the day by bing
	''')

dummy=5
while  dummy>1:

	select=int(input('What would you like to view :'))

	if select==1:
		res=requests.get('http://quotes.toscrape.com/')
		soup=BeautifulSoup(res.text, 'html.parser')
		quotes=soup.find_all('div', {'class' : 'quote'})
		#iterating through the lists of songs 
		count=1
		for q in quotes:
			msg=q.find('span', {'class' : 'text'})
			author=q.find('small', {'class' : 'author'})
			print(f'{count}.',msg.text)
			print(author.text)
			print()
			count+=1

	elif select==2:	
		res=requests.get('https://www.elle.com/culture/music/g25939887/best-songs-2019/')
		soup=BeautifulSoup(res.text, 'html.parser')
		songs=soup.find_all('div', {'class' : 'listicle-slide-hed'})
		#iterating through the lists
		count=1
		for s in songs:
			name=s.find('span', {'class' : 'listicle-slide-hed-text'})
			print(f'{count}.',name.text)
			print()
			count+=1

	elif select==3:
		res=requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/th5xS,pbZQ0_')
		soup=BeautifulSoup(res.text, 'html.parser')
		solist_name=soup.find_all('div', {'class' : 'content-cell num'})
		#iterating through the lists
		count=1
		for s in solist_name:
			name=s.find('p', {'class' : 'song-name ellip'})
			time=s.find('p', {'class' : 'time'})
			album=s.find('p', {'class' : 'album-name ellip'})
			print(f'{count}.',name.text)
			print(f'    album/movie={album.text},    duration={time.text}')
			print()
			count+=1

	elif select==4:
		res=requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_')
		soup=BeautifulSoup(res.text, 'html.parser')
		solist_name=soup.find_all('div', {'class' : 'content-cell num'})
		#iterating through the lists
		count=1
		for s in solist_name:
			name=s.find('p', {'class' : 'song-name ellip'})
			time=s.find('p', {'class' : 'time'})
			album=s.find('p', {'class' : 'album-name ellip'})
			print(f'{count}.',name.text)
			print(f'    album/movie={album.text},    duration={time.text}')
			print()
			count+=1

	elif select==5:
		res=requests.get('https://www.jiosaavn.com/featured/top-jiotunes---english/xXiMISqMjsrfemJ68FuXsA__')
		soup=BeautifulSoup(res.text, 'html.parser')
		solist_name=soup.find_all('div', {'class' : 'content-cell num'})
		#iterating through the lists
		count=1
		for s in solist_name:
			name=s.find('p', {'class' : 'song-name ellip'})
			time=s.find('p', {'class' : 'time'})
			album=s.find('p', {'class' : 'album-name ellip'})
			print(f'{count}.',name.text)
			print(f'    album/movie={album.text},    duration={time.text}')
			print()
			count+=1		

	elif select==6:
		res=requests.get('https://bing.wallpaper.pics/')
		soup=BeautifulSoup(res.text, 'html.parser')
		image_box=soup.find('a', {'class' : 'cursor_zoom'})
		image= image_box.find('img')

		link=image['src']

		filename= dt.now().strftime('%d-%m-%y')
		urllib.request.urlretrieve(link, f'{filename}.jpg')		


