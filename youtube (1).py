from googleapiclient.discovery import build
from tabulate import tabulate
import subprocess
import sys
import time
print("""Hey if error occured please make sure to restart the program once excecuted.""")
# Function to check and install required packages
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if 'tabulate' is installed
try:
    from googleapiclient.discovery import build
except ImportError:
    print("The 'tabulate' package is not installed. Installing now...")
    install_package("googleapiclient.discovery")
    from googleapiclient.discovery import build

from rich.console import Console

console = Console()
console.clear()

print(r"""Developed By:
  __   ___    ______       _  _          ______        ___  
 /_ | |__ \  |____  |     | || |        |____  |      / _ \ 
  | |    ) |     / /      | || |_           / /      | (_) |
  | |   / /     / /       |__   _|         / /        > _ < 
  | |  / /_    / /     _     | |     _    / /     _  | (_) |
  |_| |____|  /_/     (_)    |_|    (_)  /_/     (_)  \___/
      
      """)
time.sleep(2.5)

# Set up YouTube API client
api_key = 'AIzaSyC5Hya2kQeWjpx9B_-nWQaE6iq_5wU_ywQ'  # Replace with your API key
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id):
    # Retrieve video details including description
    request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    response = request.execute()
    video = response['items'][0]['snippet']
    description = video['description']
    return description

def get_video_comments(video_id):
    # Retrieve comments from the video
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    )
    response = request.execute()
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

def analyze_comments(comments):
    # Basic comment analysis
    word_count = sum(len(comment.split()) for comment in comments)
    comment_count = len(comments)
    return {
        'total_comments': comment_count,
        'total_words': word_count
    }

def print_table(title, data):
    print(f"\n{title}")
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

def main_menu():
    print("\nYouTube Video Analysis")
    print("1. Get Video Description")
    print("2. Get Video Comments")
    print("3. Analyze Comments")
    print("4. Exit")

if __name__ == '__main__':
    print(r"""Well hi...!!!
          
          This tool is used to check the number of comments with simople python program with google API's
          here this can check
             1. Youtube descriptions
             2. Comments
          
          and it will ask now to enter the ID:..... 

          in this youtube link below
          https://www.youtube.com/watch?v=YOUTUBE-ID/
          
          the 'YOUTUBE-ID' is the ID 
          copy that <id> and paste when it asks

          hope you enjoy Thank you😃
          """)
    time.sleep(2.5)

    video_id = input("Enter Video ID: ").strip()

    while True:
        main_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            description = get_video_details(video_id)
            description_data = [{'Description': description}]
            print_table("Video Description", description_data)
        elif choice == '2':
            comments = get_video_comments(video_id)
            comments_data = [{'Comment': comment} for comment in comments]
            print_table("Comments", comments_data)
        elif choice == '3':
            comments = get_video_comments(video_id)
            analysis = analyze_comments(comments)
            analysis_data = [{'Total Comments': analysis['total_comments'], 'Total Words': analysis['total_words']}]
            print_table("Comments Analysis", analysis_data)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")
