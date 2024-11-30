def calculate_supplement(data):
    result = {
        "id": data["id"],
        "isEligible": False,
        "baseAmount": 0.0,
        "childrenAmount": 0.0,
        "supplementAmount": 0.0,
    }

    if not data.get("familyUnitInPayForDecember"):
        return result

    result["isEligible"] = True
    family_composition = data.get("familyComposition", "")
    num_children = data.get("numberOfChildren", 0)

    if family_composition == "single":
        result["baseAmount"] = 60.0
    elif family_composition == "couple":
        result["baseAmount"] = 120.0
    else:
        return result

    result["childrenAmount"] = num_children * 20.0
    result["supplementAmount"] = result["baseAmount"] + result["childrenAmount"]

    return result
