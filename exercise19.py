import urllib.request as req
url="http://wwwk.eyny.com/index.php"

request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("li",class_="li_orange")
#print(titles.a.string)
with open("data.txt","w",encoding="utf-8")as file:
    for title in titles:
        if title.a !=None:
            print(title.a.string)
            file.write(title.a.string+"\n")
#test
    
