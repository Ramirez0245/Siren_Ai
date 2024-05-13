These scripts are based on 4-5 software installation

This script uses Whisper AI on the local machine for speech to text.

Installations for Voice Recording
1. pip install pyaudio 
2. pip install wave

Installations needed to Whisper Ai.
1. This script work only got 3.7-3.10 Python. Install appropriate version
2. Installing PyTorch for local version, a machine learning library. 
    NOTE: Please make sure if using CUDA that you have a NVIDA graphics card else select CPU option on website. THis can cause errors if not selected correctly.
3. Install FFmpeg based on your OS. Is used to read different audio files.
    macOS: https://ffmpeg.org/download.html
    Windows: https://chocolatey.org/install. Install by using command from webpage on powershell and as admin.
    NOTE: After chocolity run choco install ffmpeg in powershell.
4. Lastly install Whisper AI by command 'pip install -U openai-whisper'

After installations run voice_recoder script for voice recording.
After open command prompt where audio files are saved and run "whisper myrecoding.wav"

Result is the Text to speech file.

NOTE: Need to integreate the whisper command into script. Currently getting cannot open using the os libary. 
