from OpenCVR.Labels \
    import \
    denmark, \
    default_email, \
    default_user_agent, \
    json


class OpenCVRAPI:
    def __init__(
            self,
            user_agent: None | str = default_user_agent(),
            country: None | str = denmark(),
            contact: None | str = default_email(),
            response_format: str | str = json()
    ):
        self.country: str = country
        self.user_agent: str = user_agent
        self.contact: str = contact
        self.response_format: str = response_format

    def get_country(self) -> None | str:
        return self.country

    def set_country(
            self,
            value: str
    ) -> None:
        self.country = value

    def get_user_agent(self) -> str:
        return self.user_agent

    def set_user_agent(
            self,
            value: str
    ) -> None:
        self.user_agent = value

    def get_contact(self) -> str:
        return self.contact

    def set_contact(
            self,
            value: str
    ):
        self.contact = value
