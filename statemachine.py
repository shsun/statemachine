# **************************************************************************************
# 			                      ______
# 			                   .-"      "-.
# 			                  /    SSH     \
# 			                 |              |
# 			                 |,  .-.  .-.  ,|
# 			                 | )(__/  \__)( |
# 			                 |/     /\     \|
# 			       (@_       (_     ^^     _)
# 			  _     ) \_______\__|IIIIII|__/__________________________
# 			 (_)@8@8{}<________|-\IIIIII/-|___________________________>
# 			        )_/        \          /
# 			       (@           `--------`                    
#
# **************************************************************************************

__author__ = 'shsun'
__copyright__ = 'Copyright 2012, shsun'
__license__ = 'Apache'
__version__ = '1.1'
__email__ = '89090125@qq.com'


class State :
	#
	# name
	# handler : callback function which will be fied when entering.
	#	
	def __init__(self, name, handler, max_execute_times=1, is_end_state=False):
		self.name = name
		self.handler = handler
		self.max_execute_times = (1 if max_execute_times < 1 else max_execute_times ) 
		self.executed_times = 0
		self.is_end_state = is_end_state


class FSM :
	def __init__(self, on_state_execute_timesout=None, on_fsm_ended=None):
		# Hasb used to hold all states
		self.states = {}
		# Array used to hold all states which can be end state.
		self.endStates = []
		self.startState = None
		#
		self.on_state_execute_timesout = on_state_execute_timesout
		self.on_fsm_ended = on_fsm_ended

	# add state
	def add_state(self, state):
		self.states[state.name] = state
		if state.is_end_state:
			self.endStates.append(state.name)
	
	# set the start state.
	# name state name
	def set_start(self, state):
		self.startState = state
	
	# 
	# 
	# content the parameter what you want to pass to next-state.
	def run(self, content):
		print "run ", str(self.startState.name)
		if self.startState.name in self.states:
			handler = self.startState.handler
		else:
			raise "InitError", ".set_start() has to be called before .run()"
		if not self.endStates:
			raise  "InitError", "at least one state must be an end_state"
		oldState = self.startState
		while 1:
			(newState, content) = oldState.handler(content, oldState)
			oldState.executed_times += 1
			if oldState.executed_times > oldState.max_execute_times : 
				#print oldState.name, " reached max execute times ", oldState.max_execute_times 
				if self.on_state_execute_timesout <> None: 
					self.on_state_execute_timesout( oldState )
				break;
			if newState.name in self.endStates:
				#print "reached ", newState.name, "which is an end state"
				if self.on_fsm_ended <> None:
					self.on_fsm_ended( newState )
				break 
			else:
				handler = newState.handler
			oldState = newState
