htmlDoc='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baslik</title>
</head>
<body>
    Menu 
    <div class="group1"> <!-- grup olusturuldu -->
        <h1 id="header1"> Operation 1  <!-- header olusturuldu -->
        </h1>
        <ul>
            <li>Menu 1</li> <!-- liste olusturuldu -->
            <li>Menu 2</li> 
            <li>Menu 3</li> 
        </ul>    
    </div>
    <div class="group2">
        <h2 id="header2"> Modules
        </h2>
        <ul>
            <li>Menu 1.1</li>
            <li>Menu 2.1</li>
            <li>Menu 3.1</li>
        </ul>            
    </div>
    <img src="webimage.jpg" alt=""> <!-- pc den görüntü eklenip html e yuklendi. -->
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a> <!-- webden link eklendi. -->
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup=BeautifulSoup(htmlDoc,'html.parser')
#result=soup.prettify()
#result=soup.div.findNextSibling()
#result=soup.div.findChildren()
result=soup.find_all('a')
for link in result:
    print(link)
