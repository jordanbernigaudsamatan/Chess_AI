import json
import itertools

# ======================================================================================
# Generate Dict of neural names + index. take promotion + castle into account.
# Save Dict into NeuralDict.json
# number of neurals : 64 x 16 + 16 x (64 + 8x4 )(promotion square for pawns taken in (for future piece with same name) + implemented for 4 different proms) + 4 (2 different castles x 2 players) = 2560 neural
# ======================================================================================


Dict = {}

PieceList = ['wRa1', 'wNb1', 'wBc1', 'wQd1', 'wKe1', 'wBf1', 'wNg1', 'wRh1', 'wPa2', 'wPb2', 'wPc2', 'wPd2', 'wPe2', 'wPf2', 'wPg2', 'wPh2',
            'bRa8', 'bNb8', 'bBc8', 'bQd8', 'bKe8', 'bBf8', 'bNg8', 'bRh8', 'bPa7', 'bPb7', 'bPc7', 'bPd7', 'bPe7', 'bPf7', 'bPg7', 'bPh7'
             ]
column_list = ['a','b','c','d','e','f','g','h']
line_list = ['1', '2', '3', '4', '5', '6', '7', '8']

square_list = []

for j,i in itertools.product(column_list,line_list) :
    square_list.append(j+i)

Neural_Dict = {}
index = 0
for piece, square in itertools.product(PieceList, square_list) :
    neural_name = piece+'->'+square
    if ('wP' in neural_name) and ('8' in neural_name) :
        for prom in ['N', 'B', 'R', 'Q'] :
            index +=1
            Neural_Dict[neural_name + '=' + prom] = index
    elif ('bP' in neural_name) and ('1' in neural_name) :
        for prom in ['N', 'B', 'R', 'Q'] :
            index+=1
            Neural_Dict[neural_name + '=' + prom] = index


    index+=1
    Neural_Dict[neural_name] = index

# Add Castle
index+=1
Neural_Dict['wO-O'] = index
index+=1
Neural_Dict['wO-O-O'] = index
index+=1
Neural_Dict['bO-O'] = index
index+=1
Neural_Dict['bO-O-O'] = index


print(index)
with open('NeuralDict.json', 'w') as f :
    json.dump(Neural_Dict, f)