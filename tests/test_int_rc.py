import os
import unittest

branch_coverage = {
    "branch_1": False,
    "branch_2": False, 
}

def _int_rc(text):
    rc = text.find('rc')
    if rc >= 0:
        branch_coverage["branch_1"] = True
        text = text[:rc]
    else:
        branch_coverage["branch_2"] = True
    return int(text)

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

def test_int_rc_text_positiveOrZero_returns_9876():
    result = _int_rc("9876")  


def test_int_rc_text_positiveOrZero_returns_neg333():
    result = _int_rc("-333")  


def test_int_rc_text_is_not_positiveOrZero_returns_333():
    result = _int_rc("333rc") 


def test_int_rc_text_is_not_positiveOrZero_returns_321():
    result = _int_rc("321rc555") 
   
def test_int_rc_text_is_not_positiveOrZero_returns_3456():
    result = _int_rc("3456rc555rc")

def calculate_coverage():
    hit_branches = 0
    for branch, hit in branch_coverage.items():
        if hit:
          hit_branches = hit_branches + 1
    total_branches = len(branch_coverage)
    coverage = (hit_branches / total_branches) * 100
    print("Coverage is", coverage, "%")
    
test_int_rc_text_positiveOrZero_returns_9876()
test_int_rc_text_positiveOrZero_returns_neg333()
test_int_rc_text_is_not_positiveOrZero_returns_333()
test_int_rc_text_is_not_positiveOrZero_returns_321()
test_int_rc_text_is_not_positiveOrZero_returns_3456()
print_coverage()
calculate_coverage()