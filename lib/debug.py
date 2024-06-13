#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()

class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "title"):
            self._title = title
        else:
            raise AttributeError ("Title must be string 5 to 50 characters long and not already exist")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
            raise AttributeError ("input must be an Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise AttributeError ("input must be a Magazine")
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "name"):
            self._name = name
        else:
            raise AttributeError ("Input must be string and not already exist")
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})


    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        topics = list({magazine.category for magazine in self.magazines()})
        return topics or None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise AttributeError ("Input must be string 2 to 16 characters long")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise AttributeError ("Category must be string")
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        art_titles = [article.title for article in self.articles()]
        return art_titles or None

    def contributing_authors(self):
        author_list = [article.author for article in self.articles()]
        club3pub = [author for author in author_list if author_list.count(author) > 2]
        return club3pub or None