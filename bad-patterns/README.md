# Writeup DamCTF 2021 - bad-patterns

---

## Information:


**CTF Name:** DamCTF

**CTF Challenge:** misc/bad-patterns

**Challenge Category:** Misc

**Challenge Points:** 235

**By:** BaboonWithTheGoon

**DamCTF 2021**


---


```bash
A hacker was too lazy to do proper encryption. However, they left us some examples of how their encryption "algo" was supposed to work.

original text : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

encoded: "Lpthq jrvym!frpos"vmt!cpit-"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu"oebpth$eu"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp"oebptlw okvm vv#eljsxmp!g{$eb"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo"svojfhrt-"vynu"lr dwota!sxm phimcjc#hetguynu"pslmkw$aokp$ie"hwt!ndfoswp2"

Find the pattern!

Maybe you should try the same pattern on this string:

bagelarenotwholewheatsometimes

Make sure you wrap your solution with `dam{...}`!

Author: BaboonWithTheGoon
```

Both the original text and ciphertext are given. And we need to find the key.We are presented with the original text and the encoded one in this challenge. According to the challenge description, this encoding was done by a lazy hacker who did not use proper encryption.

```
Lorem i -> the original text.

Lpthq j -> the encoded text.
```

...

```
L becomes L which comes from L + 0 = L

o becomes p which comes from o + 1 = p

r becomes t which comes from r + 2 = t

e becomes h which comes from e + 3 = h

m becomes q which comes from m + 4 = q

” ” becomes ” ” which comes from ” ” + 0 = ” “

i becomes j which comes from i + 1 = j
```

This simple pattern repeats itself across the entire text. I decided to create a script to automate the process and check my logic quickly to solve this. 

```python
#!/usr/bin python3

def decode_bad_pattern(s):
    string_size = len(s)
    res = ""
    for i in range(0, string_size, 5):
        res += chr(ord(s[i]) - 0)
        res += chr(ord(s[i+1]) - 1)
        res += chr(ord(s[i+2]) - 2)
        res += chr(ord(s[i+3]) - 3)
        res += chr(ord(s[i+4]) - 4)
    return res


def encode_bad_pattern(s):
    string_size = len(s)
    res = ""
    for i in range(0, string_size, 5):
        res += chr(ord(s[i]) + 0)
        res += chr(ord(s[i+1]) + 1)
        res += chr(ord(s[i+2]) + 2)
        res += chr(ord(s[i+3]) + 3)
        res += chr(ord(s[i+4]) + 4)
    return res

print(encode_bad_pattern("bagelarenotwholewheatsometimes"))
```

The first function decodes the “bad pattern” and encodes it.
As you can see, we have the same logic in this code as in the explanation above. We call the function **decode_bad_patterns** on the initial encoded text to test if this code was correct. It worked. 

**output:**
```
bbihpasgqstxjrpexjhettqpitjohw
```

### ***Another way:***

```python
#!/usr/bin/env python3
# get pattern
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

encoded = "Lpthq jrvym!frpos\"vmt!cpit-\"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu\"oebpth$eu\"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp\"oebptlw okvm vv#eljsxmp!g{$eb\"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf\"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo\"svojfhrt-\"vynu\"lr dwota!sxm phimcjc#hetguynu\"pslmkw$aokp$ie\"hwt!ndfoswp2"

pattern = ""

for i in range(encoded.__len__()):
    pattern+= str(ord(encoded[i]) - ord(text[i]))

print(pattern)
```

**output:**

```
0123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234012340123401234

```
That was a good guess! The key is 1234 repeated throughout the sentence.

Let's try to decode the cypher they gave us:

```python
encoded = "Lpthq jrvym!frpos\"vmt!cpit-\"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu\"oebpth$eu\"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp\"oebptlw okvm vv#eljsxmp!g{$eb\"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf\"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo\"svojfhrt-\"vynu\"lr dwota!sxm phimcjc#hetguynu\"pslmkw$aokp$ie\"hwt!ndfoswp2"

pattern = "01234"

text = ""

for i in range(encoded.__len__()):
    text+= chr(ord(encoded[i]) - int(pattern[i % 5]))

print(text)
```


We got the plain text back, the last thing we need to do is to encode `bagelarenotwholewheatsometimes` as mentioned in the description:

```python
text = "bagelarenotwholewheatsometimes"
pattern = "01234"
encoded = ""

for i in range(text.__len__()):
    encoded+= chr(ord(text[i]) + int(pattern[i % 5]))

print(encoded)
```
**output:**
```
bbihpasgqstxjrpexjhettqpitjohw
```


#### **Flag:** 

```
dam{bbihpasgqstxjrpexjhettqpitjohw}
```
