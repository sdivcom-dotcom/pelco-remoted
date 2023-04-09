import vlc

# путь к libvlc
vlc_path = "/usr/lib/x86_64-linux-gnu/"

# создание экземпляра
instance = vlc.Instance("--no-xlib", "--quiet", "--plugin-path", vlc_path)

# создание медиа
media = instance.media_new("rtsp://192.168.11.50", "sout=#display")

# создание плеера
player = instance.media_player_new()

# установка медиа для плеера
player.set_media(media)

# запуск плеера
player.play()