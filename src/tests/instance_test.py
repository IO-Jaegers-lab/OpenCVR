from OpenCVR \
    import Singleton

from OpenCVR.SearchByCVR \
    import SearchByCVRInRegistry

from OpenCVR.SearchByName \
    import SearchByNameInRegistry


def test_create_instance() -> None:
    test = Singleton.get_open_cvr_api()
    assert not test is None


def test_search_for_cvr() -> None:
    test = Singleton.get_open_cvr_api()
    cvr: str = '41157089'

    search = SearchByCVRInRegistry(
        configuration=test,
        search_by_cvr=cvr
    )

    search.call()

    assert not (search.content is None)


def test_search_for_name() -> None:
    test = Singleton.get_open_cvr_api()

    name: str = 'io-jaegers'

    search = SearchByNameInRegistry(
        configuration=test,
        search_by_name=name
    )

    search.call()

    assert not (search.content is None)


