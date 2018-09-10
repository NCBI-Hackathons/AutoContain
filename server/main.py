import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class CondaHandler(tornado.web.RequestHandler):
    def get(self, filePath):
        with open(filePath) as f:
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

        self.write(condaPackages)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/packages/(.*)", CondaHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()