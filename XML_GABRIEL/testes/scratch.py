# loca = {
#     "Pais": xml.getElementsByTagName("Country"),
#     Estado: ,
#     Cidade: ,
#     Cidade: ,
#     Cidade: ,
#     Cidade: ,
# }

from xml.dom import minidom

local = [
        xml.getElementsByTagName("Country"),
        xml.getElementsByTagName("State"),
        xml.getElementsByTagName("City"),
        xml.getElementsByTagName("Neighborhood"),
        xml.getElementsByTagName("PostalCode"),
        xml.getElementsByTagName("Address"),
    ]

    for count, element in enumerate(local[0]):
        print(f"\n Pais: {local[0][count].firstChild.data}, len: {len(local[0])}",
              # f"\n Estado: {local[1][count].firstChild.data}",
              # f"\n Cidade: {local[2][count].firstChild.data}",
              # f"\n Bairro: {local[3][count].firstChild.data}",
              # f"\n CEP: {local[4][count].firstChild.data}",
              f"\n {count}"
              )
for count, element in enumerate(local[0]):
    print(f"\n Pais: {local[0][count].firstChild.data}",
          f"\n Estado: {local[1][count].firstChild.data}",
          f"\n Cidade: {local[2][count].firstChild.data}",
          f"\n Bairro: {local[3][count].firstChild.data}",
          f"\n CEP: {local[4][count].firstChild.data}",
          f"\n Rua/Endereco: {local[5][count].firstChild.data}",
          f"\n {count}"
          )

print(f'{count}° lista, len: {len(element)}, type:{type(element)}')

for count, tag in enumerate(Listing):
    print(f"\n{tag.getElementsByTagName('ListingID')[0].firstChild.data, count}")
    print(f"{tag.getElementsByTagName('Title')[0].firstChild.data, count}")
    print(f"{tag.getElementsByTagName('TransactionType')[0].firstChild.data, count}")


    def ignore_NoneType(argument):
        if isinstance(argument, None):
            return None
        else:
            return argument.[0].firstChild.data


"""
if type(argument) == type(None):
            return None
        else:
            return argument[0]





"""