import socketserver
import datetime

class AfodeServer(socketserver.StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        method, *args = data.split(" ")
        try:
            response = getattr(self, "cmd_{}".format(self.data))(*args)
            self.wfile.write("0\n" + response)
        except AttributeError:
            self.wfile.write("1\nError: invalid command.")
        except Exception as e:
            self.wfile.write("2\n" + str(e))
    def cmd_current_song(self):
        return self.backend.current_song()
    def cmd_next(self):
        self.backend.next()
    def cmd_prev(self):
        self.backend.prev()
    def cmd_play(self):
        self.backend.play()
    def cmd_pause(self):
        self.backend.pause()
    def cmd_playing(self):
        return self.backend.playing()
    def cmd_paused(self):
        return self.backend.paused()
    def cmd_time(self):
        return self.backend.time()
    def cmd_subtitles(self):
        return self.backend.subtitles()
