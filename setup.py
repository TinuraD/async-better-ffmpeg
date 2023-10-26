from setuptools import setup

setup(
    name="better-ffmpeg-async",
    version="1.0",
    packages=["better-ffmpeg-async"],
    install_requires=[
        "ffmpeg-python",
        "tqdm",
        "asyncio",
    ],
)
