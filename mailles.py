def ajouteDroite( laLigne , caractere):
    laLigne.append(caractere)
    return laLigne
def ajouteGauche( laLigne , caractere):
    reponse = [caractere]
    for k in laLigne :
        reponse.append(k)
    return reponse

def affiche(ligne):
    for k in ligne :
        print(k , end='')

nombreMaillesAReduire = int(input('Entrez le nombre de mailles à réduire'))
nombreMaillesReduit = int(input('Entrez le nombre de mailles de la ligne réduite'))
maillesDoubles = nombreMaillesAReduire - nombreMaillesReduit - 2
maillesSimples = nombreMaillesReduit - maillesDoubles
nombreMotifs = maillesDoubles-1
maillesSimplesDansMotif = maillesSimples // nombreMotifs
maillesQuiRestent = maillesSimples - maillesSimplesDansMotif * nombreMotifs
attente = nombreMotifs - maillesQuiRestent
print('mailles double : ', maillesDoubles)
print('mailles simples : ', maillesSimples)
print('nombre de motifs : ' , nombreMotifs)
print('nombre de o dans motif : ', maillesSimplesDansMotif)
print('mailles qui restent : ', maillesQuiRestent)
if nombreMotifs%2==0 :
    ligne=['X']
else :
    ligne=['X']
    for k in range(maillesSimplesDansMotif):
        ligne = ajouteDroite(ligne , 'o')
    if attente != 0:
        attente = attente - 1
    else :
        ligne = ajouteDroite(ligne, 'o')
    ligne = ajouteDroite(ligne , 'X')
#affiche(ligne)
print('')
for k in range(nombreMotifs // 2):
    for l in range(maillesSimplesDansMotif):
        ligne = ajouteDroite( ligne , 'o')
    if attente != 0:
        attente = attente - 1
    else :
        ligne = ajouteDroite(ligne, 'o')
    ligne = ajouteDroite(ligne, 'X')
    #affiche(ligne)
    #print('')
    for l in range(maillesSimplesDansMotif):
        ligne = ajouteGauche( ligne , 'o')
    if attente != 0:
        attente = attente - 1
    else :
        ligne = ajouteGauche(ligne, 'o')
    ligne = ajouteGauche(ligne, 'X')
affiche(ligne)
