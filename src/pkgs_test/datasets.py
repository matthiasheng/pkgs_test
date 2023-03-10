import warnings
from importlib import resources


def get_flatland():
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    warnings.warn('This function will be depreciated in future', FutureWarning)
    with resources.path("pkgs_test.data", "flatland.txt") as full_path:
        return full_path
