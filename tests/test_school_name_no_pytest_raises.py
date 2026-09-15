from school_name import claim_unreserved_code_school_name

def test_invalid_name_no_pytest():
    # Implement the equivalent of this test logic but DO NOT import or otherwise access pytest:

    # with pytest.raises(ValueError):
    #     claim_unreserved_code_school_name("Ada Developers Academy")

    # Think about what the test actually does and think about how to write them ourselves.

    # Replace this with your own logic
    try:
        claim_unreserved_code_school_name("Ada Developers Academy")
    except ValueError:
        return
    raise AssertionError("Expected ValueError")
    #raise Exception("test not implemented")