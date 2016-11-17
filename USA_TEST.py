# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:16:12 2016

@author: Pim
"""
v0 = "alabama"; v1 = "alaska"; v2 = "arizona"; v3 = "arkansas"; v4 = "california"; 
v5 = "colorado"; v6 = "connecticut"; v7 = "delaware"; v8 = "florida"; v9 = "georgia"; 
v10 = "hawaii"; v11 = "idaho"; v12 = "illinois"; v13 = "indiana"; v14 = "iowa"; 
v15 = "kansas"; v16 = "kentucky"; v17 = "louisiana"; v18 = "maine"; v19 = "maryland"; 
v20 = "massachusetts"; v21 = "michigan"; v22 = "minnesota"; v23 = "mississippi"; 
v24 = "missouri"; v25 = "montana"; v26 = "nebraska"; v27 = "nevada"; v28 = "new hampshire"; 
v29 = "new jersey"; v30 = "new mexico"; v31 = "new york"; v32 = "north carolina"; 
v33 = "north dakota"; v34 = "ohio"; v35 = "oklahoma"; v36 = "oregon"; v37 = "pennsylvania"; 
v38 = "rhode island"; v39 = "south carolina"; v40 = "south dakota"; v41 = "tennessee"; 
v42 = "texas"; v43 = "utah"; v44 = "vermont"; v45 = "virginia"; v46 = "washington"; 
v47 = "west virginia"; v48 = "wisconsin"; v49 = "wyoming"

states = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16,
          v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31,
          v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45,
          v46, v47, v48, v49]

neighbors = {v0: [v41, v9, v8, v23], v1: [], v2: [v4, v27, v43, v5, v30], v3: [v42, v35, v24, v41, v0],
             v4: [v36, v27, v2], v5: [v2, v43, v49, v26, v15, v35, v30], v6: [v31, v20, v38],
             v7: [v19, v37, v29], v8: [v0, v9], v9: [v0, v8, v41, v32, v40], v10: [], v11: [v36, v25, v49, v43, v27],
             v12: [v24, v14, v48, v13, v16], v13: [v12, v21, v34, v16], v14: [v26, v40, v22, v48, v12, v24],
             v15: [v5, v26, v24, v35], v16: [v24, v12, v13, v34, v47, v45, v41], v17: [v42, v3, v23],
             v18: [v28], v19: [v47, v37, v7, v45], v20: [v31, v44, v28, v38, v6], v21: [v48, v34, v13],
             v22: [v40, v33, v48, v14], v23: [v17, v3, v41, v0], v24: [v35, v15, v26, v14, v12, v16, v41, v3],
             v25: [v11, v33, v40, v49], v26: [v5, v49, v40, v14, v24, v15], v27: [v4, v36, v11, v43, v2],
             v28: [v44, v18, v20], v29: [v7, v37, v31], v30: [v2, v43, v5, v35, v42], v31: [v37, v44, v20, v6],
             v32: [v41, v45, v39, v9], v33: [v25, v22, v40], v34: [v13, v21, v37, v47, v16],
             v35: [v42, v30, v5, v15, v24, v3], v36: [v4, v46, v11, v27], v37: [v47, v34, v31, v29, v7, v19],
             v38: [v6, v20], v39: [v9, v32], v40: [v49, v25, v33, v22, v14, v26], v41: [v3, v24, v16, v45, v9, v0, v23],
             v42: [v30, v35, v3, v17], v43: [v27, v11, v49, v5, v30, v2], v44: [v31, v28, v20],
             v45: [v41, v47, v19, v32], v46: [v36, v11], v47: [v16, v34, v37, v19, v45], v48: [v22, v21, v12, v14],
             v49: [v11, v25, v40, v26, v5, v43]}

zenders = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


colors_of_states = {}
for key, value in (neighbors.items()):
    print(key, len([item for item in value if item])) 

"""
def promising(state, zender):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == zender:
            return False

    return True

def get_color_for_state(state):
    for zender in zenders:
        if promising(state, zender):
            return zender

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print colors_of_states


main()
"""
