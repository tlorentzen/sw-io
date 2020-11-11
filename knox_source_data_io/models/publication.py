from knox_source_data_io.models.model import Model

class Byline:
    """
    A class used to represent a Byline

    ...

    Attributes
    ----------
    name : str
        the author name (default "")
    email : str, optional
        the author email (default "")
    """

    name: str
    email: str

    def __init__(self, values: dict = None, **kwargs):
        values = values if values is not None else kwargs
        self.name = values.get('name')
        self.email = values.get('email', None)


class Paragraph:
    """
    A class used to represent a Paragraph

    ...

    Attributes
    ----------
    kind : str
        the type of paragraph
    value : str
        the paragraph
    """

    kind: str
    value: str

    def __init__(self, values: dict = None, **kwargs):
        """
        Parameters
        ----------
        values : dict
            The class values in dict format (default None)
        kwargs :
            The class values as kwargs arguments
        """

        values = values if values is not None else kwargs
        self.kind = values.get("kind", "")
        self.value = values.get("value", "")


class Article:
    """
    A class used to represent an Article

    ...

    Attributes
    ----------
    id : int
        the article id (default 0)
    title : str
        the article title
    trompet : str
        the article trompet (default "")
    byline : Byline
        the article byline
    paragraphs : list
        a list of paragraph elements
    confidence : float
        a confidence score, describing the confidence of correct data (default 1.0)
    publisher : str
        the publisher
    publishedAt : str
        the article publish date
    publication : str
        the magazine/newspaper where it was published
    extractedFrom : list
        a list of path to source files
    page : int
        the page number where the article was found (default 0)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    id: int
    headline: str
    subhead: str
    byline: Byline
    lead: str
    paragraphs: list
    confidence: float
    extracted_from: list = []
    page: int

    def __init__(self, values: dict = None, **kwargs):
        """
        Parameters
        ----------
        values : dict
            The class values in dict format (default None)
        kwargs :
            The class values as kwargs arguments
        """

        values = values if values is not None else kwargs
        if isinstance(values.get("extracted_from", []), list):
            self.extracted_from = values.get("extracted_from", [])
        self.confidence = values.get("confidence", 1.0)
        self.page = values.get("page", 0)
        self.id = values.get("id", None)
        self.headline = values.get("headline", "")
        self.subhead = values.get("subhead", "")
        self.byline = values.get("byline", None)
        self.lead = values.get("lead", None)
        self.paragraphs = values.get("paragraphs", [])

    def add_paragraph(self, paragraph: Paragraph):
        """Add a paragraph the the article

        It simply adds a paragraph to the list of paragraphs on the article.

        Parameters
        ----------
        paragraph : Paragraph
            an instance of Paragraph containing the required properties.
        """

        if isinstance(paragraph, Paragraph):
            self.paragraphs.append(paragraph)

    def add_byline(self, byline_name: str, byline_email: str = None):
        """Add a byline to the article

        It simply adds a byline to the article.

        Parameters
        ----------
        byline_name : str
            the name of the writer
        byline_email : str
            the email of the writer
        """
        if isinstance(byline_name, str):
            self.byline = Byline(name=byline_name, email=byline_email)

    def add_extracted_from(self, path: str):
        """Add the path to the file used for extraction.

        Parameters
        ----------
        path : str
            the file path
        """
        if isinstance(self.extracted_from, list) and isinstance(path, str) and path not in self.extracted_from:
            self.extracted_from.append(path)


class Publication(Model):
    """
    A class used to represent an Publication

    ...

    Attributes
    ----------

    publishedAt : str
        the article publish date
    publication : str
        the magazine/newspaper where it was published
    publisher : str
        the publisher
    pages : int
        the total number of pages
    articles : list
        a list of articles
    """

    publication: str
    published_at: str
    publisher: str
    pages: int
    articles: list

    def __init__(self, values: dict = None, **kwargs):
        """
        Parameters
        ----------
        values : dict
            The class values in dict format (default None)
        kwargs :
            The class values as kwargs arguments
        """

        values = values if values is not None else kwargs
        self.publisher = values.get("publisher", "")
        self.published_at = values.get("published_at", "")
        self.publication = values.get("publication", "")
        self.pages = values.get("pages", 0)
        self.articles = values.get("articles", [])

    def add_article(self, article: Article):
        """Add a article the publication

        It simply adds a article to the list of articles on the publication.

        Parameters
        ----------
        article : Article
            an instance of Paragraph containing the required properties.
        """

        if isinstance(article, Article):
            self.articles.append(article)
