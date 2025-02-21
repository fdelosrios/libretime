from typing import List

from libretime_playout.config import Config


def make_config_with_stream(**kwargs) -> Config:
    return Config(
        **{
            "general": {
                "public_url": "http://localhost:8080",
                "api_key": "some_api_key",
            },
            "stream": kwargs,
        }
    )


TEST_STREAM_CONFIGS: List[Config] = [
    make_config_with_stream(),
    make_config_with_stream(
        outputs={
            "icecast": [
                {
                    "enabled": True,
                    "mount": "main",
                    "source_password": "hackme",
                    "audio": {"format": "ogg", "bitrate": 256},
                    "name": "LibreTime!",
                    "description": "LibreTime Radio! Stream #1",
                    "website": "https://libretime.org",
                    "genre": "various",
                },
                {
                    "enabled": False,
                    "mount": "second",
                    "source_password": "hackme",
                    "audio": {"format": "mp3", "bitrate": 256},
                },
            ],
        }
    ),
    make_config_with_stream(
        outputs={
            "shoutcast": [
                {
                    "enabled": True,
                    "source_password": "hackme",
                    "audio": {"format": "mp3", "bitrate": 256},
                    "name": "LibreTime!",
                    "description": "LibreTime Radio! Stream #1",
                    "website": "https://libretime.org",
                    "genre": "various",
                },
            ],
        }
    ),
    make_config_with_stream(
        outputs={
            "icecast": [
                {
                    "enabled": True,
                    "mount": "main",
                    "source_password": "hackme",
                    "audio": {"format": "ogg", "bitrate": 256},
                },
            ],
            "shoutcast": [
                {
                    "enabled": True,
                    "source_password": "hackme",
                    "audio": {"format": "mp3", "bitrate": 256},
                },
            ],
        }
    ),
    make_config_with_stream(
        outputs={
            "system": [{"enabled": True, "kind": "pulseaudio"}],
        }
    ),
    make_config_with_stream(
        outputs={
            "system": [{"enabled": False, "kind": "alsa"}],
        }
    ),
]
