# 111

# 222

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


class State:
    '''
    entering_callback : callback function which will be fired when entering.
    '''

    def __init__(self, name, entering_callback, max_execute_times=1, is_end_state=False):
        self.name = name
        self.entering_callback = entering_callback
        self.max_execute_times = (1 if max_execute_times < 1 else max_execute_times)
        self.executed_times = 0
        self.is_end_state = is_end_state

    def has_executed(self):
        return self.executed_times > 0


class FSM:
    def __init__(self, on_state_execute_timesout=None, on_fsm_ended=None):
        # Hasb used to hold all states
        self.states = {}
        # Array used to hold all states which can be end state.
        self.end_states = []
        self.start_state = None
        #
        self.on_state_execute_timesout = on_state_execute_timesout
        self.on_fsm_ended = on_fsm_ended
        self.is_running = False

    # add state
    def add_state(self, state):
        self.states[state.name] = state
        if state.is_end_state:
            self.end_states.append(state.name)

    # set the start state.
    def set_start(self, state):
        self.start_state = state

    #
    #
    # parameter the parameter what you want to pass to target-state.
    def run(self, parameter):
        # print "run ", str(self.start_state.name)
        if self.start_state.name in self.states:
            entering_callback = self.start_state.entering_callback
        else:
            raise "InitError", "please call set_start() before call run()"
        if not self.end_states:
            raise "InitError", "the FSM need at least 1 end_state"
        old_state = self.start_state
        while 1:
            self.is_running = True
            (new_state, parameter) = old_state.entering_callback(parameter, old_state)
            old_state.executed_times += 1
            if old_state.executed_times > old_state.max_execute_times:
                # print old_state.name, " reached max execute times ", old_state.max_execute_times
                if self.on_state_execute_timesout <> None:
                    self.on_state_execute_timesout(old_state)
                    self.is_running = False
                break;
            if new_state.name in self.end_states:
                # print "reached ", new_state.name, "which is an end state"
                if self.on_fsm_ended <> None:
                    self.on_fsm_ended(new_state)
                    self.is_running = False
                break
            else:
                entering_callback = new_state.entering_callback
            old_state = new_state
