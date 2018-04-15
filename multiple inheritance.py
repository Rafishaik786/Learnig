class Music(object):
    def song(self):
        print("this is song method")
    def lyric(self):
        print('this is lyric method')
class Dance():
    def compose(self):
        print('iam composing this song')
    def mild(self):
        print('iam watching this dance')
class Watch(Dance,Music,):
    def write(self):
        print('iam writing a story' )
    def reading(self):
        print('iam reading a book')

bavi=Watch()

bavi.song()
bavi.lyric()

bavi.compose()
bavi.mild()
bavi.write()
bavi.reading()
