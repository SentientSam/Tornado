import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world!")

class staticRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("HelloWorld2Index.html")

if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/", basicRequestHandler),
    (r"/Welcome", staticRequestHandler)
  ])

  app.listen(3000)
  print("I am listening on port 3000")
  tornado.ioloop.IOLoop.current().start()