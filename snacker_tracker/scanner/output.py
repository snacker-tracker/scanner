import requests

class File(object):
  def __init__(self, path):
    path = path.replace("file://", "")
    self.fp = open(path, 'a+')

  def write(self, time, data):
    self.fp.write(",".join([time, data]) + "\r\n")
    self.fp.flush()

class Http(object):
  def __init__(self, uri, token_provider = None):
    self.token_provider = token_provider
    self.uri = uri

  def write(self, time, data):

    if self.token_provider is not None:
      headers = {
        "Authorization": "Bearer " + self.token_provider.token
      }
    else:
      headers = {}

    result = requests.post(
      url = self.uri,
      data = {
        'code': data,
        'scanned_at': time
      },
      headers = headers
    )

    print(result)
