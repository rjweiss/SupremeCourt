from lxml import html
import itertools

def get_writings_links(url):
	doc = html.parse(url)
	root = doc.getroot()
	
	links = []
	for i in root.body.find_class('content-inner')[0].getchildren()[3].getiterator():
	    if i.tag == 'a':
		links.append(i)

	link_names = [link.get('name') for link in links]

	opin_links = links[link_names.index('OPIN')+1:link_names.index('CONCUR')]
	concur_links = links[link_names.index('CONCUR')+1:link_names.index('DISSENT')]
	dissent_links = links[link_names.index('DISSENT')+1:link_names.index('CD')]
	cd_links = links[link_names.index('CD')+1:len(link_names)]

#	opin_links.pop(0)
#	concur_links.pop(0)
#	dissent_links.pop(0)
#	cd_links.pop(0)
	opin_href = [a.get('href') for a in opin_links]
	concur_href = [a.get('href') for a in concur_links]
	dissen_href = [a.get('href') for a in dissent_links]
	cd_href = [a.get('href') for a in cd_links]

def main():
	url = 'http://www.law.cornell.edu/supct/author.php?Alito' #will need to iterate over all of them
	get_writings_links(url)
	
if __name__ = "__main__":
	main()