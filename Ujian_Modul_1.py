# Ujian Modul 1 Data Science Rizqi Karnadi

# -------------------------- Year of Investment (20 Points) --------------------------

def calculate_years(principal, interest, tax, desired):
    
    years = 0
    while principal < desired :
        principal += (principal * interest) * (1-tax)
        years += 1
    return print(years)

calculate_years(1000.00, 0.05, 0.18, 1100.00)
calculate_years(1200.00, 0.17, 0.05, 2000.00)
calculate_years(1500.00, 0.07, 0.6, 5000.00)

# -------------------------- Number in Expanded Form (40 Points) --------------------------
# def expandedForm(num):
#     angka = str(num)
#     z = ''

#     for item in range (len(angka)) :

#         if angka[item] != '0' :
#             if item == len(angka) - 1 :
#                 z+= str(int(angka[item])) * 10**(len(angka)-1-item)
#             else :
#                 z+= str(int(angka[item]) * 10**(len(angka)-1-item)) + ' + '

#     return print(z)

# expandedForm(12)
# # expandedForm(42)
# expandedForm(70304)

# -------------------------- Build Tower (40 Points) --------------------------

# def tower_builder(n_floors, block_size):
#     width, height = block_size
#     z = ''
#     for i in range(n_floors):
#         for j in range(height):
#             for k in range((width * (n_floors - i)) - width):
#                 z += ' ' 
#             for l in range(width+(i * (width * 2))):
#                 z += '*'
#             z += '\n'
#     print(z)

# tower_builder(3,(2,3))
# tower_builder(6,(2,1))