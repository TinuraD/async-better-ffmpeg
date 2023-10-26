from setuptools import setup

setup(
    name="better-ffmpeg-async",
    version="1.0",
    packages=["better_ffmpeg_async"],
    install_requires=[
        "ffmpeg-python",
        "tqdm",
        "asyncio",
    ],
)
