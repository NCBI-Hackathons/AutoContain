import tornado.ioloop
import tornado.web
import json
import os

import generateFiles
import dockerUtils

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")

    def get(self):
        self.write('AutoContain APIs')

class CondaHandler(BaseHandler):
    def get(self, filePath):
        with open("packages/conda/" + filePath) as f:
            data = json.load(f)

        condaPackages = {}
        packages = data["packages"]

        for package in packages:
            name = packages[package]["name"]
            version = packages[package]["version"]

            try:
                if version not in condaPackages[name]["versions"]:
                    condaPackages[name]["versions"].append(version)
            except:
                condaPackages[name] = {
                    "versions": [
                        version
                    ]
                }
        self.write(json.dumps(condaPackages))

class SubmitHandler(BaseHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        folderPath = str(data['id'])
        os.makedirs(folderPath)
        dockerfile = generateFiles.run(data, folderPath)
        self.write(dockerfile)

        dockerUtils.build_docker(folderPath)
        dockerUtils.push_docker(folderPath)

def make_app():
    return tornado.web.Application([
        (r"/", BaseHandler),
        (r"/packages/(.*)", CondaHandler),
        (r"/submit", SubmitHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()