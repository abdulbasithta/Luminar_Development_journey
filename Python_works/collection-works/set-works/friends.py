

all_user={"sachin","abd","kohli","panth","dhoni","bumra","siraj","yuvi"}

sachin_frnds={"abd","kohli","panth","dhoni"}

yuvi_frnds={"panth","dhoni","bumra","siraj"}

# display suggestion for sachin

suggestions=all_user.difference(sachin_frnds)

suggestions.remove("sachin")

# mutual friends

mutual_frnds=sachin_frnds.intersection(yuvi_frnds)

print(mutual_frnds)

st1={10,20,30,40}

st2={100,10,200,20,300}

symmetric_set=st1.symmetric_difference(st2)

# a union b  -  a inter b

print(symmetric_set) # 30,40,100,200,300
