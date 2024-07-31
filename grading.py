w_grades = {
	"all-in": 5,
	"lane bully": 4,
	"hypercarry": 3,
	"mobile": 2,
	"utility": 1,
	"auto-attacker": 0,
	"poker": -1,
	"scaler": -2
}
vs_grades = {
	"scaler": 4,
	"auto-attacker": 3,
	"all-in": 2,
	"hypercarry": 1,
	"poker": -1,
	"utility": -2,
	"mobile": -3,
	"lane bully": -4
}
ranks = {
    "Z": 1.0,
    "S+": 0.9,
    "S": 0.8,
    "A+": 0.7,
    "A": 0.6,
    "B+": 0.5,
    "B": 0.4,
    "C+": 0.3,
    "C": 0.2,
    "D": 0.1,
    "F": 0.0
}
champions = {
    "Akshan": 	    "Auto-Attacker, All-in, Mobile",
	"Aphelios":     "Poker, Hypercarry, Scaler",
	"Ashe": 	    "Auto-Attacker, Poker, Utility",
	"Caitlyn": 	    "Auto-Attacker, Poker, Lane Bully",
	"Corki": 	    "All-in, Poker, Mobile",
	"Draven": 	    "Auto-Attacker, Lane Bully",
	"Ezreal": 	    "Poker, Mobile",
	"Jhin": 	    "Poker, Lane Bully, Utility",
	"Jinx": 	    "Auto-Attacker, Hypercarry, Scaler",
	"Kai'Sa":	    "Auto-Attacker, Lane Bully, Hypercarry, Scaler",
	"Kalista": 	    "Auto-Attacker, Lane Bully, Utility, Mobile",
	"Kog'Maw":	    "Auto-Attacker, Hypercarry, Scaler",
	"Lucian": 	    "All-in, Lane Bully, Mobile",
	"Miss Fortune": "Auto-Attacker, Poker, Lane Bully",
	"Nilah": 	    "Auto-Attacker, All-in, Mobile",
	"Samira": 	    "All-in, Mobile",
	"Senna": 	    "Lane Bully, Poker, Utility",
	"Smolder": 	    "Poker, Scaler",
	"Sivir": 	    "Auto-Attacker, Poker, Lane Bully, Utility",
	"Tristana":     "Auto-Attacker, All-in, Lane Bully, Mobile",
	"Twitch": 	    "Auto-Attacker, All-in, Hypercarry, Scaler",
	"Varus": 	    "Auto-Attacker, Poker, Utility",
	"Vayne": 	    "Auto-Attacker, Hypercarry, Scaler, Mobile",
	"Xayah": 	    "Auto-Attacker, Poker, Utility",
	"Yasuo": 	    "Auto-Attacker, All-in, Hypercarry, Mobile",
	"Zeri": 	    "All-in, Mobile"
}

def get_rank(eff):
    for rank in ranks:
        threshold = ranks[rank]
        if eff >= threshold:
            return rank

w_grades_total_sum = 0
w_grades_offset = 0
for key in w_grades:
    w_grade = w_grades[key]
    w_grades_total_sum += abs(w_grade)
    w_grades_offset += abs(w_grade) if w_grade < 0 else 0
vs_grades_total_sum = 0
vs_grades_offset = 0
for key in vs_grades:
    vs_grade = vs_grades[key]
    vs_grades_total_sum += abs(vs_grade)
    vs_grades_offset += abs(vs_grade) if vs_grade < 0 else 0

for champion in champions:
    print("=================", champion)

    archetypes = champions[champion].split(',')

    w_grade = 0
    vs_grade = 0
    for archetype in archetypes:
        archetype = archetype.strip().lower()
        w_grade += w_grades[archetype]
        vs_grade += vs_grades[archetype]
       
    w_eff = (w_grade + w_grades_offset) / w_grades_total_sum
    w_rank = get_rank(w_eff)
    vs_eff = (vs_grade + vs_grades_offset) / vs_grades_total_sum
    vs_rank = get_rank(vs_eff)

    #print("w/ grade:", w_grade)
    print("w/ rank:", w_rank)
    #print("w/ eff:", round(w_eff * 100), "%")
    #print("vs grade:", vs_grade)
    print("vs rank:", vs_rank)
    #print("vs eff:", round(vs_eff * 100), "%")