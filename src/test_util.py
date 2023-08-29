import pytest
import datetime
from util import to_hankaku, extract_number, format_date

@pytest.mark.parametrize(('str', 'expected'), [
  ("３", "3"),
  ("⑨", "9"),
  ("3番", "3番"),
  ("１０番", "10番"),
  ("ただいま　９９９番　をお呼びしています。", "ただいま 999番 をお呼びしています。")
])
def test_to_hankaku(str, expected):
  assert to_hankaku(str) == expected

@pytest.mark.parametrize(('str', 'expected'), [
  ("", "-"),
  ("ただいま診療時間外です。", "-"),
  ("3番", "3"),
  ("１０番", "１０"),
  ("ただいま 109番 をお呼びしています。", "109")
])
def test_extract_number(str, expected):
  assert extract_number(str) == expected

def test_format_date():
  case_1 = datetime.date(2022, 2, 22)
  assert format_date(case_1) == "2022年02月22日 00時00分00秒"
  case_2 = datetime.datetime.now()
  assert format_date(case_2) == "{:0>4}年{:0>2}月{:0>2}日 {:0>2}時{:0>2}分{:0>2}秒".format(case_2.year, case_2.month, case_2.day, case_2.hour, case_2.minute, case_2.second)