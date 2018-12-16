# early Google-like web crawler and social network building

def find_last(s,t): 
# input search (s) and target (t) string, returns last position of s in t or -1 if not found
	if s.find(t) == -1:
		return -1
	position = 0
	while s.find(t,position + 1) != -1:
		position += 1
	return position

def get_page(url):
  with open('xkcd_about_page.txt', 'r') as myfile: # this is a dummy for now
  	data=myfile.read().replace('\n', '')
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
	url, page = get_next_target(page)
	links = []
	while url:
		links.append(url)
		url, page = get_next_target(page)
	if len(links) == 0:
		return None
	return links

### MAIN PROGRAM
page_data = get_page('dummy') #eventually will be a url
print(get_links(page_data))
