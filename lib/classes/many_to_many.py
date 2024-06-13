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
        if not isinstance(title, str):
            raise TypeError('title must be a string')
        elif len(title) < 5 or len(title) > 50:
            raise ValueError('title must be between 5 and 50 characters')
        elif hasattr(self, "title"):
            raise AttributeError("title must not already exist")
        else:
            self._title = title
            return 
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author is not an Author")            
        self._author = author
        return
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("input must be a Magazine")
        self._magazine = magazine
        return
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif len(name) == 0:
            raise ValueError("name cannot be blank")
        elif hasattr(self, "name"):
            raise AttributeError("name must not already exist")
        else:
            self._name = name
            return
    
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
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif len(name) > 16 or len(name) < 2:
            raise ValueError("name must be 2 to 16 characters long")
        else:
            self._name = name
            return        
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        elif len(category) == 0:
            raise ValueError("category cannot be left blank")
        else:
            self._category = category
            return
        
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