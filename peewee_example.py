""" пример использования peewee
"""
import os
from peewee import *
from playhouse.sqlite_ext import *

curdir = os.getcwd()
dbfile = curdir + "\\sample.db"
db = SqliteExtDatabase(dbfile)
ext_lib = "closure.dll"
print(ext_lib)
db.load_extension(ext_lib)

class BaseMode(Model):
    class Meta:
        database = db

class Category(BaseMode):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=150)
    parent = ForeignKeyField('self', related_name="child", null=True)
    class Meta:
        db_table = "Categories"
    
class Book(BaseMode):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=250)
    link = CharField(max_length=250, null=True)
    category = ForeignKeyField(Category, related_name="books", null=True)
    class Meta:
        db_table = "Books"
    
CategoryClosure = ClosureTable(Category)

db.create_tables([Category, Book, CategoryClosure], True)
cat = Category.create(name=u"Все книги")
book = Book.create(name=u"Моя крутая книга по Python", category=cat)
print(cat.name)
print(book.name)

books = Category.select().where(Category.id==1)
print(books)
all_descendants = (Category
                   .select()
                   .join(CategoryClosure, on=(Category.id == CategoryClosure.id))
                   .where(CategoryClosure.root == books))
print([ct.name for ct in all_descendants])