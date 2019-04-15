from bs4 import BeautifulSoup
from requests import get
from urllib.request import urlopen

#A crawler for a external link of site,but you cant get href for a links, beause it have a u 'uncrawlable-url'

def links():
	html_page = "https://naruto.fandom.com/wiki/Category:Characters"
	page = urlopen(html_page)
	soup = BeautifulSoup(page, 'html.parser')
	all_a_links = soup.find_all("a", class_="external text")
	links = [a for a in all_a_links]
	print(links)

def main():
	html_doc = "https://naruto.fandom.com/wiki/Category:Characters?from=Fukusuke+Hikyakuya%0AFukusuke+Hikyakuya"
	a_link = "https://naruto.fandom.com/wiki/Category:Characters?from=A"
	b_link = "https://naruto.fandom.com/wiki/Category:Characters?from=Fukusuke+Hikyakuya%0AFukusuke+Hikyakuya"
	c_link = "https://naruto.fandom.com/wiki/Category:Characters?from=Iggy%0AIggy"
	d_link = "https://naruto.fandom.com/wiki/Category:Characters?from=Korobi%0AKorobi"
	e_link = "https://naruto.fandom.com/wiki/Category:Characters?from=Noji%0ANoji"
	f_link = "https://naruto.fandom.com/wiki/Category:Characters?from=Suika%0ASuika"
	g_link = "https://naruto.fandom.com/wiki/Category:Characters?from=Yokozuna%0AYokozuna"

	list_of_links = []
	list_of_links.append(a_link)
	list_of_links.append(b_link)
	list_of_links.append(c_link)
	list_of_links.append(d_link)
	list_of_links.append(e_link)
	list_of_links.append(f_link)
	list_of_links.append(g_link)

	list_of_names = []

	for link in list_of_links:
		page = urlopen(link)
		soup = BeautifulSoup(page, 'html.parser')
		all_a_links = soup.find_all("a", class_="category-page__member-link")
		names = [a.string for a in all_a_links]
		list_of_names.append(names)
	
	print(list_of_names)

if __name__ == '__main__':
	main()