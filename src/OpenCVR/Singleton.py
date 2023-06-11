from OpenCVR.OpenCVRAPI \
    import OpenCVRAPI

openCVRAPI = None


def get_open_cvr_api() -> OpenCVRAPI | None:
    global openCVRAPI

    if openCVRAPI is None:
        set_open_cvr_api(
            OpenCVRAPI()
        )

    return openCVRAPI


def set_open_cvr_api(value: OpenCVRAPI) -> None:
    global openCVRAPI
    openCVRAPI = value

