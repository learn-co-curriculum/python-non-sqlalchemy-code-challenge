class Article:
    all = []
    authors = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.add_article_to_all(self)

    @property ## ARTICLE.AUTHOR ###############################################################
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
            if author.name not in Article.authors:
                Article.authors.append(author.name)
            else: pass
        else:
            print("Must be a valid author")
        
    @property ## ARTICLE.MAGAZINE ###############################################################
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            print("Must be a valid magazine")

    @property ## ARTICLE.TITLE ###############################################################
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
            self._title = title
        else:
            print("Title must be a string between 5 and 50 characters")

    @classmethod ## ARTICLE CLASS METHODS ###############################################################
    def add_article_to_all(cls, article):
        cls.all.append(article)
        
        
class Author:
    
    def __init__(self, name):
        self.name = name

    @property ## AUTHOR.NAME ###############################################################
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, 'name'):
            self._name = name
        else:
            print("Author name must be a string with at least 1 character!")
    
    ## AUTHOR.ARTICLES ###############################################################
    def articles(self):

        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) > 0:
            return list({article.magazine.category for article in self.articles()})
        else:
            return None
        

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property ## MAGAZINE.NAME ###############################################################
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <=  16:
            self._name = name
        else:
            print("Magazine name must be a string between 2 and 16 characters")

    @property ## MAGAZINE.CATEGORY ###############################################################
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) >0:
            self._category = category
        else:
            print("Magazine category must be a string that is at least 1 character")  
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self ]

    def contributors(self):
        return list({article.author for article in self.articles()})
        
    def article_titles(self):
        if len(self.articles()) > 0:
            return [article.title for article in self.articles()]
        else:
            None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        if author_count[author] >= 2:
            return [author for author in author_count]
        else:
            None

# author_1 = Author("Carry Bradshaw")
# author_2 = Author("Nathaniel Hawthorne")
# magazine = Magazine("Vogue", "Fashion")
# article_1 = Article(author_1, magazine, "How to wear a tutu with style")
# article_2 = Article(author_1, magazine, "Dating life in NYC")
# article_3 = Article(author_2, magazine, "How to be single and happy")        


# # assert len(author_1.articles()) == 2
# # assert len(author_2.articles()) == 1
# # assert article_1 in author_1.articles()
# # assert article_2 in author_1.articles()
# # assert article_3 not in author_1.articles()
# # assert article_3 in author_2.articles()

# author_1 = Author("Carry Bradshaw")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("AD", "Architecture")
# Article(author_1, magazine_1, "How to wear a tutu with style")
# Article(author_1, magazine_2, "2023 Eccentric Design Trends")
# Article(author_1, magazine_2, "Carrara Marble is so 2020")

# author_1 = Author("Carry Bradshaw")
# author_2 = Author("Giorgio Faletti")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("AD", "Architecture")
# author_1.add_article(magazine_1, "How to wear a tutu with style")
# author_1.add_article(magazine_1, "Dating life in NYC")
# author_1.add_article(magazine_2, "2023 Eccentric Design Trends")

# author_1 = Author("Carry Bradshaw")
# author_2 = Author("Nathaniel Hawthorne")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("AD", "Architecture")
# Article(author_1, magazine_1, "How to wear a tutu with style")
# Article(author_1, magazine_1, "How to be single and happy")
# Article(author_1, magazine_1, "Dating life in NYC")
# Article(author_1, magazine_2, "Carrara Marble is so 2020")
# Article(author_2, magazine_2, "2023 Eccentric Design Trends")

# assert author_1 in magazine_1.contributing_authors()