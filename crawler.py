# early Google-like web crawler and social network building
import requests

def find_last(s,t): 
# input search (s) and target (t) string, returns last position of s in t or -1 if not found
	if s.find(t) == -1:
		return -1
	position = 0
	while s.find(t,position + 1) != -1:
		position += 1
	return position

def get_page(url):
  response = requests.get(url)
  data = response.text
  return data

def get_next_target(s):
# finds links in string s (webpage source code obtained from get_page)
	target = find_last(s,'<a href=')
	if target == -1:
		return None, None
	startlink = s.find('"',target)
	endlink = s.find('"',startlink+1)
	url = s[startlink+1:endlink]
	page = s[:target]
	return url, page

def get_links(page):
# gets all of the links from a webpage's source code (a long string)
# and outputs a list of links as strings
	url, page = get_next_target(page)
	links = []
	while url:
		links.append(url)
		url, page = get_next_target(page)
	if len(links) == 0:
		return None
	return links

def crawl_web(link_list):
	to_crawl = link_list
	crawled = []
	while to_crawl:
		page = to_crawl.pop()
		if page not in crawled:
			crawled.append(page)
			new_links = get_links(get_page(page))
			if new_links:
				for url in new_links:
					if url not in crawled:
						if url not in to_crawl:
							to_crawl.append(url)
	return crawled


### MAIN PROGRAM
page_data = get_page('https://udacity.github.io/cs101x/index.html') #Nice little test set of pages
mylist = get_links(page_data)
crawled = crawl_web(mylist)
for i in crawled:
	print(i)