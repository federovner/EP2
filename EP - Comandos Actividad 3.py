scrapy shell
fetch("https://doi.org/10.1371/journal.pone.0005738")

import html2text
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto=converter.handle(response.css('*').get())
texto=texto.encode('ascii', 'ignore')
f1=open("paper1.txt",'wb')
f1.write(texto)
f1.close()

fetch("http://www.gutenberg.org/files/244/244-h/244-h.htm")
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto=converter.handle(response.css('*').get())
texto=texto.encode('ascii', 'ignore')
f2=open("AStudyinScarlet.txt",'wb')
f2.write(texto)
f2.close()

fetch("http://www.gutenberg.org/files/244/244-h/244-h.htm")
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto=converter.handle(response.css('*').get())
texto=texto.encode('ascii', 'ignore')
f2=open("AStudyinScarlet.txt",'wb')
f2.write(texto)
f2.close()

fetch("http://www.gutenberg.org/files/58866/58866-h/58866-h.htm")
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto=converter.handle(response.css('*').get())
texto=texto.encode('ascii', 'ignore')
f3=open("TheMurderontheLinks.txt",'wb')
f3.write(texto)
f3.close()

fetch("http://www.gutenberg.org/files/1695/1695-h/1695-h.htm")
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto=converter.handle(response.css('*').get())
texto=texto.encode('ascii', 'ignore')
f4=open("TheManWhoWasThursday.txt",'wb')
f4.write(texto)
f4.close()

fetch("http://www.gutenberg.org/files/58820/58820-h/58820-h.htm")
converter=html2text.HTML2Text()
converter.ignore_links=True
converter.ignore_images=True
converter.ignore_tables=True
texto=converter.handle(response.css('*').get())
texto=texto.encode('ascii', 'ignore')
f5=open("WhoseBody",'wb')
f5.write(texto)
f5.close()