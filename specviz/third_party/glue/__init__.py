def setup():
    from glue.config import qt_client
    from .viewer import SpecviDataViewer
    qt_client.add(SpecvizDataViewer)
