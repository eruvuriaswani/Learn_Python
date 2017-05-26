# # coding=utf-8
# import chardet
# import ijson
# from apps import config, models, db


# def uploadFile(filename):
#     with open(filename, 'rb') as file:
#         raw = file.read(32)  # at most 32 bytes are returned
#         encoding = chardet.detect(raw)['encoding']
#     print("encoding detected: ", encoding)
#     file = open(filename, encoding='utf-8')
#     apis = ijson.items(file, 'log.entries.item')
#     for api in apis:
#         url = api['request']['url'].lower()
#         if(url.endswith(tuple(config.SKIP_FILE_TYPE))):
#             continue
#         req = models.ApiRequests()
#         req.url = api['request']['url']
#         req.method = api['request']['url']

#         for h in api['request']['headers']:
#             hed = models.Headers()
#             hed.name = h['name']
#             hed.value = h['value']
#             hed.request = req

#         for h in api['request']['cookies']:
#             models.Cookies(h, req)
#         res = api['response']
#         resp = models.ApiResponse(status=res['status'],
#                                   statusText=res['statusText'])

#         for h in res['headers']:
#             hed = models.RespHeaders(h, resp)

#         for h in res['cookies']:
#             models.RespCookies(h, resp)

#         # resp.content = models.Content(res['content'])
#         resp.request = req
#         db.session.add(req)
#         db.session.flush()
#     db.session.commit()


# if __name__ == "__main__":
#     uploadFile(r"C:\Users\johri_m\Desktop\10.112.118.203.har")
