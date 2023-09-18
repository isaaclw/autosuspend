import logging
from typing import Any, Optional


def logger_by_class(klass: type, name: Optional[str] = None) -> logging.Logger:
    return logging.getLogger(
        "{module}.{klass}{name}".format(
            module=klass.__module__,
            klass=klass.__name__,
            name=f".{name}" if name else "",
        )
    )


def logger_by_class_instance(
    instance: Any,
    name: Optional[str] = None,
) -> logging.Logger:
    return logger_by_class(instance.__class__, name=name)
