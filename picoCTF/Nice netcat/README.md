# Nice netcat...

Category:`General Skills`
Author: `SYREAL`

---

## Description

There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 35652, but it doesn't speak English...

## :bulb: Solution

Connecting to the port given with the `netcat` command, and that gives us an output of a set of several integers.
#### **Command**

`nc mercury.picoctf.net 35652`

#### **Output**

```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
57 
98 
51 
98 
55 
51 
57 
50 
125 
10
```
Seeing as all these numbers are in decimal range, we can throw them into [***Cyberchef***](https://gchq.github.io/CyberChef/)  with the recipe "From Decimal" to `ASCII`

#### **Flag**

`picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}`

---
# An Alternate Solution

These numbers are ASCII values in text, so we can write python script to convert them into flag.

```python
num = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 55, 99, 48, 56, 50, 49, 102, 53, 125, 10]
flag = ""
for number in num:
    flag += chr(number)
print(flag)
```
