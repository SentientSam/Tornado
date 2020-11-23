import tornado.web
import tornado.ioloop

class basicRequesthandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world!")



if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/", basicRequesthandler)
  ])

  app.listen(3000)
  print("I am listening on port 3000")
  tornado.ioloop.IOLoop.current().start()