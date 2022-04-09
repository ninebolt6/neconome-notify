from datetime import datetime
import unicodedata
import re

def extract_number(str):
  regex = r".*?(\d+)"
  result = re.compile(regex).match(str)
  return "-" if result is None else result.group(1)

def to_hankaku(str):
  return unicodedata.normalize("NFKC", str)

def format_date(time: datetime):
  return "{0:%Y年%m月%d日 %H時%M分%S秒}".format(time)
