def claim_unreserved_code_school_name(name):
    #if name == "Ada Developers Academy":
    #    raise ValueError("There's already an awesome school with that name!")
    try:
        claim_unreserved_code_school_name("Ada Developers Academy")
    except ValueError:
        return
    raise AssertionError("Expected ValueError")
    #return True