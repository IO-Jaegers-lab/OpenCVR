from OpenCVR.OpenCVRAPI \
    import OpenCVRAPI

from requests \
    import get

from OpenCVR.Labels \
    import \
    url_country_parameter, \
    api_url, \
    url_request, \
    url_and_parameter, \
    url_vat_parameter


class SearchByCVRInRegistry:
    def __init__(
            self,
            configuration: OpenCVRAPI,
            search_by_cvr: str
    ):
        self.configuration = configuration
        self.search_by_cvr = search_by_cvr

        self.content = None

    def make_url_request(self) -> str:
        final_url = api_url + url_request
        final_url = final_url + url_country_parameter + self.configuration.get_country()
        final_url = append_and_to_request(final_url)
        final_url = final_url + url_vat_parameter + self.search_by_cvr

        return final_url

    def call(self):
        url = self.make_url_request()
        retrieve_request = get(url, headers=self.generate_header())
        self.content = retrieve_request.json()

    def generate_header(self):
        return {
            'User-Agent': self.configuration.get_user_agent(),
            'From': self.configuration.get_contact()
        }


def append_and_to_request(
        append_to_str
) -> str:
    return str(append_to_str + url_and_parameter)
