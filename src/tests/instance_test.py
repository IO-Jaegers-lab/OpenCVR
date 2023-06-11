from OpenCVR \
    import Singleton


def test_create_instance() -> None:
    test = Singleton.get_open_cvr_api()
    assert not test is None
