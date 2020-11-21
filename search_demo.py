from requests_html import HTMLSession

s = HTMLSession()

key_word = "爱"
search_data = s.get("https://search.douban.com/movie/subject_search?search_text=" + key_word + "&cat=1002")