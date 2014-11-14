"""
Taken from Matthew Briggs
Facebook Music Group YouTube Link Extractor
Crawls a specified Facebook group and returns a list of posted YouTube
links sorted by the amount of likes each has received to maybe find good tunes.
"""

import facebook
import requests
import operator
from urlparse import urlparse

#GET A TEMPORARY TOKEN FROM https://developers.facebook.com/tools/explorer/
#UNDER GET TOKEN BUTTON CHECK 'USER_GROUPS' AND IN EXTENDED TAB 'READ_STREAM'
ACCESS_TOKEN = ''

#FIND GROUP ID BY PASTING GROUP URL INTO http://lookup-id.com/
GROUP = ''


def main():
    """
    Connect to Graph API and parse the group feed passing to link extractor
    functions. Loops through all pagination links to get every post.
    """
    all_posts = []
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    posts = graph.get_connections(GROUP, 'feed')

    while True:
        try:
            [fetch_links(post, graph, all_posts) for post in posts["data"]]
            posts = requests.get(posts['paging']['next']).json() 
        except KeyError:
            break
     
    youtube_links = only_tube(all_posts)
    write_text(youtube_links)


def fetch_links(post, graph, all_posts):
    """
    Take all group posts and get the total amount of likes for each one,
    some posts are not available due to 'external app' privacy settings
    by poster so will skip any where a link is not present in JSON
    """
    try:
        if post["source"]:
            post_link =  post["source"]
            post_id = post["id"]
            get_likes = graph.get_connections(post_id, 'likes', summary=1)
            like_count = get_likes["summary"]["total_count"]
            all_posts.append((post_link, like_count))
    except KeyError:
        pass  
    
    return all_posts


def only_tube(all_posts):
    """
    Filter out any links that are not YouTube and sort by likes descending.
    """
    youtube_links = []
    for row in all_posts:
            parsed = (urlparse(row[0]))
            video_id = parsed.path.split("/")[-1]
            if parsed.netloc == 'www.youtube.com':
               url = ('http://youtube.com/watch?v='+video_id)
               youtube_links.append((url, row[1]))
    links = sorted(youtube_links, key=operator.itemgetter(1), reverse=True)
    return links


def write_text(links):
    txt_out = open('YouTubeLinks.txt', 'wb')
    for row in links:
        txt_out.write("%s\n" % (row[0]))
    txt_out.close()


if __name__ == "__main__":
    main()
