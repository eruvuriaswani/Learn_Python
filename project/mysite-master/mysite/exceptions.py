# -*- coding: utf-8 -*-

class FSLException(Exception):
    """ The base class for all exceptions in the project

    :param _message: the exception message, can be overwrite in subclass to offer a generic message.
    :param kwargs: the user data
    """
    def __init__(self, _message='', **kwargs):
        self.message = _message
        self.data = kwargs

    def __str__(self):
        res = [str(self.errno)]
        if self.message:
            res.append(str(self.message))
        if self.data:
            res.append('&'.join(['%s<%s>=%s' % (k, type(self.data[k]).__name__, self.data[k])
                                 for k in sorted(self.data)]))
        return ':'.join(res)


class Errno(object):
    """A errno descriptor that set and return value
    """

    def __init__(self, errno):
        self.errno = errno

    def __get__(self, instance, owner):
        return self.errno

    def __set__(self, instance, value):
        pass

    def __del__(self):
        pass





class _RuntimeException(FSLException):
    """ errno (300, 400)
    """
    pass


class TimeoutExc(_RuntimeException):
    errno = Errno(301)


class FileTransferFail(_RuntimeException):
    errno = Errno(303)

    def __init__(self, _message='', **kwargs):
        if not _message:
            _message = 'File transfer failed'
        super(FileTransferFail, self).__init__(_message, **kwargs)



class ObjectNotFound(_RuntimeException):
    errno = Errno(306)

    def __init__(self, _message='', **kwargs):
        if not _message:
            _message = 'The object can not be found'
        super(ObjectNotFound, self).__init__(_message, **kwargs)


def _timeout():
    raise TimeoutExc("Timeout for query.")
