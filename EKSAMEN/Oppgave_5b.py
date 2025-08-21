alfabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,æ,ø,å,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,Æ,Ø,Å".split(",")
# print(alfabet)


def behandleTekst(tekst, n):
    nyTekst = ""
    for bokstav in tekst:
        if bokstav in alfabet:
            nyBokstav = manipulerBokstav(bokstav, n)
            nyTekst = nyTekst + str(nyBokstav)
            # print(alfabetet.index(bokstav)+1)
        else:
            nyTekst += bokstav
    return nyTekst

def manipulerBokstav(bokstav,n):
    alfabetet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,æ,ø,å,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,Æ,Ø,Å".split(",")
    posisjon = alfabetet.index(bokstav)
    nyPosisjon = (posisjon + n) % 29
    return print(alfabetet[nyPosisjon])

behandleTekst("Hei på deg",3)

# manipulerBokstav("a",1)