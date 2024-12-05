from ytube_api import Ytube
yt = Ytube()
search_results = yt.search_videos(
   "Alan Walker songs"
)
target_video = search_results.items[0]
download_link = yt.get_download_link(
   target_video,
   format="mp3",
   quality="320"
   )
saved_to = yt.download(
   download_link,
   progress_bar=True,
   quiet=False
)
print(saved_to)
"""
/home/smartwa/git/smartwa/ytube-api/Alan Walker, Putri Ariani, Peder Elias - Who I Am (Official Music Video) - Alan Walker (youtube).mp3
"""
