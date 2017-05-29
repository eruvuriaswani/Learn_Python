# coding=utf-8
import chardet
import ijson
from apps import config, models, db
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
from werkzeug.http import http_date


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = http_date(datetime.now())
        response.headers[
            'Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


def uploadFile(filename, proj):
    with open(filename, 'rb') as file:
        raw = file.read(32)  # at most 32 bytes are returned
        encoding = chardet.detect(raw)['encoding']
    print("encoding detected: ", encoding)
    file = open(filename, encoding='utf-8')
    apis = ijson.items(file, 'log.entries.item')
    for api in apis:
        url = api['request']['url'].lower()
        if(url.endswith(tuple(config.SKIP_FILE_TYPE))):
            continue
        req = models.ApiRequests()
        req.url = api['request']['url']
        req.method = api['request']['url']

        for h in api['request']['headers']:
            hed = models.Headers()
            hed.name = h['name']
            hed.value = h['value']
            hed.request = req

        for h in api['request']['cookies']:
            models.Cookies(h, req)
        res = api['response']
        resp = models.ApiResponse(status=res['status'],
                                  statusText=res['statusText'])

        for h in res['headers']:
            hed = models.RespHeaders(h, resp)

        for h in res['cookies']:
            models.RespCookies(h, resp)

        # resp.content = models.Content(res['content'])
        resp.request = req
        req.project = proj
        req.project_id = req.project.id
        db.session.add(req)
        db.session.flush()
    db.session.commit()


if __name__ == "__main__":
    uploadFile(r"C:\Users\johri_m\Desktop\10.112.118.203.har")
