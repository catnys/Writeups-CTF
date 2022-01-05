# GET aHEAD

---

### **Author:** Madstacks
### **Category:** Web Exploitation

![](https://i.imgur.com/RSneQKR.png)


---

# Description

Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:15931/


---

# Solution

Hello everyone, today we will have a look at another picoCTF. 

if we try to open the given link, we would get:

![](https://i.imgur.com/C74iB2l.png)

first thing we should inspect the webpage so that lets see if we have get some clue or not.


![](https://i.imgur.com/OAlkfBb.jpg)

I guess I'm right :), we have a link and if we click this link up

```
maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css
```

![](https://i.imgur.com/FgfBbtP.png)

this looks so complicated. However, at that point we should focus on HEAD request.

```
root@immalegend:~$ curl -I HEAD -i http://mercury.picoctf.net:15931/index.php
curl: (6) Could not resolve host: HEAD
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_82880908}
Content-type: text/html; charset=UTF-8
```

as you can see we get flag easily.

**Flag:**
```
picoCTF{r3j3ct_th3_du4l1ty_82880908}
```



