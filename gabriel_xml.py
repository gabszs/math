
from xml.dom import minidom

with open(r"C:\Users\Win10\Desktop\python_empowerdata\Dominando_python\modulo_10_manipulando_arquivos\gabriel\gabriel.xml", 'r', encoding='utf-8') as f:
    xml = minidom.parse(f)

""" pega tudo que não comenta e imprime, porém vira um looping
for tag in xml.getElementsByTagName("Listing"):
    print(f"\n{tag.getElementsByTagName('ListingID')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('PublicationType')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('Title')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('TransactionType')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('ListDate')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('LastUpdateDate')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('DetailViewUrl')[0].firstChild.data}")
    print(f"{tag.getElementsByTagName('Featured')[0].firstChild.data}")
    # LOCATION
    for local in xml.getElementsByTagName("Location"):
        print(f"{local.getElementsByTagName('Country')[0].firstChild.data}")
        print(f"{local.getElementsByTagName('State')[0].firstChild.data}")
        print(f"{local.getElementsByTagName('City')[0].firstChild.data}")
        print(f"{local.getElementsByTagName('Neighborhood')[0].firstChild.data}")
        #print(f"{local.getElementsByTagName('PostalCode')[0].firstChild.data}")
        #print(f"{local.getElementsByTagName('Address')[0].firstChild.data}")
    # DETAILS
    for detalhe in xml.getElementsByTagName("Details"):
        print(f"{detalhe.getElementsByTagName('PropertyType')[0].firstChild.data}")
        print(f"{detalhe.getElementsByTagName('Description')[0].firstChild.data}")
        #print(f"{detalhe.getElementsByTagName('RentalPrice')[0].firstChild.data}")
        print(f"{detalhe.getElementsByTagName('ConstructedArea')[0].firstChild.data}")
        print(f"{detalhe.getElementsByTagName('Bedrooms')[0].firstChild.data}")
        print(f"{detalhe.getElementsByTagName('Bathrooms')[0].firstChild.data}")
        print(f"{detalhe.getElementsByTagName('Suites')[0].firstChild.data}")
        #print(f"{detalhe.getElementsByTagName('Garage')[0].firstChild.data}")
    # MEDIA
    for media in xml.getElementsByTagName("Media"):
        print(f"{media.getElementsByTagName('Item')[0].firstChild.data}")
"""


""" PEGANDO TODOS OS CONTEÚDOS DIFERENTES DE NULOS DE ADRESS
lista = []
listaCERTA = []
for tag in xml.getElementsByTagName("Listing"):
    for local in xml.getElementsByTagName("Location"):
        lista.append(local.getElementsByTagName('Address'))
        
for id,content in enumerate(lista):
    if id % 2 == 0:
        listaCERTA.append(content)
    else:
        pass
print(listaCERTA)
"""





""" AQUI TA TUDO ERRADO
listaPrice = []
for tag in xml.getElementsByTagName("Listing"):
    for local in xml.getElementsByTagName("Details"):
        listaPrice.append(local.getElementsByTagName('RentalPrice'))

print(listaPrice)
"""