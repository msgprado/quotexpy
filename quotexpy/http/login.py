from typing import Union, Dict
from quotexpy.http.qxbroker import Browser


class Login(Browser):
    """Class for Quotex login resource."""

    url = ""
    ssid = None
    cookies = None
    base_url = "qxbroker.com"
    https_base_url = f"https://{base_url}"

    async def __call__(self, email, password, proxy: Union[Dict, None]=None):
        """
        Method to get Quotex API login http request.
        :param str username: The username of a Quotex server.
        :param str password: The password of a Quotex server.
        :returns: The instance of :class:`playwright.cookies`.
        """

        self.email = email
        self.password = password
        self.proxy = proxy

        self.ssid, self.cookies = await self.get_cookies_and_ssid()
        return self.ssid, self.cookies
