from OpenCVR.OpenCVRAPI \
    import OpenCVRAPI

from requests \
    import get

from OpenCVR.Labels \
    import \
    url_country_parameter, \
    api_url, \
    url_vat_parameter, \
    url_format_parameter


class SearchByCVRInRegistry:
    def __init__(
            self,
            configuration: OpenCVRAPI,
            search_by_cvr: str
    ):
        self.configuration = configuration
        self.search_by_cvr = search_by_cvr

        self.content = None

    def payload(self):
        return {
            url_country_parameter: self.configuration.get_country(),
            url_vat_parameter: self.search_by_cvr,
            url_format_parameter: self.configuration.response_format
        }

    def call(self):
        retrieve_request = get(
            api_url,
            headers=self.generate_header(),
            params=self.payload()
        )

        if retrieve_request.status_code == 200:
            self.content = retrieve_request.text
        else:
            raise Exception('')

    def generate_header(self):
        return {
            'User-Agent': self.configuration.get_user_agent(),
            'From': self.configuration.get_contact()
        }

