import json
import pandas as pd

file = "hashmap.json"
data = None
with open(file,'r') as f:
  data = json.load(f)

channel_id, stats = data.popitem()

print(channel_id)

channel_stats = stats["channel_statistics"]
video_stats = stats["video_data"]

sorted_vids = sorted(video_stats.items(),key=lambda item: int(item[1]["viewCount"]), reverse=True)

stats = []
for video in sorted_vids:
  video_id = video[0]
  title = video[1]["title"]
  likes = video[1]["likeCount"]
  dislikes = video[1]["dislikeCount"]
  comments = video[1]["commentCount"]
  publishedAt = video[1]["publishedAt"]
  description = video[1]["description"]
  views = video[1]["viewCount"]
  stats.append([video_id,title,views,likes,dislikes, publishedAt, description, comments])

  df = pd.DataFrame(stats, columns=['video_id','title','views','likes','dislikes','publishedAt','description','comments'])

file = "youtube.xlsx"
df.to_excel(file)