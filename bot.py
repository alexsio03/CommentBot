import subprocess
import whisper
import torch
import os
import glob
from transformers import pipeline

def down_yt(url):
    try:
        for file in glob.glob('audio.*'):
            os.remove(file)
        print("\nDownloading...\n")
        subprocess.run(['yt-dlp', '-f', 'ba', '-o', 'audio.%(ext)s', url], check=True)
        print("\nSuccesfully converted\n")
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def transcribe_audio():
    try:
        for file in glob.glob('text.txt'):
            os.remove('text.txt')
        print("\nBeginning transcription...\n")
        model = whisper.load_model("medium")
        result = [{'text': 'hello there!'}]
        for file in glob.glob('audio.*'):
            result = model.transcribe(file)
        return result['text']
    except Exception as e:
        print(f"Error transcribing: {e}")
        return None

def gen_comments(text): 
    for file in glob.glob('comment.txt'):
        os.remove(file)
    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="cuda",
    )
    messages = [
        {"role": "system", "content": "Given the transcript to a YouTube video, generate 3-4 comments on it. One comment can ask a question, the rest should just comment on the contents of the video."},
        {"role": "video_transcript", "content": text},
    ]
    print("\nBeginning comment generation...\n")
    outputs = pipe(
        messages,
        max_new_tokens=256,
    )
    return outputs[0]["generated_text"][-1]["content"]


if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    audio = down_yt(url)
    if audio:
        text = transcribe_audio()
        if text:
            with open("text.txt", "w") as f:
                f.write(text)
            print("\nTranscribed\n")
            comment = gen_comments(text)
            print("\nComments generated\n")
            if comment:
                with open("comment.txt", "w") as f:
                    f.write(comment)
        else:
            print("Could not transcribe")
