import streamlit as st
st.title("Ádám")
szoveg = st.text_input("szöveg")
#Csupa nagybetű, kisbetű
st.write(szoveg.upper())
st.write(szoveg.lower())
#Szavak száma
szavak = szoveg.split(" ")
darab = 0
for i in szavak:
    if i == "":
        continue
    else:
        darab +=1
st.write(f"{darab}")

#Leggyakoribb szó
szavak_szama = {}
for i in szavak:
    if i in szavak_szama:
        szavak_szama[i] += 1
    else:
        szavak_szama[i] = 1
st.write(f"Leggyakoribb szó: {max(szavak_szama, key=szavak_szama.get)}")

#Leggyakoribb betű
betuk_szama = {}
for i in szoveg:
    if i in betuk_szama:
        betuk_szama[i] += 1
    else:
        betuk_szama[i] = 1
if True:
    try: st.write(f"Leggyakoribb betű {max(betuk_szama, key=betuk_szama.get)}")
    except: st.write("")
        
#Betűk száma
betuk_szama = 0
betuk = szoveg.strip()

for i in betuk:
    betuk_szama += 1
st.write(f"Betűk száma: {betuk_szama}")


