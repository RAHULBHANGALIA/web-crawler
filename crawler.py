from urllib import *
#from os import *
v=urlopen("http://google.com").read()
count=v.count("href=")
totallength=len(v)
startindex=v.index("href=")
endindex=v[startindex:].index(">")+startindex
j=0
i=0
while(j<count):
        startindex=v[i:].index("href=")
        endindex=v[startindex:].index(">")+startindex
        link=v[startindex+5:endindex-1]
        print link
        i=endindex
        j=j+1

file=open("C:\Users\rahi\Music\Playlists","wb")
file.write((urlopen("http://google.com").read()))
        

        
        
        
        
	





