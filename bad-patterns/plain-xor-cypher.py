text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

encoded = "Lpthq jrvym!frpos\"vmt!cpit-\"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu\"oebpth$eu\"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp\"oebptlw okvm vv#eljsxmp!g{$eb\"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf\"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo\"svojfhrt-\"vynu\"lr dwota!sxm phimcjc#hetguynu\"pslmkw$aokp$ie\"hwt!ndfoswp2"

pattern = ""

for i in range(encoded.__len__()):
    pattern+= str(ord(encoded[i]) - ord(text[i]))

print(pattern)
