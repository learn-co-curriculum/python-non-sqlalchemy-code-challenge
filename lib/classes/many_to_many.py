class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self.title = title
        self.magazine.articles.append(self)

    def set_title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self.title = new_title

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self.name = name
        self.articles = []

    def articles(self):
        return self.articles.copy()

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance")
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article

    def topic_areas(self):
        if not self.articles:
            return None
        return list(set(article.magazine.category for article in self.articles))

class Magazine:
    magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self.name = name
        self.category = category
        self.articles = []
        Magazine.magazines.append(self)

    def articles(self):
        return self.articles.copy()

    def contributors(self):
        authors = [article.author for article in self.articles]
        return [author for author in set(authors) if authors.count(author) > 2] or None

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        authors = [article.author for article in self.articles]
        return [author for author in set(authors) if authors.count(author) > 2] or None