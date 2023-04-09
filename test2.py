import vlc

# путь к libvlc
vlc_path = "/usr/lib/x86_64-linux-gnu/libvlc.so"

# создание экземпляра
instance = vlc.Instance("--no-xlib", "--quiet", "--plugin-path", vlc_path)