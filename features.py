install=False
def good():
    global install
    install=True
def playchromecast(vid):
    install=False
    ch("pafy",good)
    if install:
        import chromecast
        chromecast.yt(vid)
