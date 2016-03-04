# -*- coding: utf-8 -*-

import bs4 as BeautifulSoup
import requests


class ColorSystem(dict):
    """
    Provides an interface for a color system.
    """

    def load(self):
        """
        Try to load the data from a pre existing cache file if it exists.
        If the cache does not exist, auto fetch the data and save it in
        the cache for future use.
        """
        raise NotImplementedError

    def refresh(self):
        """
        Refreshes the cached data from the URL provided for this color system.
        """
        raise NotImplementedError

    def request(self, *args, **kwargs):
        """
        Gets the request using the `_url` and converts it into a
        beautiful soup object.

        :param args:            The args to pass on to `requests`.
        :param kwargs:          The kwargs to pass on to `requests`.
        """
        response = requests.request(*args, **kwargs)
        return BeautifulSoup.BeautifulSoup(response.text, "html.parser")
