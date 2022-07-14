def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    f_to_c = (temp - 32) * 5 / 9
    c_to_f = temp * 9 / 5 + 32
    same_unit = temp

    if unit_in != "f" and unit_in != "c":
      return f"Invalid unit {unit_in}"
    elif unit_out != "f" and unit_out != "c":
      return f"Invalid unit {unit_out}"
    elif unit_in == "f":
      if unit_out == "f":
        return same_unit
      else: # unit_out == "c"
        return f_to_c
    else: # unit_in == "c"
      if unit_out == "c":
        return same_unit
      else: # unit_out == "f"
        return c_to_f


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
