import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

def fetch_blogs(query, limit):
    list_blogger_profiles = []
    list_blogger_urls = []
    output_directory = "Outputs/"
    blogger_url = "http://www.blogger.com/profile-find.g?t=m&q=" + query
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    while len(list_blogger_urls) < limit:
        response = requests.get(blogger_url)
        print(blogger_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            profiles_tag_selector = soup.find_all('dl')
            for tags in profiles_tag_selector:
                profile_url_selector = tags.find('a', href=True)
                blogger_profile_url = "http://www.blogger.com/" + profile_url_selector['href'][1:]
                list_blogger_profiles.append(blogger_profile_url)
            list_blogger_urls.extend(fetch_blog_urls(list_blogger_profiles, limit))
            print(list_blogger_urls)
            list_blogger_profiles = []
            blogger_url_selector = soup.find('a', {'id': 'next-btn'},
                                             href=True)
            if blogger_url_selector:
                blogger_url = blogger_url_selector['href']
            else:
                break
            print(len(list_blogger_urls))
    print(len(list_blogger_urls))
    if os.path.isfile(output_directory + "test1.txt"):
        file_blog_urls = open(output_directory + "blogList.txt", "a+")
    else:
        file_blog_urls = open(output_directory + "blogList.txt", "w")
    for urls in list_blogger_urls:
        file_blog_urls.write(urls + "\n")
    file_blog_urls.close()

def fetch_blog_urls(list_blogger_profiles, limit):
    count = 0
    list_blogger_urls = []
    for profile in list_blogger_profiles:
        if count < limit:
            response = requests.get(profile)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                profile_blog_link_selector = soup.find_all('span', dir=True)
                for profile_blog_links in profile_blog_link_selector:
                    if profile_blog_links['dir'] == 'ltr':
                        blog_links_selector = profile_blog_links.find_all('a', href=True)
                        for blog_links in blog_links_selector:
                            print(blog_links['href'])
                            try:
                                response = requests.head(blog_links['href'], timeout=60)
                                print(response.headers)
                                if response.encoding and (response.encoding == 'ISO-8859-1' or response.encoding == 'UTF-8'):
                                    list_blogger_urls.append(blog_links['href'])
                                    print()
                                    count += 1
                            except Exception as e:
                                print(e)
    print(list_blogger_urls)
    return list_blogger_urls

fetch_blogs("Food", 100)
file_open = open("Outputs/blogList.txt", "a+")
file_open.write("http://f-measure.blogspot.com/" + "\n")
file_open.write("http://ws-dl.blogspot.com/" + "\n")
file_open.close()







