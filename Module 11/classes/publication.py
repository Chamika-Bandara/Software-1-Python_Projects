class Publication:
    def __init__(self, name):
        self.name= name

class Book(Publication):
    def __init__(self, name, author,page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f' Book: {self.name}')
        print(f' Author: {self.author}')
        print(f' Page Count: {self.page_count}')

class Magazine(Publication):
    def __init__(self, name, new_chief_editor):
        super().__init__(name)
        self.chief_editor = new_chief_editor

    def print_information(self):
        print(f' Magazine: {self.name}')
        print(f' Chief Editor: {self.chief_editor}')

