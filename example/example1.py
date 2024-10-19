#!/usr/bin/python


# python3 -m venv nome_do_ambiente
# pip install quiz_for_kids
# source nome_do_ambiente/bin/activate
# python3 example.py

import quiz_for_kids as qfk

variables = ["x", "y", "z"]
equations, data = qfk.linear_system.integer_equations(variables, var_min=1,var_max=4, coef_min=-1,coef_max=3, in_extensive=True)

print("Sistema de equações:")
print("\n".join(equations))


print(qfk.tex.from_numpy_array(data["coefficients"]))

print("\nData:")
print(data)
