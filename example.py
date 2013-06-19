#!/usr/bin/env python

import time, random
from statemachine import State
from statemachine import FSM



# 
# 
# 
def on_state_entering(parameters, state):
	print str(parameters), 'is_running:', fsm.is_running, ' has_executed:', state.has_executed()
	if state == ready:
		time.sleep( 0.5 )
		# TODO
		next = A0
		return (next, {"prev_state":state, "message":"current: "+state.name+", next: "+next.name})
	elif state == A0:
		time.sleep( 0.5 )
		# TODO
		next = B
		return (next, {"prev_state":state, "message":"current: "+state.name+", next: "+next.name}) 
	elif state == B:
		time.sleep( 0.5 )
		# TODO
		next = C
		return (next, {"prev_state":state, "message":"current: "+state.name+", next: "+next.name})
	elif state == C:
		time.sleep( 0.5 )
		# TODO
		if random.randint(0, 1) :
			next = C
		else :
			next = A1		
		return (next, {"prev_state":state, "message":"current: "+state.name+", next: "+next.name})
	elif state == A1:
		time.sleep( 0.5 )
		# TODO
		if random.randint(0, 1) :
			next = A0
		else :
			next = D
		return (next, {"prev_state":state, "message":"current: "+state.name+", next: "+next.name})
	elif state == D:
		time.sleep( 0.5 )
		# TODO
		print 'done'


def on_state_execute_timesout( state ) :
	print 'on_state_execute_timesout', state.name

def on_fsm_ended( state ) :
	print 'on_fsm_ended', state.name



def main( ):
	global fsm

	global ready
	global A0
	global B
	global C
	global A1
	global D

	ready = State("ready", on_state_entering, 1, False)
	A0 = State("A0", on_state_entering, 2, False)
	B = State("B", on_state_entering, 2, False)
	C = State("C", on_state_entering, 2, False)
	A1 = State("A1", on_state_entering, 1, False)
	D = State("D", on_state_entering, 1, True)

	# 
	fsm = FSM(on_state_execute_timesout, on_fsm_ended)
	# add states
	fsm.add_state(ready)
	fsm.add_state(A0)
	fsm.add_state(B)
	fsm.add_state(C)
	fsm.add_state(A1)
	fsm.add_state(D)
	#
	fsm.set_start(ready)
	print 'is_running:', fsm.is_running

	#
	fsm.run( {"prev_state":None, "message":"let's go"} )
	#fsm.run("x")
	#fsm.run("x")

if __name__== "__main__":
	main( )
