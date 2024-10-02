import subprocess

def down_yt(url):
    try:
        print("Downloading...")
        subprocess.run(['yt-dlp', '-f ba', '-o', 'video.%(ext)s', url], check=True)
        print(f"Succesfully converted")
    except Exception as e:
       print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    down_yt(url)
