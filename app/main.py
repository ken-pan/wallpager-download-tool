import multiprocessing
import requests
import bs4
import os

from app.extractor.bing import BingExtractor
from .extractor.konachan import KonachanExtractor
from .extractor.wallpapercraft import WallpaperCraftExtractor
from .dowanloader.http import HttpDownloader
from .processor.common import Processor

bing = BingExtractor()
downloader = HttpDownloader(bing)
processor = Processor()
processor.submit(downloader.download, bing)
