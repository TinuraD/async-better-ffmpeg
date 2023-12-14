# Better FFmpeg Async
## Asynchronous fork of [Better FFmpeg Progress](https://github.com/CrypticSignal/better-ffmpeg-progress)
Runs an FFmpeg command and uses [tqdm](https://github.com/tqdm/tqdm) to show a progress bar.<br/>

## Note ⚠️
- This is originally based on [CrypticSignal's better-ffmpeg-progress](https://github.com/CrypticSignal/better-ffmpeg-progress). The only difference is, this is asynchronous. (Also unifinished project)


</div>

## Example:

```
39%|███████████████████████████████████████████ | 23.6/60.2 [00:19<00:34, 1.07s/s]
```

Where:

- `39%` is the percentage progress.
- `23.6` seconds of the input file have been processed.
- `60.2` is the duration of the input file in seconds.
- `00:19` is the time elapsed since the FFmpeg process started.
- `00:34` is the estimated time required for the FFmpeg process to complete.
- `1.07` shows how many seconds of the input file are processed per second.

## Installation:

```
pip3 install git+https://github.com/TinuraD/better-ffmpeg-async.git
```

## Usage:

Create an instance of the `FfmpegProcess` class and supply a list of arguments like you would to `subprocess.run()`.

 Example:

```py
from better_ffmpeg_async import FfmpegProcessAsync

def handle_progress_info(percentage, speed, eta, estimated_filesize):
    print(f"Estimated Output Filesize: {estimated_filesize / 1_000_000} MB")

# Pass a list of FFmpeg arguments, like you would if using subprocess.run()
process = FfmpegProcessAsync(["ffmpeg", "-i", "input.mp4", "-c:a", "libmp3lame", "output.mp3"])

# Use the run method to run the FFmpeg command.
await process.run(progress_handler=handle_progress_info)
```

## Credits
- [CrypticSignal](https://github.com/CrypticSignal/better-ffmpeg-progress)
