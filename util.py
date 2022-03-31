import unicodedata
import re

def extract_number(str):
  regex = ".*?(\d+)"
  return re.compile(regex).match(str).group(1)

def to_hankaku(str):
  return unicodedata.normalize("NFKC", str)

# TODO: pytestでテスト書きたい