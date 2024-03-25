
class Responses:
    """
    A dataclass containing global values to parse results 
    """

    # Text Errors
    PAGE_UNREACHEABLE = "[!!!] Page couldnt be reached."
    PAGE_UNREADEABLE = "[!!!] Page couldnt be accessed but may exist."

    # 100 - 199 Range: ERRORS
    PROBE_ERROR_REQUEST_FAIL = 100 # Error when attempting to get a response from URL
    PROBE_ERROR_REQUEST_FATAL = 101 # Fatal error when parsing URL

    # 200 - 299 Range: SUCCESS
    PROBE_REQUEST_SUCCESS = 200 # Response recieved from URL

