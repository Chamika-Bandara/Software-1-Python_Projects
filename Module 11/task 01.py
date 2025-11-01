from classes.publication import Book, Magazine

publications = []
publications.append(Magazine('Donald Duck', 'Aki Hyyppä'))
publications.append(Book('Compartment No. 6', 'Rosa Liksom', 192))

for i, e in enumerate (publications):
    e.print_information()
    print()




