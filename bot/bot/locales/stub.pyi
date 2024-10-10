from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    menu: Menu
    source: Source
    news: News
    back: Back
    lang: Lang

    @staticmethod
    def incorrect_message() -> Literal["""&lt;b&gt;Enter a valid text message&lt;/b&gt;"""]: ...


class Menu:
    create_source: MenuCreate_source
    news_for_hour: MenuNews_for_hour
    news_for_day: MenuNews_for_day
    help: MenuHelp

    @staticmethod
    def start_message() -> Literal["""&lt;b&gt;This is the main menu of the bot for receiving news.&lt;/b&gt;
You can choose your language and get started."""]: ...


class MenuCreate_source:
    @staticmethod
    def button() -> Literal["""Add news source ➕"""]: ...


class MenuNews_for_hour:
    @staticmethod
    def button() -> Literal["""News for the last hour 👀"""]: ...


class MenuNews_for_day:
    @staticmethod
    def button() -> Literal["""News for the last day 👀"""]: ...


class MenuHelp:
    @staticmethod
    def button() -> Literal["""Help 🆘"""]: ...

    @staticmethod
    def message() -> Literal["""In this bot you can make your own news feed by adding tracking links."""]: ...


class Source:
    create: SourceCreate
    save_answer: SourceSave_answer


class SourceCreate:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Send link to RSS news source&lt;/b&gt;"""]: ...


class SourceSave_answer:
    @staticmethod
    def message() -> Literal["""Link saved ✅"""]: ...


class News:
    current: NewsCurrent

    @staticmethod
    def message() -> Literal["""&lt;b&gt;News:&lt;/b&gt;"""]: ...


class NewsCurrent:
    @staticmethod
    def full(*, title, description, link, category, published_at) -> Literal["""&lt;b&gt;{ $title }&lt;/b&gt;
{ $description }

{ $link }

&lt;i&gt;Category: { $category }&lt;/i&gt;
&lt;i&gt;Published at: { $published_at }&lt;/i&gt;"""]: ...

    @staticmethod
    def without_category(*, title, description, link, published_at) -> Literal["""&lt;b&gt;{ $title }&lt;/b&gt;
{ $description }

{ $link }

&lt;i&gt;Published at: { $published_at }&lt;/i&gt;"""]: ...

    @staticmethod
    def without_description(*, title, link, category, published_at) -> Literal["""&lt;b&gt;{ $title }&lt;/b&gt;

{ $link }

&lt;i&gt;Category: { $category }&lt;/i&gt;
&lt;i&gt;Published at: { $published_at }&lt;/i&gt;"""]: ...

    @staticmethod
    def minimal(*, title, link, published_at) -> Literal["""&lt;b&gt;{ $title }&lt;/b&gt;

{ $link }

&lt;i&gt;Published at: { $published_at }&lt;/i&gt;"""]: ...


class Back:
    @staticmethod
    def button() -> Literal["""Back"""]: ...


class Lang:
    @staticmethod
    def ru() -> Literal["""🇷🇺 Русский"""]: ...

    @staticmethod
    def en() -> Literal["""🇬🇧 English"""]: ...

