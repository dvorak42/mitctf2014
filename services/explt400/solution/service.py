import tornado.httpclient
import tornado.process
import tornado.ioloop
import tornado.tcpserver
import tornado.netutil
import tornado.gen
import time


tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

DIR = "/"

def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body


MENU="""Mars Data Retriever
Menu:
  (1) List data files
  (2) Upload data file
  (3) Install flag
  (4) Upload flag
"""

FILES = [""]


class Server(tornado.tcpserver.TCPServer):
	@tornado.gen.coroutine
	def handle_stream(self, stream, address):
		print "Connection from ", address
		flagLoaded = False

		while True:
			try:
				stream.write(MENU)
				client = tornado.httpclient.AsyncHTTPClient()

				line = yield stream.read_until("\n")
				num = int(line.strip())
				
				if num == 1:
					stream.write("0\n\n")
				elif num == 2:
					stream.write("URL:  ")
					url = (yield stream.read_until("\n")).strip()
					headers = {
						"User-Agent": "curl 7.35.0 (x86_64-pc-linux-gnu) libcurl/7.35.0 OpenSSL/1.0.1f zlib/1.2.8"
					}
					print "URL:", url
					if not url.startswith("https://"):
						stream.write("I will only upload files through HTTPS Protocol, because that's how much I care about security.\n\n")
						continue

					try:
						r = yield client.fetch(url, headers=headers)
						stream.write("Done!\n\n")
					except Exception as e:
						stream.write(str(e) + "\n\n")
				elif num == 3:
					stream.write("Loading flag...\n")
					yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout,
										   time.time() + 1)
					flagLoaded = True
					stream.write("Done! I put the flag somewhere in the memory.\n\n")
				elif num == 4:
					if flagLoaded:
						yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout,
											   time.time() + 2)
						stream.write("Flag sent to Space Patrol.\n\n")
					else:
						stream.write("Load flag first.\n\n")
				else:
					stream.write("Command not recognized.\n\n")
			except Exception as e:
				print e
				break

		stream.close()

def main():
	sockets = tornado.netutil.bind_sockets(4433)
	tornado.process.fork_processes(0)
	server = Server()
	server.add_sockets(sockets)
	ioloop = tornado.ioloop.IOLoop.instance()
	ioloop.start()

if __name__ == "__main__":
	main()
