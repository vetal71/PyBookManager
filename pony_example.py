"""
пример  
"""
from pony.orm import *


db = Database()


class Category(db.Entity):
    _table_ = 'Categories'
    id = PrimaryKey(int, auto=True)
    categoryname = Required(str, 100, column='name')
    categories = Set('Category', reverse='parent')
    parent = Optional('Category', column='parent_id', reverse='categories')
    books = Set('Book')


class Book(db.Entity):
    _table_ = 'Books'
    id = PrimaryKey(int, auto=True)
    bookname = Required(str, 200, column='name')
    booklink = Optional(str, 250, nullable=True)
    category = Required(Category, column='category_id')


db.bind("sqlite", "BookLibrary.db", create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def populate_database():
    cat_root = select(c for c in Category if c.categoryname=="Книги")
    if cat_root == None:
        cat_root = Category(categoryname="Книги")
    #book = Book(bookname="Лучшая книга про python", category=[cat_root])

@db_session
def test_queries():
    print('All Category')
    result = select((c.id, c.categoryname) for c in Category)[:]
    print(result)

if __name__ == '__main__':
    """with db_session:
        if Book.select().first() is None:
    """        
    populate_database()
    test_queries()    