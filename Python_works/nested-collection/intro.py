
"""
collection inside collection

data=[
    [],[],[]
    
] list of list

data=[
    {key:value},{key:value},{key:value}

] list of dictionary

"""

students=[
    {"id":1,"name":"basith","qualifiaction":"bca","college":"st joseph","pass_out_year":2025},
    {"id":2,"name":"abhin","qualifiaction":"btech","college":"ace","pass_out_year":2025},
    {"id":3,"name":"adarsh","qualifiaction":"bca","college":"amstk","pass_out_year":2025},
    {"id":4,"name":"aibin","qualifiaction":"btech","college":"mbits","pass_out_year":2024},
    {"id":5,"name":"alfiya","qualifiaction":"bsccs","college":"kmm","pass_out_year":2025},
]

# for st in students:

#     print(st.get("name"))

# for st in students:

#     print(st.get("college"))

all_st_names=[st.get("name") for st in students]

print(all_st_names)

all_st_college=[st.get("college") for st in students]

print(all_st_college)

bca_st_name=[st.get("name") for st in students if st.get("qualifiaction")== "bca"]

print(bca_st_name)

st_pass_2025=[st.get("name") for st in students if st.get("pass_out_year")==2025]

print(st_pass_2025)
