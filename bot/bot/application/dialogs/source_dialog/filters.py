from pydantic import HttpUrl, ValidationError


def rss_link_filter(text):
    if 'rss' in text:
        HttpUrl(text)
        return text
    raise ValueError()