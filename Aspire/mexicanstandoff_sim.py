import numpy

a = .1 #worst
b = .6 #middle
c = .9 #best

''' 
better approach would be to actually write it so that the person shoots
the function which decides person to shoot at
'''

states = ['abc', 'ab', 'ac', 'bc', 'a', 'b', 'c', 'all dead']

transtition_abc = [(1-a)*(1-b)*(1-c), (1-c)*(1-(1-a)*(1-b)), c*(1-a)*(1-b), 0, (c)*(1-(1-a)*(1-b)), 0, 0, 0]
transition_ab = [0, (1-a)*(1-b), 0, 0, (1-b)*a, b*(1-a), 0, b*a]
transition_ac = [0, 0, (1-c)*(1-a), 0, (1-c)*(a), 0, (c)*(1-a),c*a]
transition_bc = [0,0,0, (1-b)*(1-c), 0, b*(1-c), (1-b)*c, b*c]
transition_a = [0,0,0,0,1,0,0,0]
transition_b = [0,0,0,0,0,1,0,0]
transition_c = [0,0,0,0,0,0,1,0]
transition_dead = [0,0,0,0,0,0,0,1]

transition_matrix = numpy.array([transtition_abc, transition_ab, transition_ac, transition_bc,
                     transition_a, transition_b, transition_c, transition_dead])

result = numpy.linalg.matrix_power(transition_matrix, 20)


print(result[0][4:7])
