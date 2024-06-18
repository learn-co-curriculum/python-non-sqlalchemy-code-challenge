class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and (5 <= len(new_title) <= 50) and not hasattr(self, "title"):
            self._title = new_title

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, "name"):
            self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author is self]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self): 
        first_list = [article.magazine for article in Article.all if article.author is self]
        if len(first_list) > 0:
            return list(set([magazine.category for magazine in first_list])) 
        else:
            return None
        

class Magazine:
    def __init__(self, name, category):
         all = []
         self.name = name
         self.category = category

    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category
    @category.setter 
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
       


    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self]))

    def article_titles(self):
        list_o_titles = [article.title for article in Article.all if article.magazine is self]
        if len(list_o_titles) > 0:
            return list_o_titles
        else:
            return None

    def contributing_authors(self): 
        all_contributors = [article.author for article in Article.all if article.magazine is self]
        for element in all_contributors:
            if all_contributors.count(element) >= 2:
                return [element for element in all_contributors]
            else: 
                return None