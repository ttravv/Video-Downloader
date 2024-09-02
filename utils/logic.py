import yt_dlp


def get_direct_link(url):
    ydl_opts = {
        "format": "bestvideo[height>=720]+bestaudio/best[height>=720]",
        "quiet": True,
        "no_warnings": True,
        "outtmpl": "%(id)s.%(ext)s",
        "merge_output_format": "mp4",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    L = info_dict["formats"]
    for x in range(len(L)):
        if L[x].get("height", 0) == 1280:
            direct_link = L[x]["url"]
            return direct_link
