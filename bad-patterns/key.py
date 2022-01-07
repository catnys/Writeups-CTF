encoded = "Lpthq jrvym!frpos\"vmt!cpit-\"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu\"oebpth$eu\"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp\"oebptlw okvm vv#eljsxmp!g{$eb\"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf\"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo\"svojfhrt-\"vynu\"lr dwota!sxm phimcjc#hetguynu\"pslmkw$aokp$ie\"hwt!ndfoswp2"

pattern = "01234"

text = ""

for i in range(encoded.__len__()):
    text+= chr(ord(encoded[i]) - int(pattern[i % 5]))

print(text)
