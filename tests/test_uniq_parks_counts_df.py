import sys
sys.path.insert(0, './answers')
from answer import uniq_parks_counts_df

def test_uniq_parks_count_df():
    a = uniq_parks_counts_df("./data/frenepublicinjection2016.csv")
    try:
        out = open("tests/list_parks_count.txt","r").read()
        assert(a == out)
    except:
        out = open("tests/list_parks_count.txt","r", encoding="ISO-8859-1").read()
        assert(a == out)
